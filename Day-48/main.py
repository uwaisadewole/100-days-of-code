from selenium import webdriver
from selenium.webdriver.common.by import By

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--headless")


driver = webdriver.Firefox(firefox_options)
driver.get("https://www.amazon.com/XIAOMI-Compatible-25080RABDG-Unlocked-Liberado/dp/B0FXBJZ9JK/ref=sr_1_1?crid=26F506L4BCA6A&dib=eyJ2IjoiMSJ9.f0B4b6KIr8PjGc9_CHW1KAv6WDE8qS77KFOwFBAsG_wkpANoWXNG6_2VHVbOrRDNiRLRaUGn9UnsTGTRzbEIontqI58PnG8I4yRx3Jykh-y4p0SXMQfMrhQamYbxn0kFrcQtev3w4bWJ8jR3ZDAmrcVIL35eqKIi_W8DEMTC4Nn83xpA35iHYUlJrO7cqefUHAchqvYbK04xjmE4ksN1_et7URZz_uCEL2xr25Il3OY.JheYcvDmjUo-kaEzbzIB1Tc8RMt9dhzQNEWtseKnPGE&dib_tag=se&keywords=redmi%2Bnote%2B15%2Bpro&qid=1794564163&sprefix=redmi%2Caps%2C612&sr=8-1&th=1")

price_naira = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is {price_naira.text}.{price_cents.text}")

search_bar = driver.find_element(By.NAME, value="field-keywords")
print(search_bar.tag_name)

link = driver.find_element(By.CSS_SELECTOR, value=".a-text-center a")
print(link.text)



input("Press Enter to close the browser...")
driver.quit()