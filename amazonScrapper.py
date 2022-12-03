import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.amazon.com/s?k=laptops&crid=10JSZVCBVGZBT&sprefix=laptops%2Caps%2C501&ref=nb_sb_noss_1")
time.sleep(4)
titles = driver.find_elements(By.CSS_SELECTOR,".a-size-medium.a-color-base.a-text-normal")
print(titles[0].text)
    