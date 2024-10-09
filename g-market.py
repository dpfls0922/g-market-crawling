import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd

headers = {
    'authority': 'www.gmarket.co.kr',
    'accept': '*/*',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    # 'cookie': 'cosemkid=go16896720606128759; pguid=21728281872911008892010000; cguid=11728281872911008892000000; sguid=31728281872911008892000000; jaehuid=200011415; kwid=go16896720606128759; lnd_kwd=undefined; 9b5ac327653ddb71c4abb11d9b645ca3=2b3cd2e6280efb742caf44303703c838; _ga=GA1.1.1311353796.1728281882; charset=enUS; currency=USD; shipNation=KR; PCUID=17282820159916308856625; cto_bundle=N_S0OV9xb2J3U0VRWiUyRnpjU3ZoZVVvVGYxZ0c3dWV0WmVpZFc2UUpUTVI4YW1XN3hWbXpyU3BmYnZSSFRTMkhwcCUyRlM3MXFpU2k1dno2eGZnUW5FJTJCcFI2cldhelY5RTg5aUVyVmZRbVBQQiUyQnB3TUtkM1FsJTJGNWYwQ09MJTJGVDhraXhab0lzU2d6cU54d0NlJTJGNEFRcWhyTyUyQko2MzUyampMYTJIQ1ElMkJFdlN0c1hvYUlxWUElM0Q; Sif=bd67acb7ded97bd9616211c020f3eb18; gmktloadingtimecheck=N; user%5Finfo=isNego=N; BASKET%5FCALLBACK%5FSTAT=F; Pif=E9F8C5476690D6E17BFF5A32D38D4947E4FE37D1DA7AC012C0A5847EC49224291D22FBD47366DD0997DF347D2714B15F; ASPSESSIONIDSSSBQBTD=HACFENMAAFLLFNCHPBNCIBFM; shipnation=KR; ASPSESSIONIDCSBBCBQA=MMPBDAKCEJBBNMOHFFHMGMDH; ssguid=317282969549540028322000000; __cf_bm=YMZfkjWFRMlf4CnaDUebU0ShcA3QPTlkQKKmtManwjI-1728360438-1.0.1.1-fYTRB9eWXNVwBAFSG7H_MhUFfUayJV6KtjxRZ0mMis2QA0R.YVP1vRsd3Xe7S8HsjFpEqfNW1PYwuygftvSdfw; _cfuvid=lK5EINUe683nxUIXi_6OQ5LYfN.ne8_AlH5VehvogJQ-1728360438692-0.0.1.1-604800000; mtguid=Pzberowgvuaycrwqyryudfydvlf1728360438933; cf_clearance=kKBxyJfeloB3a9xDr_xw8Lp.hK7VEk3fzAiuRnDCl1U-1728360440-1.2.1.1-ROyxejFUuaLnQhUmPxcBGyYYiJz7BghoJFu.yU0Jfu5riBXeM1lC484Gx_SOJV095NF7znwuP0z8CkyX4zIrCxRnsPs45zlFFYlEX4sb6CH1HQZriNSKAr1wzilcpdJSEW9Q2Wbsejmwsbc8kxD0ZyUlH8O6V3Q6VMxdS19W5MHqkPGd1aefNpdnYeYeZWr1xwYd8VhfMgJl78PXGHeFsISvMgVpJaUq3kzqGnwAiNo4pvc2GBsO0aw0kgiWTwkYMLyzlrZQ1.r9rhxEmveu_stoSUbjtOQf5.EpjQcMve8isUsRzPy0BzlwKNOYNQwuGu7SkygRiVI7dYBmg0vOQqUF1wbx5pu.lKVxtlUxu8oHB0b9xOl7ek1q0Tg4gFDm5q2q_gIrQEqZoKBfnu3AVw; mont_fph=1ece8e8ba63cbdd4279a484b3e78e9cf; _gcl_gs=2.1.k1$i1728360438; 6361c5a58da80370cd396c77654e6153=0b6f9bacabed184de5db39e48df805aa; _gcl_aw=GCL.1728360445.Cj0KCQjwjY64BhCaARIsAIfc7YbpysOPaF0yzodC9_QSzFAXGltqvy1IzGHbZXXX2m_-uPCjHsznqLcaAhdyEALw_wcB; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22qohQweWOuz9vXTN4c%2FjsUPY0ceIltows0QjorUMEX2c%3D%22%2C%22expiryDate%22%3A%222025-10-08T04%3A07%3A24.530Z%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22MxiAby35e12Iz5Fl0RtF%22%2C%22expiryDate%22%3A%222025-10-08T04%3A07%3A24.530Z%22%7D; mont_fpt=1728360444698; _ga_1BYVQK09SB=GS1.1.1728360440.4.1.1728360660.60.0.0',
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

def gmarket():
    url = Request('https://www.gmarket.co.kr/n/best', headers=headers)

    html = urlopen(url)

    soup = BeautifulSoup(html, 'html.parser')


    product_list = []
    items = soup.find_all('li', class_='list-item')
    for item in items:
        product = {
            'rank': item.select_one('.box__label-rank').text.strip() if item.select_one('.box__label-rank') else "No rank",  # 순위 추가
            'title': item.select_one('.box__item-title').text.strip() if item.select_one('.box__item-title') else "No title",
            'discount': item.select_one('.box__discount .text__value').text.strip() if item.select_one('.box__discount .text__value') else "No discount",
            'original_price': item.select_one('.box__price-original .text__value').text.strip() if item.select_one('.box__price-original .text__value') else "No original price",
            'sale_price': item.select_one('.box__price-seller .text__value').text.strip() if item.select_one('.box__price-seller .text__value') else "No sale price",
            'free_delivery': item.select_one('.icon__delivery-free img')['alt'] if item.select_one('.icon__delivery-free img') else "No free delivery",
            'image_url': "https:" + item.select_one('.box__thumbnail img')['src'] if item.select_one('.box__thumbnail img') else "No image",  # 이미지 URL
            'product_url': item.find('a')['href'] if item.find('a') else "No product URL"  # 상품 URL
        
        }
        product_list.append(product)

    for product in product_list:
        print(f"Rank: {product['rank']}")
        print(f"Title: {product['title']}")
        print(f"Discount: {product['discount']}")
        print(f"Original Price: {product['original_price']} 원")
        print(f"Sale Price: {product['sale_price']} 원")
        print(f"Free Delivery: {product['free_delivery']}")
        print(f"Image URL: {product['image_url']}")
        print(f"Product URL: {product['product_url']}")
        print("-" * 40)

    try:
        df = pd.DataFrame(product_list)
        df.to_csv('g_items_전체.csv', index=False, encoding='utf-8-sig')  # UTF-8로 인코딩하여 CSV로 저장
        print("CSV 파일이 성공적으로 저장되었습니다.")
    except Exception as e:
        print(f"CSV 파일 저장 중 오류 발생: {e}")


gmarket()