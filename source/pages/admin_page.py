from source.pages.base_page import *
import time
driver=launch()

def app_base():
    a=driver.find_element_by_id("menu_admin_viewAdminModule")
    a.click()
    a=driver.find_element_by_id("menu_admin_UserManagement")
    a.click()
    a=driver.find_element_by_id("menu_admin_viewSystemUsers")
    a.click()


def app_Organization() :

    driver.find_element_by_id("menu_admin_Organization").click()
    driver.find_element_by_id("menu_admin_viewOrganizationGeneralInformation").click()
    driver.find_element_by_id("btnSaveGenInfo").click()
    driver.find_element_by_id("organization_name").send_keys("Durgasoft")
    driver.find_element_by_id("organization_phone").send_keys("7995389708")
    #driver.find_element_by_id("organization_email").send_keys("admin@gmail.com")
    driver.find_element_by_id("organization_street1").send_keys("madhapur")
    driver.find_element_by_id("organization_city").send_keys("hyd")
    driver.find_element_by_id("organization_zipCode").send_keys("523273")
    driver.find_element_by_id("organization_note").send_keys("ntg")
    driver.find_element_by_id("organization_taxId").send_keys("ID123")
    driver.find_element_by_id("organization_registraionNumber").send_keys("148b1a0523")
    driver.find_element_by_id("organization_fax").send_keys("12345")
    driver.find_element_by_id("organization_street2").send_keys("nijampet")
    driver.find_element_by_id("organization_province").send_keys("Hyd")
    drop = Select(driver.find_element_by_id('organization_country'))
    drop.select_by_visible_text('India')
    driver.find_element_by_id("organization_province").send_keys("Hyd")
    time.sleep(3)
    driver.find_element_by_id("btnSaveGenInfo").click()
def app_locations():
    driver.find_element_by_id("menu_admin_Organization").click()
    driver.find_element_by_xpath('//*[@id="menu_admin_viewLocations"]').click()
    time.sleep(3)
    driver.find_element_by_id("searchLocation_name").send_keys("Telangana")
    driver.find_element_by_id("searchLocation_city").send_keys("hyd")
    drop = Select(driver.find_element_by_id('searchLocation_country'))
    drop.select_by_visible_text('India')
    driver.find_element_by_id("btnSearch").click()
    driver.find_element_by_id("btnAdd").click()
    driver.find_element_by_id("location_name").send_keys("Telangana")
    drop = Select(driver.find_element_by_id('location_country'))
    drop.select_by_visible_text('India')
    driver.find_element_by_id("btnSave").click()
def app_Structure():
    driver.find_element_by_id("menu_admin_Organization").click()
    driver.find_element_by_id("menu_admin_viewCompanyStructure").click()
    time.sleep(3)
    driver.find_element_by_id("btnEdit").click()
    driver.find_element_by_id("treeLink_addChild_4").click()
    driver.find_element_by_id("txtUnit_Id").send_keys("HRM001")
    driver.find_element_by_id("txtName").send_keys("HRMdevlop")
    driver.find_element_by_id("btnSave").click()
def app_nationality():
    driver.find_element_by_id("menu_admin_nationality").click()
    driver.find_element_by_id("btnAdd").click()
    driver.find_element_by_id("nationality_name").send_keys("India")
    driver.find_element_by_id("btnSave").click()

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

def navigate_admin():
    admin_button=resp.find_element_by_id("menu_admin_viewAdminModule").click()
#   resp.find_elements_by_id("menu_admin_UserManagement").click()
#   resp.find_elements_by_id("menu_admin_viewSystemUsers").click()
def user_details():
    navigate_admin()

    resp.find_element_by_name("searchSystemUser[userName]").send_keys("rajesh")
    user_roll=Select(resp.find_element_by_xpath("//*[@id='searchSystemUser_userType']"))
    user_roll.select_by_visible_text("Admin")
    resp.find_element_by_name("searchSystemUser[employeeName][empName]").send_keys("rajesh kp ")
    Select(resp.find_element_by_xpath("//*[@id='searchSystemUser_status']")).select_by_visible_text("Enabled")
    search_result=resp.find_element_by_name("_search").click()

#   return search_result
"""
recorrds_found=user_details()
if recorrds_found!=0:
    print("employee deatails matched")
else:
    add_employee_details()
"""

def add_employee_details():
    resp.find_element_by_name("btnAdd").click()
    resp.find_element_by_name("systemUser[employeeName][empName]").send_keys("Rohit@123")
    resp.find_element_by_name("systemUser[userName]").send_keys("Rohit@1234567")
    resp.find_element_by_name("systemUser[password]").send_keys("Rohit!@@#$$$$")
    resp.find_element_by_name("systemUser[confirmPassword]").send_keys("Rohit!@@#$$$$")
    resp.find_element_by_id('btnSave').click()
    time.sleep(5)
"""
def details_delete():
    resp.find_element_by_name("_reset").click()
    resp.find_element_by_name("searchSystemUser[userName]").send_keys("Rohit@12345")
    resp.find_element_by_name("_search").click()
    resp.find_element_by_xpath("//*[@id='ohrmList_chkSelectAll']").click()
    resp.find_element_by_name("btnDelete").click()
    resp.find_elements_by_id("dialogDeleteBtn")[0].click()
"""
user_details()
add_employee_details()
#details_delete()

