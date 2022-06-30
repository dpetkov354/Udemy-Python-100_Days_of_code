from bs4 import BeautifulSoup
import requests
import smtplib

MY_EMAIL = "mrboxxer95@gmail.com"
MY_PASSWORD = "kdeztiqwomejygyl"
ITEM_NAME = "EVGA GeForce RTX 3070"
URL = "https://www.amazon.com/EVGA-GeForce-08G-P5-3767-KL-Technology-Backplate/dp/B097CLCXDX/ref=sr_1_1?crid=" \
      "38LC7KKWJ5LUO&keywords=3070&qid=1655271436&sprefix=3070%2Caps%2C157&sr=8-1"

# Scraping
response = requests.get(URL, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    "Accept-Language": "bg-BG,bg;q=0.9"})

soup = BeautifulSoup(response.text, 'lxml')
price = soup.find('span', class_='a-price a-text-price a-size-medium apexPriceToPay')
price_num = float(((price.getText()).split("$")).pop())

# Send E-mail
if price_num <= 700:
    message = f"The price of {ITEM_NAME} dropped to ${price_num}\nLINK: {URL}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Price below threshold\n\n{message}".encode('utf-8')
        )
