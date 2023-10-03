# libraries
import requests
from bs4 import BeautifulSoup
import smtplib
import lxml

# constants
AMAZON_URL = "https://www.amazon.com/dp/B076B6GYJW/ref=sspa_dk_detail_4?ie=UTF8&psc=1&pd_rd_i=&pd_rd_i=B076B6GYJWp13NParams&s=musical-instruments&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM"
BUDGET = 160

# header
header = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept-Language" : "en-US,en;q=0.9"
}

# get request to get the amazon page
product_response = requests.get(AMAZON_URL,headers=header).text

# create a soup and create a parser
soup = BeautifulSoup(product_response,"lxml")

# grab all the items with the class a-offscreen
span_fetch = soup.find_all("span",class_="a-offscreen")

# fetch the price out of the list and convert it to a float
price_str = span_fetch[1].text
price_float = float(price_str.split("$")[1])

# if price is in the budget then shoot an email
if price_float < BUDGET:

    my_email = "pratham.doshi95@gmail.com"
    my_password = "xfqfetfzzqkagqrn"
    to_email = "praths.doshi@gmail.com"

    email_context = f"Subject: Amazon Item Lower Price\n\n Hi There! Your Amazon Item is in your Budget today. Please make the purchase:\n\n{AMAZON_URL}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=email_context)