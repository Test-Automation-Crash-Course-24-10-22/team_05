import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def scroll():
    browser.get('https://rozetka.com.ua/ua/asus-90nb0ty1-m00vf0/p346597995/')
    browser.execute_script("window.scrollTo(0, 200);")
    time.sleep(2)

def first_comparement():
    button_for_comparement = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[2]/rz-product-main-info/div[1]/div[1]/ul/li[3]/ul/li[1]')
    button_for_comparement.click()
    time.sleep(1)

def second_comparement():
    button_for_comparement_2 = browser.find_element(By.XPATH, '/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/ul/li[5]/rz-comparison/button')
    button_for_comparement_2.click()
    time.sleep(1)
    comparement_exit = browser.find_element(By.XPATH, '/html/body/app-root/rz-single-modal-window/div[3]/div[1]/button')
    comparement_exit.click()
    time.sleep(1)

    button_for_comparement_2.click()
    time.sleep(1)
    delete_button = browser.find_element(By.XPATH, '/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-comparison-modal/ul/li/button')
    delete_button.click()
    time.sleep(1)
    comparement_exit_2 = browser.find_element(By.XPATH, '/html/body/app-root/rz-single-modal-window/div[3]/div[1]/button')
    comparement_exit_2.click()
    time.sleep(1)

def favourite_button():
    button_for_favourite = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[2]/rz-product-main-info/div[1]/div[1]/ul/li[3]/ul/li[2]/app-goods-wishlist/button')
    button_for_favourite.click()
    time.sleep(1)
    button_for_exit = browser.find_element(By.XPATH, '/html/body/app-root/rz-single-modal-window/div[3]/div[1]/button')
    button_for_exit.click()
    time.sleep(1)

scroll()
first_comparement()
second_comparement()
favourite_button()

