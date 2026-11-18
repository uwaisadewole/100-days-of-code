from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
import time


# Tell geckodriver to connect to the already running Firefox on port 2828
service = Service(service_args=['--marionette-port', '2828', '--connect-existing'])
driver = webdriver.Firefox(service=service)


# # driver = webdriver.Firefox()
# # driver.get("https://orteil.dashnet.org/cookieclicker/")

# try:
#     driver.find_element(By.ID, "langSelect-EN").click()
#     time.sleep(2)
# except Exception:
#     pass
# count = 100

# click = driver.find_element(By.ID, value="bigCookie")


# # 5 minutes = 300 seconds
# INTERVAL = 60
# next_check = time.time() + INTERVAL
# TOP = 180
# while True:
#     click.click()
#     if time.time() >= next_check:
#         print("5 minutes passed! Checking store items...")
#         cookie_per_sec = driver.find_element(By.ID, value="cookiesPerSecond")
#         print(f"cookies/persecond: {cookie_per_sec.text}")
#         store_items = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
#         if store_items:
#             store_items[-1].click()
            

#         next_check = time.time() + INTERVAL
        

        


# input("Press enter to exit...")
# driver.quit()


five_sec_check = time.time() + 5
five_min_stop = time.time() + 300

big_cookie = driver.find_element(By.ID, "bigCookie")

try:
    print("Bot running... Press Ctrl+C in the terminal to stop early.")
    while True:
        big_cookie.click()

        # Check store every 5 seconds
        if time.time() >= five_sec_check:
            items = driver.find_elements(By.CSS_SELECTOR, "#store .product.unlocked.enabled")
            if items:
                items[-1].click()
            five_sec_check = time.time() + 5

        # Stop automatically after 5 minutes
        if time.time() >= five_min_stop:
            print("\n5 minutes reached!")
            break

except KeyboardInterrupt:
    # Catches Ctrl+C without dumping a messy traceback
    print("\nBot manually stopped by user.")

finally:
    # Always runs whether stopped by timer, Ctrl+C, or an error
    try:
        cps = driver.find_element(By.ID, "cookiesPerSecond").text
        cookies = driver.find_element(By.ID, "cookies").text.split("\n")[0]
        print(f"Final Cookies: {cookies} | {cps}")
    except Exception:
        print("Could not read final score.")

    # Cleanly shuts down geckodriver (use driver.quit() if Selenium launched Firefox)
    # Note: If attached via --connect-existing, driver.quit() will also close your Firefox window
    driver.quit()
    print("Driver closed cleanly.")