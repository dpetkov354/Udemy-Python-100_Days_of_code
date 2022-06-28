from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import speedtest
import time

PROMISED_UP = 100
PROMISED_DOWN = 100
TWITTER_NAME = "INSERT_NAME_HERE"
TWITTER_PASSWORD = "INSERT_PASSWORD_HERE"
CHROME_DRIVER_PATH = Service(r"C:\Users\PETKOV\Dev\chromedriver.exe")


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=CHROME_DRIVER_PATH)
        self.st = speedtest.Speedtest()
        self.up = self.get_internet_upload_speed()
        self.down = self.get_internet_download_speed()
        self.st = speedtest.Speedtest()

    def get_internet_upload_speed(self):
        print("Fetching upload speeds...")
        upload = round(self.st.upload() / 1000000, 2)
        return upload

    def get_internet_download_speed(self):
        print("Fetching download speeds...")
        download = round(self.st.download() / 1000000, 2)
        return download

    def tweet_at_provider(self, ):
        self.driver.get("https://twitter.com/")
        time.sleep(3)

        cookie_cancel = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div[2]'
                                                                    '/div[2]/div/span/span')
        cookie_cancel.click()
        time.sleep(3)

        sign_in = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]'
                                                              '/div[1]/div/div[3]/div[5]/a/div')
        sign_in.click()
        time.sleep(3)

        user_name = self.driver.find_element(by=By.XPATH, value='//*[@autocomplete="username"]')
        user_name.send_keys(TWITTER_NAME)
        user_name.send_keys(Keys.ENTER)
        time.sleep(3)

        user_pass = self.driver.find_element(by=By.XPATH, value='//*[@autocomplete="current-password"]')
        user_pass.send_keys(TWITTER_PASSWORD)
        user_pass.send_keys(Keys.ENTER)
        time.sleep(3)

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for " \
                f"{PROMISED_DOWN}down/{PROMISED_UP}up?"

        user_tweet = self.driver.find_element(by=By.XPATH, value='//*[@class="public-DraftStyleDefault-block public-'
                                                                 'DraftStyleDefault-ltr"]')
        user_tweet.send_keys(tweet)
        tweet_it = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/'
                                                               'div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/'
                                                               'div[3]/div/div/div[2]/div[3]')
        tweet_it.click()
        time.sleep(3)


bot = InternetSpeedTwitterBot()
bot.tweet_at_provider()
