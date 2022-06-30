from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import ElementClickInterceptedException

INSTAGRAM_NAME = "USERNAME"
INSTAGRAM_PASSWORD = "PASSWORD"
PAGE = "PAGE"
CHROME_DRIVER_PATH = Service(r"C:\Users\Dimitar Petkov\Selenium\chromedriver.exe")


class InstaFollowerBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)
        cookie_cancel = self.driver.find_element(by=By.XPATH, value='/html/body/div[4]/div/div/button[1]')
        cookie_cancel.click()
        time.sleep(2)
        user_name = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        user_name.send_keys(INSTAGRAM_NAME)
        user_pass = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        user_pass.send_keys(INSTAGRAM_PASSWORD)
        time.sleep(2)
        login_click = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
        login_click.click()
        time.sleep(2)

    def find_followers(self):
        time.sleep(2)
        self.driver.get(f"https://www.instagram.com/{PAGE}")
        time.sleep(2)
        followers = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(2)
        modal = self.driver.find_element(by=By.XPATH, value='/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow_followers(self):
        all_buttons = self.driver.find_elements(by=By.CSS_SELECTOR, value="li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value='/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollowerBot()
bot.login()
time.sleep(5)
bot.find_followers()
