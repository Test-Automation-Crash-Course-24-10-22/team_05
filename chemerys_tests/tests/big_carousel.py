import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.maximize_window()

def scroll():
    browser.get('https://rozetka.com.ua/ua/asus-90nb0ty1-m00vf0/p346597995/')
    browser.execute_script("window.scrollTo(0, 300);")
    time.sleep(2)

def right_click():
    right_arrow = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[1]/div/rz-product-gallery-main/app-slider[1]/div[1]/button[2]')
    x = 0
    while x < 14:
        right_arrow.click()
        time.sleep(1)
        x += 1

def left_click():
    left_arrow = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[1]/div/rz-product-gallery-main/app-slider[1]/div[1]/button[1]')
    y = 0
    while y < 14:
        left_arrow.click()
        time.sleep(1)
        y += 1

scroll()
right_click()
left_click()

