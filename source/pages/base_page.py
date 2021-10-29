import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time
from selenium import webdriver

def initilize_driver():
    driver_location = "..\\..\\dependecies\\chromedriver.exe"
    if not os.path.exists(driver_location):
        raise Exception("Chrome Driver is not present : {}".format(driver_location))
    return driver_location

def launch():
    driver_path = initilize_driver()
    web_url = "https://opensource-demo.orangehrmlive.com/index.php/auth/login"
    username = 'Admin'
    Password = "admin123"
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.fin
    driver.get(web_url)
    field_User_name = driver.find_element_by_id("txtUsername")
    field_User_name.send_keys(username)
    time.sleep(5)
    field_pwd = driver.find_element_by_id("txtPassword")
    field_pwd.send_keys(Password)
    field_login = driver.find_element_by_id("btnLogin")
    field_login.click()
    return driver

if __name__ == "__main__":
    launch()

def naviagte_pim():
    pass

def naviagte_admin():
    pass