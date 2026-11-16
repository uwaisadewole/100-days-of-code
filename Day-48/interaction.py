from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--headless")


driver = webdriver.Firefox()
# driver.get("https://en.wikipedia.org/wiki/Main_Page")


# article_count = driver.find_element(By.ID, value="mwDw")
# # print(article_count.text)
# # article_count.click()
# content_portals = driver.find_element(By.LINK_TEXT, value="start editing the article")
# # content_portals.click()

# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# search_button = driver.find_element(By.XPATH, value="/html/body/div[2]/header/div[2]/div/div/div/div/form/div/button")

# search_button.click()

#challenge

driver.get("http://secure-retreat-92358.herokuapp.com/")


first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Uwais")
first_name.send_keys(Keys.ENTER)

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Adewole")
last_name.send_keys(Keys.ENTER)

e_mail = driver.find_element(By.NAME, value="email")
e_mail.send_keys("uniisihe9efh@gmail.com")
e_mail.send_keys(Keys.ENTER)

sign_up = driver.find_element(By.CSS_SELECTOR, value=".text-center button")
sign_up.submit()




input("Press enter to quit...")

driver.quit()