from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSfJ7OhRIyT5Ri91-ZN7LoVSOCBmy4VLxmedsv3Iw9orNPqvRQ/viewform?usp=" \
            "sf_link"
CHROME_DRIVER_PATH = Service(r"C:\Users\Dimitar Petkov\Selenium\chromedriver.exe")

###### DATA SCRAPING ######

links = []
prices = []
for page in range(1, 2):
    URL = f"https://www.imot.bg/pcgi/imot.cgi?act=3&slink=86g212&f1={page}"
    response = requests.get(URL, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/102.0.0.0 Safari/537.36",
        "Accept-Language": "bg-BG,bg;q=0.9"})

    soup = BeautifulSoup(response.text, 'html.parser')

    price_list = soup.find_all("div", class_="price", )
    [prices.append(price.getText()) for price in price_list]

    link_list = soup.find_all(class_="photoLink")
    [links.append(link.get("href")) for link in link_list[2:42]]
    print(f"Found {len(prices)} entries.")
time.sleep(3)

##### FORM FILLING ######

driver = webdriver.Chrome(service=CHROME_DRIVER_PATH)
time.sleep(3)
driver.get(FORM_LINK)
time.sleep(3)

for entry in range(0, 5):
    time.sleep(2)
    price_entry = driver.find_element(by=By.XPATH,
                                      value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div['
                                            '1]/div/div[1]/input')
    time.sleep(3)
    price_entry.send_keys(prices[entry])
    link_entry = driver.find_element(by=By.XPATH,
                                     value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                           '1]/div/div[1]/input')
    time.sleep(3)
    link_entry.send_keys(links[entry])
    entry = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    time.sleep(3)
    entry.click()
    time.sleep(3)
    re_entry = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    re_entry.click()
    time.sleep(3)
