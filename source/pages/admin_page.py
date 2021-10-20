from source.pages.base_page import *
import time
driver = launch()


def admin():
    driver.find_element_by_id('menu_admin_viewAdminModule').click()
    driver.find_element_by_id('menu_admin_Job').click()


def job_title():
    driver.find_element_by_id('menu_admin_viewJobTitleList').click()
    driver.find_element_by_id('btnAdd').click()
    driver.find_element_by_id('jobTitle_jobTitle').send_keys('accounts')
    driver.find_element_by_id('jobTitle_jobDescription').send_keys('Automation by using python')
    driver.find_element_by_id('jobTitle_note').send_keys('i have 4 years of experiance in automation')
    driver.find_element_by_id('btnSave').click()


def pay_grade():
    driver.find_element_by_id('menu_admin_Job').click()
    driver.find_element_by_id('menu_admin_viewPayGrades').click()
    driver.find_element_by_id('btnAdd').click()
    driver.find_element_by_id('payGrade_name').send_keys('gfgc')
    driver.find_element_by_id('btnSave').click()
    driver.find_element_by_id('btnAddCurrency').click()
    driver.find_element_by_id('payGradeCurrency_currencyName').send_keys('INR - Indian Rupee')
    driver.find_element_by_id('payGradeCurrency_minSalary').send_keys('50000')
    driver.find_element_by_id('payGradeCurrency_maxSalary').send_keys('60000')
    driver.find_element_by_id('btnSaveCurrency').click()


def employment_status():
    driver.find_element_by_id('menu_admin_Job').click()
    driver.find_element_by_id('menu_admin_employmentStatus').click()
    driver.find_element_by_id('btnAdd').click()
    driver.find_element_by_id('empStatus_name').send_keys('Full_Time Contract')
    driver.find_element_by_id('btnSave').click()


def job_categories():
    driver.find_element_by_id('menu_admin_Job').click()
    driver.find_element_by_id('menu_admin_jobCategory').click()
    driver.find_element_by_id('btnAdd').click()
    driver.find_element_by_id('jobCategory_name').send_keys('Craft Workers')
    driver.find_element_by_id('btnSave').click()

def app_base():

    driver.find_element_by_id("menu_admin_viewAdminModule").click()
    driver.find_element_by_id("menu_admin_UserManagement").click()
    driver.find_element_by_id("menu_admin_viewSystemUsers").click()


def app_organization():
    app_base()

    driver.find_element_by_id("menu_admin_Organization").click()
    driver.find_element_by_id("menu_admin_viewOrganizationGeneralInformation").click()
    driver.find_element_by_id("btnSaveGenInfo").click()
    driver.find_element_by_id("organization_name").clear()
    driver.find_element_by_id("organization_name").send_keys("softtech")
    driver.find_element_by_id("organization_phone").clear()
    driver.find_element_by_id("organization_phone").send_keys("7995389708")
    driver.find_element_by_id("organization_email").clear()
    driver.find_element_by_id("organization_email").send_keys("admin@gmail.com")
    driver.find_element_by_id("organization_street1").clear()
    driver.find_element_by_id("organization_street1").send_keys("538 Teal Plaza")
    driver.find_element_by_id("organization_city").clear()
    driver.find_element_by_id("organization_city").send_keys("hyd")
    driver.find_element_by_id("organization_zipCode").clear()
    driver.find_element_by_id("organization_zipCode").send_keys("523273")
    driver.find_element_by_id("organization_note").clear()
    driver.find_element_by_id("organization_note").send_keys("ntg")
    driver.find_element_by_id("organization_taxId").clear()
    driver.find_element_by_id("organization_taxId").send_keys("ID123")
    driver.find_element_by_id("organization_registraionNumber").clear()
    driver.find_element_by_id("organization_registraionNumber").send_keys("148b1a0523")
    driver.find_element_by_id("organization_fax").clear()
    driver.find_element_by_id("organization_fax").send_keys("12345")
    driver.find_element_by_id("organization_street2").clear()
    driver.find_element_by_id("organization_street2").send_keys("nijampet")
    driver.find_element_by_id("organization_province").clear()
    driver.find_element_by_id("organization_province").send_keys("Hyd")
    drop = Select(driver.find_element_by_id('organization_country'))
    drop.select_by_visible_text('India')
    time.sleep(3)
    driver.find_element_by_id("btnSaveGenInfo").click()

def app_locations():
    app_organization()


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

def app_structure():

    app_locations()
    driver.find_element_by_id("menu_admin_Organization").click()
    driver.find_element_by_id("menu_admin_viewCompanyStructure").click()
    time.sleep(3)
    driver.find_element_by_id("btnEdit").click()
    driver.find_element_by_id("treeLink_addChild_4").click()
    driver.find_element_by_id("txtUnit_Id").send_keys("HRM001")
    driver.find_element_by_id("txtName").send_keys("HRMdevlop")
    driver.find_element_by_id("btnSave").click()

def app_nationality():

    app_structure()
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
    driver.find_element_by_id("editBtn").click()
    time.sleep(2)
    elem = driver.find_element_by_name("emailConfigurationForm[txtMailAddress]").clear()
    time.sleep(2)
    elem = driver.find_element_by_id("emailConfigurationForm_txtMailAddress")
    elem.send_keys("admin@orangehrm.com")
    elem = driver.find_element_by_id("emailConfigurationForm_cmbMailSendingMethod").click()
    sel = Select(driver.find_element_by_id("emailConfigurationForm_cmbMailSendingMethod"))
    sel.select_by_visible_text('SMTP')
    elem1 = driver.find_element_by_xpath('//*[@id="emailConfigurationForm_txtSmtpHost"]')
    time.sleep(2)
    elem1.send_keys("smtp@orangehrm.com")
    time.sleep(2)
    driver.find_element_by_id("resetBtn").click()

def email_subcrip():

    driver.find_element_by_id("menu_admin_viewAdminModule").click()
    time.sleep(2)
    driver.find_element_by_id("menu_admin_Configuration").click()
    time.sleep(2)
    driver.find_element_by_id("menu_admin_viewEmailNotification").click()
    driver.find_element_by_id("btnEdit").click()
    driver.find_element_by_id("ohrmList_chkSelectRecord_1").click()
    driver.find_element_by_id("ohrmList_chkSelectRecord_2").click()
    driver.find_element_by_id("ohrmList_chkSelectRecord_3").click()
    driver.find_element_by_id("ohrmList_chkSelectRecord_4").click()
    driver.find_element_by_id("ohrmList_chkSelectRecord_5").click()
    driver.find_element_by_id("btnSave").click()
    driver.find_element_by_xpath('// *[ @ id = "resultTable"] / tbody / tr[1] / td[1] / a').click()
    driver.find_element_by_id("btnAdd").click()
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[1]/input').send_keys("Surya")
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[2]/input').send_keys("suryateja9856@gmail.com")
    driver.find_element_by_id("btnSave").click()
    driver.find_element_by_name("chkSelectRow[]").click()
    driver.find_element_by_id("btnDelete").click()
    driver.find_element_by_id("dialogDeleteBtn").click()

def Config_nationality():

    driver.find_element_by_id("menu_admin_viewAdminModule").click()
    time.sleep(2)
    driver.find_element_by_id("menu_admin_Configuration").click()
    time.sleep(2)
    driver.find_element_by_id("menu_admin_localization").click()
    driver.find_element_by_id("btnSave").click()
    time.sleep(2)
    sel = Select(driver.find_element_by_id("localization_default_date_format"))
    time.sleep(2)
    sel.select_by_value('d-m-Y')
    driver.find_element_by_id("btnSave").click()

def Config_lan_pack():

    driver.find_element_by_id("menu_admin_viewAdminModule").click()
    time.sleep(2)
    driver.find_element_by_id("menu_admin_Configuration").click()
    time.sleep(2)
    driver.find_element_by_id("menu_admin_languagePackage").click()
    driver.find_element_by_id("btnAdd").click()
    time.sleep(2)
    sel = Select(driver.find_element_by_id("addLanguagePackage_name"))
    sel.select_by_value('en_GB')
    driver.find_element_by_id("btnSave").click()

def Config_modules():

    driver.find_element_by_id("menu_admin_viewAdminModule").click()
    time.sleep(2)
    driver.find_element_by_id("menu_admin_Configuration").click()
    time.sleep(2)
    driver.find_element_by_id("menu_admin_viewModules").click()
    time.sleep(2)
    driver.find_element_by_id("btnSave").click()
    driver.find_element_by_id("moduleConfig_leave").click()
    driver.find_element_by_id("moduleConfig_time").click()
    driver.find_element_by_id("moduleConfig_recruitment").click()
    driver.find_element_by_id("moduleConfig_performance").click()
    driver.find_element_by_id("moduleConfig_directory").click()
    driver.find_element_by_id("moduleConfig_maintenance").click()
    driver.find_element_by_id("moduleConfig_mobile").click()
    driver.find_element_by_id("btnSave").click()


# admin() #anitha code
# job_title()
# pay_grade()
# employment_status()
# job_categories()

# app_base() #deepika code
# app_Organization()
# app_locations()
# app_Structure()
# app_nationality()

# config() #surya code
# email_subcrip()
# Config_nationality()
# Config_lan_pack()
# Config_modules()



