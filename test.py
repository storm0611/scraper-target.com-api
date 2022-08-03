import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import pyautogui
from pathlib import Path
import time

#insert full path to your video file here
path = os.getcwd() + "\\final.mp4"  # your video path
# print(path)
##FacebookUser = 'Justsendit@live.com'

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\justs\\AppData\\Local\\Google\\Chrome\\User Data")
chromedriver = "./chromedriver"
capabilities = webdriver.DesiredCapabilities.CHROME.copy()
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options, desired_capabilities=capabilities)
    
driver.get("https://drive.google.com/drive/my-drive")
    
elements = driver.find_elements(
        By.CSS_SELECTOR, 'button[aria-label="New"]')
time.sleep(3)
print(len(elements))
elements[0].click()
time.sleep(2)
elements = driver.find_elements(
        By.CSS_SELECTOR, 'div[role="menuitem"][aria-posinset="2"]')
time.sleep(3)
print(len(elements))
elements[0].click()
time.sleep(3)

    # global path
pyautogui.write(path)
time.sleep(2)
pyautogui.press('enter')
time.sleep(8)

    #checking video upload
elements = driver.find_elements(
    By.CSS_SELECTOR, 'div[role="dialog"][aria-label="Uploading 1 item"]')
time.sleep(2)
if len(elements):
    print("Video is posted!")

    
