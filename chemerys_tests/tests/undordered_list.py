import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def scroll():
    browser.get('https://rozetka.com.ua/ua/acer-nxa8eeu002/p357787248/')
    browser.execute_script("window.scrollTo(0, 600);")
    time.sleep(2)

def unordered_list_buttons():
    ul_button_1 = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[2]/rz-product-main-info/rz-additional-services/div/div/ul/li[1]/rz-service-item/label')
    ul_button_2 = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[2]/rz-product-main-info/rz-additional-services/div/div/ul/li[2]/rz-service-item/label')

    ul_buttons = [ul_button_1, ul_button_2]
    for x in ul_buttons:
        x.click()
        time.sleep(1)
        x.click()
        time.sleep(1)

def unordered_list_options():
    ul_option_1 = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[2]/rz-product-main-info/rz-additional-services/div/div/ul/li[1]/rz-service-item/ul/li[1]/label')
    ul_option_2 = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[2]/rz-product-main-info/rz-additional-services/div/div/ul/li[1]/rz-service-item/ul/li[2]/label')
    ul_option_3 = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[2]/rz-product-main-info/rz-additional-services/div/div/ul/li[2]/rz-service-item/ul/li/label')
    ul_option_4 = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[2]/rz-product-main-info/rz-additional-services/div/div/ul/li[2]/rz-service-item/ul/li[2]/label')

    ul_options = [ul_option_1, ul_option_2, ul_option_3, ul_option_4]
    for y in ul_options:
        y.click()
        time.sleep(1)

def information_buttons():
    information_button_1 = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[2]/rz-product-main-info/rz-additional-services/div/div/ul/li[1]/rz-service-item/label/button')
    information_button_1.click()
    time.sleep(2)
    exit_button_1 = browser.find_element(By.XPATH, '/html/body/app-root/rz-single-modal-window/div[3]/div[1]/button')
    exit_button_1.click()
    time.sleep(2)

    information_button_2 = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[2]/rz-product-main-info/rz-additional-services/div/div/ul/li[2]/rz-service-item/label/button')
    information_button_2.click()
    time.sleep(2)
    exit_button_2 = browser.find_element(By.XPATH, '/html/body/app-root/rz-single-modal-window/div[3]/div[1]/button')
    exit_button_2.click()
    time.sleep(2)

scroll()
unordered_list_buttons()
unordered_list_options()
information_buttons()

