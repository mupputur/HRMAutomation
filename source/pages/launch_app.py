from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

def app_launch():
    driver = webdriver.Chrome(r"C:\\Users\\pushpalatha\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.find_element_by_id("txtUsername").send_keys('Admin')
    time.sleep(3)
    driver.find_element_by_id("txtPassword").send_keys('admin123')
    time.sleep(2)
    driver.find_element_by_name("Submit").click()
    return app_launch()
def navigate_pim():
    driver=app_launch()
    driver.find_element_by_id("menu_pim_viewPimModule").click()
def add_employee():
    driver=navigate_pim()
    driver.find_element_by_id("menu_pim_addEmployee").click()
    driver.find_element_by_id("firstName").send_keys("pushpa")
    driver.find_element_by_id("middleName").send_keys("latha")
    driver.find_element_by_id("lastName").send_keys("mannam")
    driver.find_element_by_id("employeeId ").send_keys("1234")
    driver.find_element_by_id("photofile").send_keys("C:\\Users\\pushpalatha\\Pictures\\latha.jpeg")
    driver.find_element_by_id("chkLogin").click()
    driver.find_element_by_id("user_name").send_keys("srivani")
    driver.find_element_by_id("user_password").send_keys("Pshpa@4")
    driver.find_element_by_id("re_password").send_keys("Pushpa@4")
    drop = Select(driver.find_element_by_id("status")
    drop.Select_by_visible_text("Enabled")
    driver.find_element_by_id("btnSave").click()
app_launch()
navigate_pim()
add_employee()
