from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")
name_input = driver.find_element(By.CSS_SELECTOR, value=".top")
name_input.send_keys("Sarosh", Keys.TAB)

last_name_input = driver.find_element(By.CSS_SELECTOR, value=".middle")
last_name_input.send_keys("Khan", Keys.TAB)

email_input = driver.find_element(By.CSS_SELECTOR, value=".bottom")
email_input.send_keys("saroshkhan@gmail.com", Keys.TAB)


btn = driver.find_element(By.CSS_SELECTOR, value=".btn")
btn.send_keys(Keys.ENTER)


