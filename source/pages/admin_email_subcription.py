from source.pages.base_page import *
import time
driver=launch()
def config():
    driver.find_element_by_id("menu_admin_viewAdminModule").click()
    time.sleep(2)
    driver.find_element_by_id("menu_admin_Configuration").click()
    time.sleep(2)
    driver.find_element_by_id("menu_admin_viewEmailNotification").click()
    elem = driver.find_element_by_xpath('//*[@id="emailConfigurationForm_txtSmtpHost"]').click()

    #driver.find_element_by_id("btnEdit").click()

config()