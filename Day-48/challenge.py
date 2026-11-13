from selenium import webdriver
from selenium.webdriver.common.by import By


firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--headless")

driver = webdriver.Firefox(firefox_options)
driver.get("https://www.python.org/events")


event_time = driver.find_elements(By.CSS_SELECTOR, value=".most-recent-events time")

event_name = driver.find_elements(By.CSS_SELECTOR, value=".most-recent-events a")


events = {}
for n in range(len(event_time)):
    events[n] = {
        "time": event_time[n].text,
        "name": event_name[n].text,
    }

print(events)


driver.quit()

