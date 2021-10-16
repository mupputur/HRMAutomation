from source.pages.base_page import *
import time
driver=launch()
def config():
    driver.find_element_by_id("menu_admin_viewAdminModule").click()
    time.sleep(2)
    driver.find_element_by_id("menu_admin_Configuration").click()
    time.sleep(2)
    driver.find_element_by_id("menu_admin_listMailConfiguration").click()
    time.sleep(2)
    driver.find_element_by_id("editBtn").click()
    time.sleep(2)
    elem = driver.find_element_by_name("emailConfigurationForm[txtMailAddress]").clear()
    time.sleep(2)
    elem = driver.find_element_by_id("emailConfigurationForm_txtMailAddress")
    elem.send_keys("admin@orangehrm.com")
    sel = Select(driver.find_element_by_id("emailConfigurationForm_cmbMailSendingMethod"))
    sel.select_by_visible_text('Sendmail')
    elem = driver.find_element_by_id("emailConfigurationForm_chkSendTestEmail").click()
    elem = driver.find_element_by_id("emailConfigurationForm_txtTestEmail")
    elem.send_keys("suryateja9856@gmail.com")
    elem = driver.find_element_by_id("editBtn").click()
    #elem = driver.find_element_by_id("resetBtn").click()>
    driver.find_element_by_id("editBtn").click()
    time.sleep(2)
    elem = driver.find_element_by_name("emailConfigurationForm[txtMailAddress]").clear()
    time.sleep(2)
    elem = driver.find_element_by_id("emailConfigurationForm_txtMailAddress")
    elem.send_keys("admin@orangehrm.com")
    elem = driver.find_element_by_id("emailConfigurationForm_cmbMailSendingMethod").click()
    sel= Select(driver.find_element_by_id("emailConfigurationForm_cmbMailSendingMethod"))
    sel.select_by_visible_text('SMTP')
    elem1 = driver.find_element_by_xpath('//*[@id="emailConfigurationForm_txtSmtpHost"]')
    time.sleep(2)
    elem1.send_keys("smtp@orangehrm.com")
    time.sleep(2)
    driver.find_element_by_id("resetBtn").click()

config()

    # elem = driver.find_element_by_id("emailConfigurationForm_chkSendTestEmail").click()
    # elem = driver.find_element_by_id("emailConfigurationForm_txtTestEmail")
    # elem.send_keys("suryateja9856@gmail.com")
    # elem = driver.find_element_by_id("editBtn").click()







# elem = Select(driver.find_element_by_id("emailConfigurationForm[cmbMailSendingMethod]"))
# elem.select_by_visible_text('Sendmail')
# sel= Select(driver.find_element_by_id("emailConfigurationForm[cmbMailSendingMethod]"))
# sel.select_by_index(0)
# elem=driver.find_element_by_id("emailConfigurationForm_chkSendTestEmail").click()