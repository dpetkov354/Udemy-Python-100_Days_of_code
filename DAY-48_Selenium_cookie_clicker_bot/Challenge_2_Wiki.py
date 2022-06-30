from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys    # to enter keyboard keys

chrome_driver_path = Service(r"C:\Users\PETKOV\Dev\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# time_event = driver.find_element(by=By.XPATH, value='//*[@id="articlecount"]/a[1]')
#
# print(time_event.text)

# all_portals = driver.find_element(by=By.LINK_TEXT, value="Talk") # get to a link via the displayed name of the link
# all_portals.click()                                              # clicks on the link to open it

search = driver.find_element(by=By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)   # using the keys library of selenium we import Keys to use to click keyboard keys

driver.quit()
