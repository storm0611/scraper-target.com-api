import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import pyautogui
from pathlib import Path

path_to_profile = os.path.abspath(os.getcwd()) + '\chrome'
user_data_dir = Path("{}/driver/User Data".format(path_to_profile))

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir={}".format(user_data_dir))
options.add_argument('--profile-directory=Default')
path = os.getcwd() + "\\final.mp4"  # your video path

driver = webdriver.Chrome(options=options)
driver.get("https://gofile.io/uploadFiles")
time.sleep(5)
driver.switch_to.frame(0)
max_timeout = 10
while max_timeout > 0:
    max_timeout -= 1
    time.sleep(1)
    buttons = driver.find_elements(By.XPATH, '//button')
    for button in buttons:
        if button.get_attribute('class') == 'uploadButton':
            button.click()
            max_timeout = 0
            print("upload button pressed!")
            break

time.sleep(5)
pyautogui.write(path)
time.sleep(2)
pyautogui.press('enter')
time.sleep(5)
print("waiting for file to be uploaded!")
