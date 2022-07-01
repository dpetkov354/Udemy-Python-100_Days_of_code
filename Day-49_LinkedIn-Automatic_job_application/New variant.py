from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

chrome_driver_path = Service(r"C:\Users\PETKOV\Dev\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("JOB SEARCH LINK")

sign_in = driver.find_element(by=By.XPATH, value="/html/body/div[5]/a[1]")

time.sleep(3)

sign_in.click()

time.sleep(3)

user_sign_in = driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
user_name = driver.find_element(by=By.ID, value="username")
user_pass = driver.find_element(by=By.ID, value="password")
user_name.send_keys("ACCOUNT NAME")
user_pass.send_keys("PASSWORD")
user_sign_in.click()

time.sleep(3)

jobs = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
i = 1
print(len(jobs))

for job in jobs:
    try:
        job.click()
        time.sleep(4)
        save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
        save_button.click()
        time.sleep(2)
        print(f"Job {i} saved")
        i += 1
    except NoSuchElementException:
        print(f"Job {i} skipped")
        i += 1
        continue
