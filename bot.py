from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= chrome_options)

driver.get("https://www.amazon.com/Active-Shirts-Athletic-Running-Workout/dp/B0B728PPRG/ref=sr_1_4?adgrpid=173230357154&dib=eyJ2IjoiMSJ9.zriT-Q2hT3S5-bvz0xgALuUkPfd7pXQLA1qYEkqj5nWWO9wYY_a6fh4qU3V1xpmq9Uju7hQr4-7pkEKveurkRCQXdWrrDkEHFdBSR9cs8IteKS0WCi93VblC5yjAWfUUu8DolndQWej2TVL-lCvhdAtH4Sajex5D-BinsFzx45XUPPID8xaHD15YmrFaytU57fUYKNmdFVFpifHgZRSkxhaF-wDFiQiTImXp57xGAb5mR8n2qEUsKN31AeOUXbp3deAG4Wut-v7cN6xxp0_tIsNWTC5OpTO1r8WriuthnpM.GfONb40Am7DudijVprXq8Asmui4oDpoc67oMc5h9Ms0&dib_tag=se&hvadid=720670981880&hvdev=c&hvlocphy=1011086&hvnetw=g&hvqmt=e&hvrand=5812415258543251917&hvtargid=kwd-31416861&hydadcr=13660_13578542&keywords=amazon%2Bus&mcid=a03e8e430ef93df5a4dfe724b533d69d&qid=1775819906&sr=8-4&th=1&psc=1")

price_dollar = driver.find_element(By.CLASS_NAME, value = "a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

print(f"The price is {price_dollar.text}.{price_cents.text}")

driver.quit()