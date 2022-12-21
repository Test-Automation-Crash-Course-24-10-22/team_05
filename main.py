import time
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://rozetka.com.ua/ua/asus-90nb0ty1-m00vf0/p346597995/')
button = browser.find_element(By.ID, "rzintersectionobserver")

button.click()
time.sleep(5)
