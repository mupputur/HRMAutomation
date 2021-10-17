from selenium import webdriver

from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome('dependecy/chromedriver.exe')
driver.get('https://opensource-demo.orangehrmlive.com/')
user=driver.find_element_by_id('txtUsername')
user.send_keys('Admin')
pwd=driver.find_element_by_id('txtPassword')
pwd.send_keys('admin123')
login=driver.find_element_by_name('Submit')
login.click()


driver.find_element_by_id('menu_pim_viewPimModule').click()
driver.find_element_by_id('menu_pim_Configuration').click()
#driver.find_element_by_id('menu_pim_configurePim').click()
#driver.find_element_by_id('btnSave').click()
#driver.find_element_by_id("configPim_chkShowTax").click()
#driver.find_element_by_id('btnSave').click()
driver.find_element_by_id('menu_pim_listCustomFields').click()
driver.find_element_by_id('buttonAdd').click()
driver.find_element_by_id('customField_name').send_keys('Developer')
drop=Select(driver.find_element_by_id('customField_screen'))
drop.select_by_visible_text('Contact Details')
down=Select(driver.find_element_by_id('customField_type'))
down.select_by_visible_text('Text or Number')
driver.find_element_by_id('btnSave').click()