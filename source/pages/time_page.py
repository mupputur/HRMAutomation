from selenium import webdriver
import os
import time


def initilize_driver():
    driver_path = "..\\..\\dependencies\\chromedriver.exe"
    if not os.path.exists(driver_path):
        raise Exception("Driver is not exist : {}".format(driver_path))
    return driver_path


def launch():
    driver_path = initilize_driver()
    driver = webdriver.Chrome(executable_path=driver_path)
    time.sleep(2)
    driver.get('https://opensource-demo.orangehrmlive.com/')
    time.sleep(2)
    user = driver.find_element_by_id("txtUsername")
    time.sleep(2)
    user.send_keys("Admin")
    time.sleep(2)
    pwd = driver.find_element_by_id("txtPassword")
    time.sleep(2)
    pwd.send_keys("admin123")
    time.sleep(2)
    driver.find_element_by_id("btnLogin").click()
    driver.find_element_by_id("menu_time_viewTimeModule").click()
    driver.find_element_by_id("menu_admin_ProjectInfo").click()
    driver.find_element_by_id("menu_admin_viewCustomers").click()
    driver.find_element_by_id("ohrmList_chkSelectRecord_1").click()
    driver.find_element_by_id("btnAdd").click()
    driver.find_element_by_xpath('//*[@id="addCustomer_customerName"]').send_keys("Projectmanager6")
    driver.find_element_by_xpath('//*[@id="btnSave"]').click()
    driver.find_element_by_id("menu_admin_viewProjects").click()
    driver.find_element_by_id("menu_admin_ProjectInfo").click()
    driver.find_element_by_id("menu_admin_viewProjects").click()





launch()