################## Selenium start-up #######################

from selenium import webdriver
from selenium.webdriver.chrome.service import Service   # needed to set up driver path
from selenium.webdriver.common.by import By             # needed to search with find element by=

chrome_driver_path = Service(r"C:\Users\PETKOV\Dev\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
############################################################

driver.get("https://www.amazon.com/EVGA-GeForce-08G-P5-3767-KL-Technology-Backplate/dp/B097CLCXDX/ref=sr_1_1?crid="
           "38LC7KKWJ5LUO&keywords=3070&qid=1655271436&sprefix=3070%2Caps%2C157&sr=8-1")

price = driver.find_element(by=By.ID, value="corePrice_feature_div")   # search with an ID
print(price.text)
driver.quit()
