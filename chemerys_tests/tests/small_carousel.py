import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.get('https://rozetka.com.ua/ua/asus-90nb0ty1-m00vf0/p346597995/')
browser.execute_script("window.scrollTo(0, 600);")
time.sleep(2)

right_arrow = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[1]/div/rz-product-gallery-main/app-slider[2]/div/button[2]')
right_arrow.click()
time.sleep(2)
left_arrow = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[1]/div/rz-product-gallery-main/app-slider[2]/div/button[1]')
left_arrow.click()
time.sleep(2)

slide_1 = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[1]/div/rz-product-gallery-main/app-slider[2]/div/div/ul/li[1]/rz-gallery-main-thumbnail-image/button')
slide_2 = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[1]/div/rz-product-gallery-main/app-slider[2]/div/div/ul/li[2]/rz-gallery-main-thumbnail-image/button')
slide_3 = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[1]/div/rz-product-gallery-main/app-slider[2]/div/div/ul/li[3]/rz-gallery-main-thumbnail-image/button')
slide_4 = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[1]/div/rz-product-gallery-main/app-slider[2]/div/div/ul/li[4]/rz-gallery-main-thumbnail-image/button')
slide_5 = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[1]/div/rz-product-gallery-main/app-slider[2]/div/div/ul/li[5]/rz-gallery-main-thumbnail-image/button')
slide_6 = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[1]/div/rz-product-gallery-main/app-slider[2]/div/div/ul/li[6]/rz-gallery-main-thumbnail-image/button')
slide_7 = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[1]/div/rz-product-gallery-main/app-slider[2]/div/div/ul/li[7]/rz-gallery-main-thumbnail-image/button')
slide_8 = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[1]/div/rz-product-gallery-main/app-slider[2]/div/div/ul/li[8]/rz-gallery-main-thumbnail-image/button')
slide_9 = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[1]/div/rz-product-gallery-main/app-slider[2]/div/div/ul/li[9]/rz-gallery-main-thumbnail-image/button')
slide_10 = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[1]/div/rz-product-gallery-main/app-slider[2]/div/div/ul/li[10]/rz-gallery-main-thumbnail-image/button')
slide_11 = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[1]/div/rz-product-gallery-main/app-slider[2]/div/div/ul/li[11]/rz-gallery-main-thumbnail-image/button')
slide_12 = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[1]/div/rz-product-gallery-main/app-slider[2]/div/div/ul/li[12]/rz-gallery-main-thumbnail-image/button')
slide_13 = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[1]/div/rz-product-gallery-main/app-slider[2]/div/div/ul/li[13]/rz-gallery-main-thumbnail-image/button')
slide_14 = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[1]/div/rz-product-gallery-main/app-slider[2]/div/div/ul/li[14]/rz-gallery-main-thumbnail-image/button')
slide_15 = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[1]/div/rz-product-gallery-main/app-slider[2]/div/div/ul/li[15]/rz-gallery-main-thumbnail-image/button')
slide_0 = browser.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[1]/div/rz-product-gallery-main/app-slider[2]/div/div/ul/li[1]/rz-gallery-main-thumbnail-image/button')

list = [slide_1, slide_2, slide_3, slide_4, slide_5, slide_6, slide_7, slide_8, slide_9, slide_10, slide_11, slide_12,
        slide_13, slide_14, slide_15]

for x in list:
    x.click()
    time.sleep(1)

reversed_list = [slide_14, slide_13, slide_12, slide_11, slide_10, slide_9, slide_8, slide_7, slide_6, slide_5,
                 slide_4, slide_3, slide_2, slide_1, slide_0]

for y in reversed_list:
    if y == slide_5:
        left_arrow.click()
        time.sleep(2)
    y.click()
    time.sleep(1)

