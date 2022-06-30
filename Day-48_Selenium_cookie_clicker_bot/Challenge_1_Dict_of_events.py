from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = Service(r"C:\Users\PETKOV\Dev\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("https://www.python.org/")

time_event = driver.find_elements(
    by=By.CSS_SELECTOR,
    value=".medium-widget.event-widget.last > div > ul > li > time"
)

time_list = [event.text for event in time_event]

title_event = driver.find_elements(
    by=By.CSS_SELECTOR,
    value=".medium-widget.event-widget.last > div > ul > li > a"
)
titles_list = [title.text for title in title_event]

driver.quit()

events = {}
for n in range(len(time_event)):
    events[n] = {
        "time": time_list[n],
        "name": titles_list[n],
    }

print(events)

driver.quit()
