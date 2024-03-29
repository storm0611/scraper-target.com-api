#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Abe
#
# Created:     27/07/2022
# Copyright:   (c) Abe 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import requests
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import pyautogui
from pathlib import Path

import bs4
import json
import sys
from selenium.webdriver.remote.webelement import WebElement
import codecs


#insert full path to your video file here
path = os.getcwd() + "\\final.mp4" # your video path
##FacebookUser = 'Justsendit@live.com'
##FacebookPass = 'Temp1234!'

FacebookUser = 'Justsendit@live.com'
FacebookPass = 'Temp1234!!'

InstagramUser = 'Mesaliquidation@gmail.com'
InstagramPass = 'Temp1234'


path_to_profile = os.path.abspath(os.getcwd()) + '\chrome'
user_data_dir = Path("{}/driver/User Data".format(path_to_profile))


def check_exists_by_xpath(xpath):
    try:
        global driver
        driver.find_element(By.XPATH, xpath)
    except:
        return False
    return True

def uploadToInstagram():
    global InstagramUser, InstagramPass, driver, driver, user_data_dir


##    options = webdriver.ChromeOptions()
##    options.add_argument("--user-data-dir={}".format(user_data_dir))
##    options.add_argument('--profile-directory=Default')
##
##    driver = webdriver.Chrome(options = options)

    driver.get("https://www.instagram.com/")
    time.sleep(8)

##    my_email=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
##    my_email.send_keys(InstagramUser)
##
##    my_password=driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
##    my_password.send_keys(InstagramPass)
##    time.sleep(2)
##
##    login=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]')
##    login.click()
##    time.sleep(5)



    upload=driver.find_element(By.XPATH,'//div[@class="_acub"]')
    print("upload button press!")
    upload.click()


    #Select from computer
##    upload=driver.find_element(By.XPATH,'//button[@class="_acan _acap _acas"]')
##    upload.click()

    max_timeout = 90
    while max_timeout>0:
        max_timeout-=1
        time.sleep(1)
        allButtons = driver.find_elements(By.XPATH,'//button')
        for button in allButtons:
            if button.text == "Select from computer":
                print("Select from computer button press!")
                button.click()
                max_timeout = 0
                break

    #/html/body/div[8]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button
    #/html/body/div[7]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button
    time.sleep(8)

    global path
    pyautogui.write(path)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(5)

    max_timeout = 90
    while max_timeout>0:
        max_timeout-=1
        time.sleep(1)
        allButtons = driver.find_elements(By.XPATH,'//button')
        for button in allButtons:
            if button.text == "Next":
                print("Next button press!")
                button.click()
                max_timeout = 0
                break

    time.sleep(5)

    allButtons = driver.find_elements(By.XPATH,'//button')
    for button in allButtons:
        try:
            if button.text == "Next":
                print("Next button press!")
                button.click()
                break
        except:
            print("pass to another element")

    time.sleep(5)

    allButtons = driver.find_elements(By.XPATH,'//button')
    for button in allButtons:
        if button.text == "Share":
            print("Share button press!")
            button.click()
            break

##    img_upload=driver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button').click()
##    #/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button
##    time.sleep(2)
##    img_upload=driver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button').click()
##    #//*[@id="mount_0_0_I/"]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/div/div/div/div[1]/div/div/div[3]/div/button
##    time.sleep(2)
##    img_upload=driver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button').click()

    #checking if video is shared
    #/html/body/div[5]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/img
    max_timeout = 90
    while max_timeout>0:
        max_timeout-=1
        time.sleep(1)
        allImages = driver.find_elements(By.XPATH,'//img')
        for image in allImages:
            if image.get_attribute('alt') == 'Animated checkmark':
                max_timeout = 0
                print("Video Uploaded!")
                break
##        if check_exists_by_xpath('/html/body/div[5]/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div/h2'):
##            print("shared success!")
##            img_upload=driver.find_element(By.XPATH,'/html/body/div[5]/div[1]/button').click()
##            max_timeout = 0

    time.sleep(3)
    #driver.close()

def uploadToTikTok():
    global driver, user_data_dir

##    options = webdriver.ChromeOptions()
##    options.add_argument("--user-data-dir={}".format(user_data_dir))
##    options.add_argument('--profile-directory=Default')
##
##    driver = webdriver.Chrome(options = options)
    driver.get("https://www.tiktok.com/upload?lang=en")

    #//*[@id="root"]/div/div/div/div/div[2]/div[1]/div/div/div[4]/button
    time.sleep(5)
    driver.switch_to.frame(0)

    max_timeout = 10
    while max_timeout>0:
        max_timeout-=1
        time.sleep(1)
        buttons = driver.find_elements(By.XPATH,'//button')
        for button in buttons:
            if button.get_attribute('class') == 'css-xqpvcy':
                print("upload button press!")
                button.click()
                max_timeout = 0
                break

    time.sleep(5)

    global path
    pyautogui.write(path)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(5)

    print("waiting for file to be uploaded!")

    max_timeout = 420
    while max_timeout>0:
        max_timeout-=1
        time.sleep(1)
        buttons = driver.find_elements(By.XPATH,'//button')
        for button in buttons:
            if button.get_attribute('class') == 'css-1ielthz':
                if button.is_enabled():
                    print("Post button press!")
                    button.click()
                    max_timeout = 0
                    time.sleep(6)
                    print("Video Posted!")
                    break

    # driver.close()

    #driver = uc.Chrome(use_subprocess=True)

    #set chromedriver.exe path
    #driver = uc.Chrome(options=options)
##    driver = webdriver.Edge()
##
##    driver.get("https://www.tiktok.com/login/phone-or-email/email")
##    time.sleep(2)
##
##    my_email=driver.find_element(By.XPATH,'//*[@id="loginContainer"]/div[1]/form/div[1]/input')
##    my_email.send_keys("imaan22000@yahoo.com")
##
##    my_password=driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div/input')
##    my_password.send_keys("ImanShabnam4411@")
##    time.sleep(2)
##
##    login=driver.find_element(By.XPATH,'//*[@id="loginContainer"]/div[1]/form/button')
##    login.click()




def uploadToFacebook():
        global driver, FacebookUser, FacebookPass, user_data_dir

##    options = webdriver.ChromeOptions()
##    options.add_argument("--user-data-dir={}".format(user_data_dir))
##    options.add_argument('--profile-directory=Default')
##
##    driver = webdriver.Chrome(options = options)
        driver.get("https://www.facebook.com/")
        time.sleep(2)

##    my_email=driver.find_element(By.XPATH,'//*[@id="email"]')
##    my_email.send_keys(FacebookUser)
##
##    my_password=driver.find_element(By.XPATH, '//*[@id="pass"]')
##    my_password.send_keys(FacebookPass)
##
##    img_upload=driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()
##    time.sleep(5)

    # max_timeout = 90
    # while max_timeout > 0:
    #     max_timeout -= 1
    #     time.sleep(1)
    #     if check_exists_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/ul/li[1]/span/div/a/span'):
    #         print("login success!")
    #         max_timeout = 0

    # if max_timeout == 0:
    #     max_timeout = 25
    #     while max_timeout > 0:
    #         max_timeout -= 1
    #         time.sleep(1)
    #         if check_exists_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/ul/li[1]/span/div/a/span'):
    #             print("Home button is visible!")
    #             max_timeout = 0

        #click home button
##        upload=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/ul/li[1]/span/div/a/span')
##        upload.click()
        print("going to mesaliquidation page")
        driver.get("https://www.facebook.com/mesaliquidation")

        #/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div/div[3]/div[1]/div[2]/div[1]/div/span/div/div/div[1]/div
        #/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/span/div/div/div[1]/div/div

        max_timeout = 90
        while max_timeout > 0:
            max_timeout -= 1
            time.sleep(1)
            allButtons = driver.find_elements(By.XPATH, '//span')
            for button in allButtons:
                #print(button.text)
                if "Create post" in button.get_attribute('textContent'):
                    button.click()
                    print("Create post button pressed!")
                    max_timeout = 0
                    break


##        #//*[@id="facebook"]/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span
##        #click post box
##        upload=driver.find_element(By.XPATH,'//*[text() = ''Create post'']')
##        upload.click()
##        time.sleep(2)

        max_timeout = 10
        while max_timeout > 0:
            max_timeout -= 1
            time.sleep(1)
            elements = driver.find_elements(By.CSS_SELECTOR, 'div[aria-label="Photo/Video"]')
            # print(len(elements))
            if len(elements):
                break
        if not max_timeout:
            print("Photo/Video button not found")
            driver.close()
            return
        
        elements[0].click()
        print("Photo/Video pressed!")
        time.sleep(5)
        
        #get file path to save page
        # n = os.path.join("C:\Users\ghs6kor\Downloads\Test", "Page.html")
        #open file in write mode with encoding
        # f = codecs.open("Page1.html", "a")
        # # #obtain page source
        # h = driver.find_elements(By.CSS_SELECTOR, 'form')
        # print(len(h))
        # # #write page source content to file
        # for hh in h:
        #     f.write(hh.get_attribute('innerHTML'))
        # driver.close()
        # return
        # for element in elements:
        #     print(element.find_elements(By.XPATH, ".//*"))
        #     for ele in element.find_elements(By.XPATH, ".//*"):
        #         print(ele.text)
        #     if "your post" in element.get_attribute("textContent"):
        #         print("find!")
        #         break
        # jsonString = element.get_attribute('innerHTML').replace("\\", "")
        # sys.stdout = open('output.txt', 'w')
        # print('"' + jsonString + '"')
        # jsonFile = open("log.html", "w")
        # jsonFile.write(str(jsonString))
        # jsonFile.close()

        # max_timeout = 120
        # while max_timeout > 0:
        #     max_timeout -= 1
        #     time.sleep(1)
        #     if check_exists_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div/div[3]/div[1]/div[2]/div[1]/div/span/div/div'):
        #         print("image/video button is visible!")
        #         max_timeout = 0

        #click image/video button
        # upload = driver.find_elements(
        #     By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div/div[3]/div[1]/div[2]/div[1]/div/span/div')
        # print(upload)
        # upload.click()
        # time.sleep(2)

# ##        #click to show file dialog
# ##        upload=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div/div')
# ##        upload.click()
# ##        time.sleep(2)

        max_timeout = 10
        while max_timeout > 0:
            max_timeout -= 1
            time.sleep(1)
            elements = driver.find_elements(
                By.CSS_SELECTOR, 'div[class="jb3vyjys dflh9lhu qt6c0cv9 scb9dxdr"] input[type="file"]')
            # print(len(elements))
            if len(elements):
                break
        if not max_timeout:
            print("Add Photo/Video button not found")
            driver.close()
            return

        elements[0].find_element(By.XPATH, '..//div[1]').click()
        print("File dialog opened!")
        time.sleep(5)

        #enetring file URL
        global path
        pyautogui.write(path)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(5)

        #checking video upload
        time.sleep(5)
        elements = driver.find_elements(
            By.CSS_SELECTOR, 'div[aria-label="Post"]')
        if len(elements):
            # print(len(elements))
            elements[0].click()
            time.sleep(10)
            print("Video is posted!")
            
        # max_timeout = 420
        # while max_timeout > 0:
        #     max_timeout -= 1
        #     time.sleep(1)
        #     # if check_exists_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div/div[3]/div[5]/div/div/div/div/div/div/div/div/span/span') == False:
        #     elements = driver.find_elements(By.CSS_SELECTOR, 'div[aria-label="Post"]')
        #     if len(elements):
        #         print(len(elements))
        #         # attrs = driver.execute_script(
        #         #     'var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', elements[0])
        #         # print(attrs)
        #         try:
        #             attr = elements[0].get_attribute('aria-disabled')
        #             print(attr)
        #             while attr and max_timeout > 0:
        #                 try:
        #                     attr = elements[0].get_attribute('aria-disabled')
        #                     max_timeout -= 1
        #                 except:
        #                     break
        #             if max_timeout > 0:
        #                 print("Video is uploaded!")
        #                 elements[0].click()
        #                 print("Video is posted!")
        #                 max_timeout = 0
        #         except:
        #             print("Video is uploaded!")
        #             elements[0].click()
        #             print("Video is posted!")
        #             max_timeout = 0
                # if max_timeout:
                #     print("Video is uploaded!")
                #     elements[0].click()
                #     print("Video is posted!")
                #     max_timeout = 0

        # time.sleep(2)
        # upload = driver.find_element(
        #     By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div/div[3]/div[3]/div')
        # upload.click()
        # print("Video is posted!")
        # time.sleep(5)

# ##        #waiting for upload to complete
# ##        print("waiting for video to post")
# ##        max_timeout = 90
# ##        while max_timeout>0:
# ##            max_timeout-=1
# ##            time.sleep(1)
# ##            if check_exists_by_xpath('//*[@id="facebook"]/body/div[4]/ul/li/div[1]/div/div[1]/span/span'):
# ##                print("Video is posted!")
# ##                max_timeout = 0

        # driver.close()

        #/li/div[1]/div/div[1]/span/span

def uploadToGoogle():

    #insert full path to your video file here
    global path
    ##FacebookUser = 'Justsendit@live.com'


    # options = webdriver.ChromeOptions()
    # options.add_argument(
    #     "--user-data-dir=C:\\Users\\justs\\AppData\\Local\\Google\\Chrome\\User Data")
    # chromedriver = "./chromedriver"
    # capabilities = webdriver.DesiredCapabilities.CHROME.copy()
    # driver = webdriver.Chrome(executable_path=chromedriver,
    #                         chrome_options=options, desired_capabilities=capabilities)

    # chrome_options = Options()
    # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--user-data-dir=C:\\Users\\justs\\AppData\\Local\\Google\\Chrome\\User Data")
    chromedriver = "./chromedriver"
    capabilities = webdriver.DesiredCapabilities.CHROME.copy()
    driver = webdriver.Chrome(executable_path=chromedriver,
                            chrome_options=chrome_options, desired_capabilities=capabilities)

    # Open a new window
    driver.execute_script("window.open('');")
    # Switch to the new window and open URL B
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://drive.google.com/drive/my-drive")
    # driver.get("https://drive.google.com/drive/my-drive")
    time.sleep(3)

    elements = driver.find_elements(
        By.CSS_SELECTOR, 'button[aria-label="New"]')
    time.sleep(3)
    # print(len(elements))
    elements[0].click()
    time.sleep(2)
    elements = driver.find_elements(
        By.CSS_SELECTOR, 'div[role="menuitem"][aria-posinset="2"]')
    time.sleep(3)
    # print(len(elements))
    elements[0].click()
    time.sleep(3)

    # global path
    pyautogui.write(path)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(8)

    #checking video upload
    elements = driver.find_elements(
        By.CSS_SELECTOR, 'div[role="dialog"][aria-label="1 upload complete"]')
    time.sleep(2)
    if len(elements):
        print("Video is posted!")
    else:
        elements = driver.find_elements(
            By.CSS_SELECTOR, 'div[role="dialog"][aria-label="Uploading 1 item"]')
        time.sleep(2)
        if len(elements):
            print("Video is posted!")


def configBrowser():
    global driver
    from pathlib import Path
    #driver_path = Path("{}/driver/chromedriver75.exe".format(PATH_TO_FOLDER))
##    path_to_profile = os.path.abspath(os.getcwd()) + '\chrome'
##    user_data_dir = Path("{}/driver/User Data".format(path_to_profile))
##    options = webdriver.ChromeOptions()
##    options.add_argument("--user-data-dir={}".format(user_data_dir))
##    options.add_argument('--profile-directory=Default')
##
##    driver = webdriver.Chrome(options = options)
    driver.get("https://www.facebook.com")
    driver.execute_script('''window.open("https://www.instagram.com", "_blank");''')
    driver.execute_script('''window.open("https://www.tiktok.com", "_blank");''')
    # driver.execute_script(
    #     '''window.open("https://drive.google.com/drive/folders/1P-qXm0wL8tqKnW3gLI1yQTsTAmQ34LjJ", "_blank");''')
    # driver.get("https://drive.google.com/drive/my-drive")

if __name__ == '__main__':
    global driver

    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir={}".format(user_data_dir))
    options.add_argument('--profile-directory=Default')
    driver = webdriver.Chrome(options = options)

    # uploadToInstagram()
    # uploadToTikTok()
    # uploadToFacebook()
    uploadToGoogle()
    
    # configBrowser()





