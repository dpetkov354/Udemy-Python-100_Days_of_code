from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = Service(r"C:\Users\Dimitar Petkov\Selenium\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie_for_clicking = driver.find_element(by=By.ID, value="cookie") # the cookie we are going to click
score = driver.find_element(by=By.ID, value="money")                # get the score

#####SHOP#####
cursor = driver.find_element(by=By.ID, value="buyCursor")
grandma = driver.find_element(by=By.ID, value="buyGrandma")
factory = driver.find_element(by=By.ID, value="buyFactory")
shipment = driver.find_element(by=By.ID, value="buyShipment")
alchemy_lab = driver.find_element(by=By.ID, value="buyAlchemy lab")
portal = driver.find_element(by=By.ID, value="buyPortal")
time_machine = driver.find_element(by=By.ID, value="buyTime machine")

# #####Logick#####
# timeout = time.time() + 60 * 5                                      #5 min loop timer
#
# while time.time() < timeout:                                        #Loop to stop after reaching 5 min
#     time.sleep(1)                                                   #Reduce startup lag
#     cookie_for_clicking.click()
#     check = driver.find_element(by=By.ID, value="money")
#     check_num = int(check)
#     if time.time() % 5 == 0:
#         if check_num <= driver.find_element(by=By.XPATH, value='//*[@id="buyTime machine"]/b/text()[2]'):
#            time_machine.click()
#         elif check_num <= driver.find_element(by=By.XPATH, value='//*[@id="buyPortal"]/b/text()[2]'):
#             portal.click()
#         elif check_num <= driver.find_element(by=By.XPATH, value='//*[@id="buyAlchemy lab"]/b/text()[2]'):
#             alchemy_lab.click()
#         elif check_num <= driver.find_element(by=By.XPATH, value='//*[@id="buyShipment"]/b/text()[2]'):
#             shipment.click()
#         elif check_num <= driver.find_element(by=By.XPATH, value='//*[@id="buyFactory"]/b/text()[2]'):
#             factory.click()
#         elif check_num <= driver.find_element(by=By.XPATH, value='//*[@id="buyGrandma"]/b/text()[2]'):
#             grandma.click()

check = driver.find_element(by=By.ID, value="money")
print(check)
