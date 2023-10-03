import requests
from bs4 import BeautifulSoup
import lxml

AMAZON_URL = "https://www.amazon.com/dp/B076B6GYJW/ref=sspa_dk_detail_4?ie=UTF8&psc=1&pd_rd_i=&pd_rd_i=B076B6GYJWp13NParams&s=musical-instruments&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM"
BUDGET = 160

header = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept-Language" : "en-US,en;q=0.9"
}

product_response = requests.get(AMAZON_URL,headers=header).text

soup = BeautifulSoup(product_response,"lxml")

span_fetch = soup.find_all("span",class_="a-offscreen")

price_str = span_fetch[1].text
price_float = float(price_str.split("$")[1])

