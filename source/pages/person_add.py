from selenium import webdriver
from time import sleep
def login_func():
    driver = webdriver.Chrome("C:\\Users\\sreekan\\Downloads\\chromedriver_win32 (2)\\chromedriver")
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()


    return driver
a=login_func()


# def clicking_view_pim():
#     a.find_element_by_id("menu_pim_viewPimModule").click()
#     a.find_element_by_id("menu_pim_Configuration").click()
#     a.find_element_by_id("menu_pim_viewReportingMethods").click()
#     a.find_element_by_id("btnAdd").click()
#     a.find_element_by_id("reportingMethod_name").send_keys("leave")
#     sleep(5)
#     a.find_element_by_id("btnSave").click()
#     a.find_element_by_class_name("checkbox").click()
#     sleep(5)
#     a.find_element_by_id("btnDel").click()
#
# clicking_view_pim()

def click_termination():
    a.find_element_by_id("menu_pim_viewPimModule").click()
    a.find_element_by_id("menu_pim_Configuration").click()
    a.find_element_by_id("menu_pim_viewTerminationReasons").click()
    a.find_element_by_id("btnAdd").click()
    a.find_element_by_id("terminationReason[name]").send_keys("faver")
    a.find_element_by_id("btnSave").click()

click_termination()