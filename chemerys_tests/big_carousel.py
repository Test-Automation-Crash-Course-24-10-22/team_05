import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.get('https://rozetka.com.ua/ua/asus-90nb0ty1-m00vf0/p346597995/')
browser.execute_script("window.scrollTo(0, 200);")
time.sleep(2)

right_arrow = browser.find_element(By.CLASS_NAME, 'simple-slider__control--next')
x = 0
while x < 14:
    right_arrow.click()
    time.sleep(1)
    x += 1

left_arrow = browser.find_element(By.CLASS_NAME, 'simple-slider__control--prev')
y = 0
while y < 14:
    left_arrow.click()
    time.sleep(1)
    y += 1






