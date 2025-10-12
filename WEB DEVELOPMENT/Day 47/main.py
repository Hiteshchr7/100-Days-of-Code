import requests
import os
import smtplib
from dotenv import load_dotenv
from bs4 import BeautifulSoup
load_dotenv()
smtp_add = os.environ.get("smtp_address")
my_email = os.environ.get("my_email")
my_pass = os.environ.get("my_password")
url_static = "https://appbrewery.github.io/instant_pot/"
url_live = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1&language=en_US&currency=INR"
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,en-IN;q=0.8",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Microsoft Edge\";v=\"140\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
  }
response  = requests.get(url_live,headers=header)
soup = BeautifulSoup(response.text,"html.parser")
price_whole = soup.find(name="span", class_ = "a-price-whole").getText()
price_decimal = soup.find(name="span", class_ = "a-price-fraction").get_text()
current_price = float(price_whole+price_decimal) 
title = soup.find(id="productTitle").get_text().strip()
print(current_price)
if current_price < 100 :
    with smtplib.SMTP(smtp_add,port=587) as connection :
        connection.starttls()
        connection.login(user=my_email,password=my_pass)
        connection.sendmail(from_addr=my_email,to_addrs=my_email,msg= f"Subject:Amazon Price Alert! \n\n{title} is on sale for ${current_price}\n{url_live}".encode("utf-8"))