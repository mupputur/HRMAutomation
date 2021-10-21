from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
driver = None
def OrangeHrm_perfomance():
    global driver
    driver = webdriver.Chrome("..\\dependencies\\chromedriver.exe")
    driver.implicitly_wait(5)
    driver.get("https://opensource-demo.orangehrmlive.com/")
def log_in_page():
    act=ActionChains(driver)
    driver.find_element_by_id("txtUsername").send_keys('Admin')
    driver.find_element_by_id("txtPassword").send_keys('admin123')
    driver.find_element_by_id("btnLogin").click()
    time.sleep(5)
def Confiugre():
    act.move_to_element(driver.find_element_by_xpath('//*[@id="menu__Performance"]/b')).perform()
    time.sleep(5)
    act.move_to_element(driver.find_element_by_xpath("//*[@id='menu_performance_Configure']")).perform()
    time.sleep(5)
    res=act.move_to_element(driver.find_element_by_xpath('//*[@id="menu_performance_searchKpi"]')).click().perform()
    time.sleep(5)
    list_of_dorpdown=driver.find_element_by_xpath('//*[@id="kpi360SearchForm_jobTitleCode"]')
    list_of_items=Select(list_of_dorpdown)
    print(list_of_items)
    driver.find_element_by_id('kpi360SearchForm_jobTitleCode').click()

    d = driver.find_element_by_xpath('//*[@id="kpi360SearchForm_jobTitleCode"]/option[4]')
    d.click()

    driver.find_element_by_id("searchBtn").click()
    time.sleep(3)

    #list_of_items.select_by_index(index=5)
def Performance_icon():

    driver.find_element_by_xpath('//*[@id="menu_performance_ManageReviews"]').click()
    driver.find_element_by_id("menu_performance_searchPerformancReview").click()

    time.sleep(5)
    driver.find_element_by_id("performanceReview360SearchForm_employeeName").send_keys("Odis Adalwin")
    driver.find_element_by_xpath('//*[@id="performanceReview360SearchForm_jobTitleCode"]')
    time.sleep(2)
    driver.find_elements_by_xpath('//*[@id="performanceReview360SearchForm_jobTitleCode"]')
    s = Select(driver.find_element_by_xpath('//*[@id="performanceReview360SearchForm_jobTitleCode"]'))
    s.select_by_visible_text('Chief Financial Officer')
    driver.find_element_by_xpath('//*[@id="performanceReview360SearchForm_status"]')
    s = Select(driver.find_element_by_id('performanceReview360SearchForm_status'))
    s.select_by_visible_text("Activated")
    driver.find_element_by_xpath('//*[@id="performanceReview360SearchForm_status"]/option[3]')

    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="fromDate"]').click()
    driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[4]/td[4]/a').click()
    driver.find_element_by_xpath('//*[@id="toDate"]').click()
    driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[5]/a').click()
    driver.find_element_by_xpath('//*[@id="performanceReview360SearchForm_reviwerName"]').send_keys("good")
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click()

    # exp_year = "2021"
    # exp_month = "March"
    #
    # driver.find_element_by_xpath('//*[@id="fromDate"]').click()
    #
    # act_year = driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]').text
    # print(act_year)
    #
    # while exp_year > act_year:
    #     next_but = driver.find_element_by_xpath("//span[text()='Next']").click()
    #     act_year = driver.find_element_by_class_name("ui-datepicker-year").text
    #     print(act_year)
    #     act_month = driver.find_element_by_class_name("ui-datepicker-month").text
    #     print(act_month)
    #
    #     while exp_month > act_month:
    #         next_but = driver.find_element_by_xpath("//span[text()='Next']").click()
    #         act_month = driver.find_element_by_class_name("ui-datepicker-month").text
    #         print(act_month)
    #         break
    #
    # allDates = driver.find_elements_by_xpath("//table[@class='ui-datepicker-calendar']//td")
    # for webElement in allDates:
    #     date = webElement.text
    #
    #     if date == "14":
    #         webElement.click()
    #         break
OrangeHrm_perfomance()
log_in_page()
Confiugre()
Performance_icon()



