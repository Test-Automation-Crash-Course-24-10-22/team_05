import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.maximize_window()

def scroll():
    browser.get('https://rozetka.com.ua/ua/asus-90nb0ty1-m00vf0/p346597995/')
    browser.execute_script("window.scrollTo(0, 1000);")
    time.sleep(3)

def button_click():
    button_for_topics = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[1]/div/rz-lazy-render/div/button')
    button_for_topics.click()
    time.sleep(3)

scroll()
button_click()

