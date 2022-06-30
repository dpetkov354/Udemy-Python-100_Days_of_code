################## Selenium start-up #######################

from selenium import webdriver
from selenium.webdriver.chrome.service import Service                # needed to set up driver path
from selenium.webdriver.common.by import By                          # needed to search with find element by=

chrome_driver_path = Service(r"C:\Users\PETKOV\Dev\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
########################################################################################################################

driver.get("https://www.python.org/")
########################################################################################################################
# search_bar = driver.find_element(by=By.NAME, value="q")           # search with an ID
# print(search_bar.tag_name)                                        #gets tag name from HTML
# print(search_bar.get_attribute("placeholder"))                    #gets specific attributes from HTML
########################################################################################################################
# logo = driver.find_element(by=By.CLASS_NAME, value="python-logo")   # gets the logo by class name
# print(logo.size)                                                    # prints the size of the logo
########################################################################################################################
# documentation_link = driver.find_element(                             # searching by css selectors
#     by=By.CSS_SELECTOR,                                               # can put multiple with a space between them as
#     value=".documentation-widget a"                                   # shown a CLASS and an Anchor
# )
# print(documentation_link.text)
########################################################################################################################
# link = driver.find_element(by=By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a') #search via right click on
#                                                                             #the HTML row hit copy then copy XPATH,
#                                                                             # the value is the copied XPATH
# print(link.text)

driver.quit()
