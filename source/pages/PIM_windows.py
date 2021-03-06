from source.pages.base_page import *
driver=launch()


def pim_config():
    driver.find_element_by_id('menu_pim_viewPimModule').click()
    driver.find_element_by_id('menu_pim_Configuration').click()
    driver.find_element_by_id('menu_pim_configurePim').click()
    driver.find_element_by_id('btnSave').click()
    driver.find_element_by_id("configPim_chkShowTax").click()
    driver.find_element_by_id('btnSave').click()
    time.sleep(5)
    
def cust_field():
    driver.find_element_by_id('menu_pim_viewPimModule').click()
    driver.find_element_by_id('menu_pim_Configuration').click()
    driver.find_element_by_id('menu_pim_listCustomFields').click()
    driver.find_element_by_id('buttonAdd').click()
    driver.find_element_by_id('customField_name').send_keys('Developer')
    drop = Select(driver.find_element_by_id('customField_screen'))
    drop.select_by_visible_text('Contact Details')
    down = Select(driver.find_element_by_id('customField_type'))
    down.select_by_visible_text('Text or Number')
    driver.find_element_by_id('btnSave').click()


def clicking_view_pim():
    driver.find_element_by_id("menu_pim_viewPimModule").click()
    driver.find_element_by_id("menu_pim_Configuration").click()
    driver.find_element_by_id("menu_pim_viewReportingMethods").click()
    driver.find_element_by_id("btnAdd").click()
    driver.find_element_by_id("reportingMethod_name").send_keys("leave")
    time.sleep(5)
    driver.find_element_by_id("btnSave").click()


def click_termination():
    driver.find_element_by_id("menu_pim_viewPimModule").click()
    driver.find_element_by_id("menu_pim_Configuration").click()
    driver.find_element_by_id("menu_pim_viewTerminationReasons").click()
    driver.find_element_by_id("btnAdd").click()
    driver.find_element_by_id("terminationReason_name").send_keys("fever")
    driver.find_element_by_id("btnSave").click()

def pim_hrm():
    driver.find_element_by_xpath("//*[@id='menu_pim_viewPimModule']").click()
    driver.find_element_by_id("menu_pim_viewEmployeeList").click()
    name = driver.find_element_by_id("empsearch_employee_name_empName")
    time.sleep(5)
    name.send_keys("Parthu")
    id = driver.find_element_by_id("empsearch_id")
    id.send_keys("143")
    supervisore = driver.find_element_by_id("empsearch_supervisor_name")
    supervisore.send_keys("Kishore")
    job_title = Select(driver.find_element_by_id("empsearch_job_title"))
    job_title.select_by_visible_text("QA Engineer")
    emp_status =Select(driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[3]/select"))
    emp_status.select_by_visible_text("Part-Time Contract")
    sub_unit = Select(driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[7]/select"))
    sub_unit.select_by_visible_text("Engineering")
    include = Select(driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[4]/select"))
    include.select_by_visible_text("Past Employees Only")
    time.sleep(5)
    click = driver.find_element_by_id("searchBtn").click()
    time.sleep(4)
    add = driver.find_element_by_id("btnAdd").click()


def navigate_pim():
    driver.find_element_by_id('menu_pim_viewPimModule').click()

def add_employee():
    driver.find_element_by_id("menu_pim_addEmployee").click()
    driver.find_element_by_id("firstName").send_keys("pushpa")
    driver.find_element_by_id("middleName").send_keys("latha")
    driver.find_element_by_id("lastName").send_keys("mannam")
    driver.find_element_by_id("employeeId ").send_keys("1234")
    driver.find_element_by_id("photofile").send_keys("C:\\Users\\pushpalatha\\Pictures\\lathdriver.jpeg")
    driver.find_element_by_id("chkLogin").click()
    driver.find_element_by_id("user_name").send_keys("srivani")
    driver.find_element_by_id("user_password").send_keys("Pshpa@4")
    driver.find_element_by_id("re_password").send_keys("Pushpa@4")
    drop = Select(driver.find_element_by_id("status"))
    drop.select_by_visible_text("Enabled")
    driver.find_element_by_id("btnSave").click()

def navigate_reports():
    driver.find_element_by_id("menu_pim_viewPimModule").click()
    time.sleep(5)
    reports = driver.find_element_by_id("menu_core_viewDefinedPredefinedReports").click()
    time.sleep(5)
def add_report():
    driver.find_element_by_name("btnAdd").click()
    time.sleep(5)
    driver.find_element_by_id("report_report_name").send_keys("Rohit Mission")
    select = Select(driver.find_element_by_id("report_criteria_list"))
    select.select_by_visible_text('Education')
    driver.find_element_by_id("btnAddConstraint").click()
    time.sleep(2)
    select2 = Select(driver.find_element_by_id("report_criteria_list"))
    select2.select_by_visible_text('Job Title')
    driver.find_element_by_id("btnAddConstraint").click()
    s = Select(driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/form/fieldset[4]/ol/li[2]/select"))
    s.select_by_visible_text("Past Employees Only")
    time.sleep(3)
    select_edu = Select(driver.find_element_by_id("report_education"))
    select_edu.select_by_visible_text("Bachelor's Degree")
    job_title = Select(driver.find_element_by_id("report_job_title"))
    job_title.select_by_visible_text("QA Engineer")
    display1 = Select(driver.find_element_by_id("report_display_groups"))
    display1.select_by_visible_text("Personal")
    driver.find_element_by_id("btnAddDisplayGroup").click()
    time.sleep(5)
    display2 = Select(driver.find_element_by_id("report_display_groups"))
    display2.select_by_visible_text("Contact Details")
    display_down = Select(driver.find_element_by_id("report_display_field_list"))
    display_down.select_by_visible_text("Mobile")
    driver.find_element_by_id("btnAddDisplayField").click()
    time.sleep(3)
    driver.find_element_by_id("display_group_1").click()
    time.sleep(2)
    driver.find_element_by_id("display_group_2").click()
    driver.find_element_by_id("btnSave").click()

#kishore
navigate_reports()

rep=add_report()
print(rep)


#priya
#pim_config()
#cust_field()


#sreekanth
#clicking_view_pim()
#click_termination()

#pardhu
#pim_hrm()


#latha
#navigate_pim()
#add_employee()
