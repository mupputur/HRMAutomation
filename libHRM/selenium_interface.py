import os
from selenium import webdriver
import time


class SeleniumInterFace:

    def __int__(self):
        print("Hi")
        self.driver = None
        self.url = "https://www.facebook.com/"
        self.driver_location = "..\\..\\dependecies\\chromedriver.exe"
        self._initialize_driver()
        print("Hello")

    def _initialize_driver(self):
        if not os.path.exists(self.driver_location):
            raise Exception("Chrome Driver is not present : {}".format(self.driver_location))
        self.driver = webdriver.Chrome(executable_path=self.driver_location)
        self.driver.get(self.url)

    def identify_element(self, locator_value, locator_type, element_name):
        try:
            if locator_type == "ID":
                element = self.driver.find_element_by_id(locator_value)
            elif locator_type == "XPATH":
                self.driver.find_element_by_xpath(locator_value)
            return element
        except Exception as e:
            print("Unable to find the element :{} ERROR: {}".format(element_name, str(e)))

    def click(self, element):
        try:
            element.click()
        except Exception as e:
            print("Unable to click the element")

    def send_text(self, elem, text):
        try:
            elem.send_keys(text)
        except Exception as e:
            print("Unable to enter a text")


if __name__ == "__main__":
    app = SeleniumInterFace()
