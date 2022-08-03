from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

print('Enter the gmailid and password')
gmailId = 'Oleksolo92@gmail.com'
passWord = 'Temp1234!'
try:
    driver = webdriver.Chrome()
    driver.get(r'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
    driver.implicitly_wait(15)

    loginBox = driver.find_element(By.XPATH, '//*[@id ="identifierId"]')
    loginBox.send_keys(gmailId)

    nextButton = driver.find_elements(By.XPATH, '//*[@id ="identifierNext"]')
    nextButton[0].click()

    passWordBox = driver.find_element(By.XPATH, '//*[@id ="password"]/div[1]/div / div[1]/input')
    passWordBox.send_keys(passWord)

    nextButton = driver.find_elements(By.XPATH, '//*[@id ="passwordNext"]')
    nextButton[0].click()

    print('Login Successful...!!')
    
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver = webdriver.Chrome("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
# chrome_options = Options()
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# #Change chrome driver path accordingly
# chrome_driver = "./chromedriver.exe"
# driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
# driver.get(r"https://cosmocode.io/how-to-connect-selenium-to-an-existing-browser-that-was-opened-manually/")

    # driver.execute_script(
    #     '''window.open("https://drive.google.com/drive/folders/1P-qXm0wL8tqKnW3gLI1yQTsTAmQ34LjJ", "_blank");''')


    # url = driver.command_executor._url
    # session_id = driver.session_id
    # print(session_id)

    # driver = webdriver.Remote(command_executor=url, desired_capabilities={})
    # driver.close()
    # driver.session_id = session_id

except: 
    print('Login Failed')



# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# # Optional argument, if not specified will search path.
# driver = webdriver.Chrome(
#     service=Service('C:\Program Files\Google\Chrome\Application\chrome.exe'))
# driver.get('https://drive.google.com/drive/my-drive')
# time.sleep(5)  # Let the user actually see something!
# driver.quit()

# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options


# executable_path = "path_to_webdriver"
# os.environ["webdriver.chrome.driver"] = executable_path

# chrome_options = Options()
# chrome_options.add_extension('path_to_extension')

# driver = webdriver.Chrome(
#     executable_path=executable_path, chrome_options=chrome_options)
# driver.get("http://stackoverflow.com")
# driver.quit()
