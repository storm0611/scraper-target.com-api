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

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import pyautogui

#insert full path to your video file here
path = "D:\Pictures\DMUF9294.MP4" # your video path
FacebookUser = 'iman.omidvar@live.com'
FacebookPass = 'ImanShabnam4411'

InstagramUser = 'iman.omidvar@live.com'
InstagramPass = 'ImanShabnam4411'



def check_exists_by_xpath(xpath):
    try:
        global driver
        driver.find_element(By.XPATH, xpath)
    except:
        return False
    return True

def uploadToInstagram():
    global InstagramUser, InstagramPass, driver

    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/")
    time.sleep(2)

    my_email=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
    my_email.send_keys(InstagramUser)

    my_password=driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
    my_password.send_keys(InstagramPass)
    time.sleep(2)

    login=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]')
    login.click()
    time.sleep(5)

##    max_timeout = 30
##    while max_timeout>0:
##        max_timeout-=1
##        time.sleep(1)
##        if check_exists_by_xpath('//div[@class="QBdPU "]'):
##            print("login success!")
##            max_timeout = 0

    upload=driver.find_element(By.XPATH,'//div[@class="QBdPU "]')
    upload.click()
    time.sleep(2)
    img_upload=driver.find_elements(By.XPATH,'//button')[4].click()
    #/html/body/div[8]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button
    #/html/body/div[7]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button
    time.sleep(5)

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
                button.click()
                max_timeout = 0
                break

    time.sleep(2)

    allButtons = driver.find_elements(By.XPATH,'//button')
    for button in allButtons:
        try:
            if button.text == "Next":
                button.click()
                break
        except:
            print("pass to another element")

    time.sleep(2)

    allButtons = driver.find_elements(By.XPATH,'//button')
    for button in allButtons:
        if button.text == "Share":
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

    driver.close()

def uploadToTikTok(filePath):
    global driver

    #driver = uc.Chrome(use_subprocess=True)
    options = uc.ChromeOptions()
    options.add_argument("--user-data-dir=C:/Users/Abe/AppData/Local/Google/Chrome/User Data")
    #set chromedriver.exe path
    #driver = uc.Chrome(options=options)
    driver = webdriver.Edge()

    driver.get("https://www.tiktok.com/login/phone-or-email/email")
    time.sleep(2)

    my_email=driver.find_element(By.XPATH,'//*[@id="loginContainer"]/div[1]/form/div[1]/input')
    my_email.send_keys("imaan22000@yahoo.com")

    my_password=driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div/input')
    my_password.send_keys("ImanShabnam4411@")
    time.sleep(2)

    login=driver.find_element(By.XPATH,'//*[@id="loginContainer"]/div[1]/form/button')
    login.click()


def uploadToFacebook():
    global driver, FacebookUser, FacebookPass
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    time.sleep(2)

    my_email=driver.find_element(By.XPATH,'//*[@id="email"]')
    my_email.send_keys(FacebookUser)

    my_password=driver.find_element(By.XPATH, '//*[@id="pass"]')
    my_password.send_keys(FacebookPass)

    img_upload=driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()
    time.sleep(5)

    max_timeout = 90
    while max_timeout>0:
        max_timeout-=1
        time.sleep(1)
        if check_exists_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/ul/li[1]/span/div/a/span'):
            print("login success!")
            max_timeout = 0

    if max_timeout==0:
        max_timeout = 25
        while max_timeout>0:
            max_timeout-=1
            time.sleep(1)
            if check_exists_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/ul/li[1]/span/div/a/span'):
                print("Home button is visible!")
                max_timeout = 0

        #click home button
        upload=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/ul/li[1]/span/div/a/span')
        upload.click()
        max_timeout = 25
        while max_timeout>0:
            max_timeout-=1
            time.sleep(1)
            if check_exists_by_xpath('//*[@id="facebook"]/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span'):
                print("Post button is visible!")
                max_timeout = 0

        #click post box
        upload=driver.find_element(By.XPATH,'//*[@id="facebook"]/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span')
        upload.click()
        time.sleep(2)

        #click image/video button
        upload=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div[1]/div/span/div/div/div[1]/div')
        upload.click()
        time.sleep(2)

        #click to show file dialog
        upload=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div/div')
        upload.click()
        time.sleep(2)

        #enetring file URL
        global path
        pyautogui.write(path)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)

        #posting video
        upload=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div')
        upload.click()

        #waiting for upload to complete
        print("waiting for video to post")
        max_timeout = 90
        while max_timeout>0:
            max_timeout-=1
            time.sleep(1)
            if check_exists_by_xpath('//*[@id="facebook"]/body/div[4]/ul/li/div[1]/div/div[1]/span/span'):
                print("Video is posted!")
                max_timeout = 0


        driver.close()



        #/li/div[1]/div/div[1]/span/span


if __name__ == '__main__':
    uploadToInstagram()
    #uploadToFacebook()





