#from source.pages.base_page import *
#driver = launch()
from selenium import webdriver
import os
import time
driver = None

def initilize_driver():
    global driver
    driver_location = "..\\..\\dependecies\\chromedriver.exe"
    if not os.path.exists(driver_location):
        raise Exception("Chrome Driver is not present : {}".format(driver_location))
    driver = webdriver.Chrome(executable_path=driver_location)

    time.sleep(5)
    return driver

def identify_element(locator_value, locator_type, element_name):
    try:
        if locator_type == "ID":
            element = driver.find_element_by_id(locator_value)
        elif locator_type == "XPATH":
            driver.find_element_by_xpath(locator_value)
        return element
    except Exception as e:
        print("Unable to find the elemnet :{} ERROR: {}".format(element_name, str(e)))

def click(element):
    try:
        element.click()
    except Exception as e:
        print("Unable to click the element")

def send_text(elem, text):
    try:
        elem.send_keys(text)
    except Exception as e:
        print("Unable to enter a text")