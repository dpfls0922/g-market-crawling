import json
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import urlparse, parse_qs
import pandas as pd


headers = {
    'authority': 'www.gmarket.co.kr',
    'accept': '*/*',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.gmarket.co.kr',
    'referer': 'https://www.gmarket.co.kr/n/best',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}


def fetch_html(url):
    req = Request(url, headers=headers)
    return urlopen(req).read()


def get_category1(soup):
    category1_elements = soup.select('.box__1depth-filter .swiper-slide')
    category1 = [
        {
            'name': category.select_one('.text__category').text.strip(),
            'groupCode': parse_qs(urlparse(category.select_one('.link__category')['href']).query).get('groupCode', [None])[0]
        }
        for category in category1_elements
    ]
    return category1


def get_category2_and_products(group_code):
    if group_code:
        sub_url = f"https://www.gmarket.co.kr/n/best?groupCode={group_code}"
        html = fetch_html(sub_url)
        sub_soup = BeautifulSoup(html, 'html.parser')

        category2_elements = sub_soup.select('.list__category-filter .list-item')
        return [
            {
                'category2': category2.select_one('.text__category').text.strip(),
                'products': get_product_data(f"https://www.gmarket.co.kr{category2.select_one('.link__category')['href']}")
            }
            for category2 in category2_elements
        ]


def get_product_data(url):
    html = fetch_html(url)
    soup = BeautifulSoup(html, 'html.parser')

    products = []
    product_elements = soup.find_all('li', class_='list-item')

    for product in product_elements:
        products.append({
                'rank': product.select_one('.box__label-rank').text.strip() if product.select_one('.box__label-rank') else "No rank",
                'name': product.select_one('.box__item-title').text.strip() if product.select_one('.box__item-title') else "No title",
                'imgUrl': "https:" + product.select_one('.box__thumbnail img')['src'] if product.select_one('.box__thumbnail img') else "No image",
                'price': extract_price(product, '.box__price-original .text__value'),
                'price_sale': extract_price(product, '.box__price-seller .text__value'),
                'sale_rate': extract_discount(product, '.box__discount .text__value'),
                'linkUrl': product.find('a')['href'] if product.find('a') else "No product URL"
            })

    return products


def extract_price(product, selector):
    price_element = product.select_one(selector)
    return int(price_element.text.strip().replace(',', '')) if price_element else 0


def extract_discount(product, selector):
    discount_element = product.select_one(selector)
    return int(discount_element.text.strip().replace('%', '')) if discount_element else 0


def write_to_csv(result):
    try:
        df = pd.DataFrame(result)
        df.to_csv('g_items_total.csv', index=False, encoding='utf-8-sig')
        print("CSV 파일이 성공적으로 저장되었습니다.")
    except Exception as e:
        print(f"CSV 파일 저장 중 오류 발생: {e}")


def crawl_gmarket_best(group_code=None):
    url = 'https://www.gmarket.co.kr/n/best'
    html = fetch_html(url)
    soup = BeautifulSoup(html, 'html.parser')

    category1 = get_category1(soup)

    result = {'category1': []}
    for category in category1:
        group_code = category.get('groupCode')
        if group_code:
            category2_with_products = get_category2_and_products(group_code)
            result['category1'].append({
                'category1': category['name'],
                'data': category2_with_products
            })

    write_to_csv(result)
    return result


product_data = crawl_gmarket_best()
print(json.dumps(product_data, ensure_ascii=False, indent=4))