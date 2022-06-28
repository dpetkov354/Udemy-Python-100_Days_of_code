from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys  #USED IF REQUEST FOR PHONE NUMBER IS USED
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

FB_EMAIL = "FB_NAME"
FB_PASSWORD = "FB_PASS"
# PHONE_NUMBER = "PHONE_NUMBER" # IF FONE NUMBER IS REQUESTED

chrome_driver_path = Service(r"C:\Users\PETKOV\Dev\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

######## ENTERING TINDER AND ACCEPTING LOGGING WITH FB ################################################################

driver.get("https://tinder.com/app/recs")
time.sleep(2)
sign_in = driver.find_element(by=By.XPATH,
                              value='//*[@id="t1836739397"]'
                                    '/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
sign_in.click()
time.sleep(2)
with_fb = driver.find_element(by=By.XPATH,
                              value='//*[@id="t108358321"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')

######## SWITHCING TO FB PAGE TO ENTER LOGGING INFORMATION ############################################################

window_before = driver.window_handles[0]                   # saves tinder window position
with_fb.click()
time.sleep(2)
window_after = driver.window_handles[1]                    # saves FB window position
driver.switch_to.window(window_after)                      # switched to FB
allow_cookies = driver.find_element(By.XPATH, '//*[contains(@id, "u_0_a_")]')
allow_cookies.click()
time.sleep(2)
driver.switch_to.window(window_after)
next_click = driver.find_element(by=By.CSS_SELECTOR, value="[id^=u_0_0_")
user_name = driver.find_element(by=By.XPATH, value='//*[@id="email"]')
user_pass = driver.find_element(by=By.XPATH, value='//*[@id="pass"]')
user_name.send_keys(FB_EMAIL)
user_pass.send_keys(FB_PASSWORD)
next_click.click()
time.sleep(5)
driver.switch_to.window(window_before)                      # switched back to TINDER
time.sleep(5)

############ IF FONE NUMBER IS REQUESTED ##############################################################################

# phone_number = driver.find_element(By.XPATH, '//*[@id="t108358321"]/div/div/div[1]/div/div[2]/div/input')
# phone_number.send_keys(PHONE_NUMBER)
# phone_click = driver.find_element(By.XPATH, '//*[@id="t108358321"]/div/div/div[1]/div/button')
# time.sleep(3)
# phone_click.send_keys(Keys.ENTER)

######## ACCEPTING TINDER POP-UPS #####################################################################################

allow = driver.find_element(by=By.XPATH,
                            value='//*[@id="t108358321"]/div/div/div/div/div[3]/button[1]/span')
allow.click()
dont_accept = driver.find_element(by=By.XPATH,
                                  value='//*[@id="t108358321"]/div/div/div/div/div[3]/button[2]/span')
dont_accept.click()

######## SWIPING #####################################################################################
for n in range(100):
    time.sleep(2)
    try:
        print("called")
        like_button = driver.find_element(by=By.XPATH,
                                          value='//*[@id="content"]'
                                                '/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(by=By.XPATH, value=".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)

driver.quit()
