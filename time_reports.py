from source.pages.base_page import *

driver = launch()

def project_reports():
    #Click_the_time
    driver.find_element_by_xpath('//*[@id="menu_time_viewTimeModule"]/b').click()
    #Click_the_Reports
    driver.find_element_by_xpath('//*[@id="menu_time_Reports"]').click()
    #Click_the_Criteria
    driver.find_element_by_xpath('//*[@id="menu_time_displayProjectReportCriteria"]').click()
    driver.find_element_by_xpath('//*[@id="time_project_name"]').send_keys("Internal-Recruitment")

    #click_the_from_calender
    driver.find_element_by_xpath('//*[@id="project_date_range_from_date"]').click()

    #year
    act_year = driver.find_elements_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option')
    for years in act_year:
        year = years.text
        if year == "2020":
            years.click()
            break

    #month
    act_month = driver.find_elements_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option')
    for months in act_month:
        month = months.text
        if month == "12":
            months.click()
            break

    #date
    allDates = driver.find_elements_by_xpath("//table[@class='ui-datepicker-calendar']//td")
    for dates in allDates:
        date = dates.text
        if date == "22":
            dates.click()
            break

    #click_the_to_calender
    driver.find_element_by_xpath('//*[@id="project_date_range_to_date"]').click()

    #year
    act_year = driver.find_elements_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option')
    for years in act_year:
        year = years.text
        if year == "2022":
            years.click()
            break

    #month
    act_month = driver.find_elements_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option')
    for months in act_month:
        month = months.text
        if month == "11":
            months.click()
            break

    #date
    allDates = driver.find_elements_by_xpath("//table[@class='ui-datepicker-calendar']//td")
    for dates in allDates:
        date = dates.text

        if date == "31":
            dates.click()
            break

    driver.find_element_by_xpath('//*[@id="only_include_approved_timesheets"]').click()
    driver.find_element_by_xpath('//*[@id="viewbutton"]').click()

if __name__ == "__main__":
    project_reports()


def employ_report():
    #click employ reports

    driver.find_element_by_xpath('//*[@id="menu_time_Reports"]').click()
    #click display employ reports
    driver.find_element_by_xpath('//*[@id="menu_time_displayEmployeeReportCriteria"]').click()
    #click employ name send keys
    driver.find_element_by_xpath('//*[@id="employee_empName"]').send_keys("Jasmine Morgan")
    #click project name
    driver.find_element_by_xpath('//*[@id="time_project_name"]').send_keys('Internal-Recruitment')
    #click activity
    driver.find_element_by_xpath('//*[@id="time_activity_name"]').send_keys('All')

    driver.find_element_by_xpath('//*[@id="project_date_range_from_date"]')

    #date
    driver.find_element_by_xpath('//*[@id="project_date_range_from_date"]').click()
    #year
    act_year = driver.find_elements_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option')
    for years in act_year:
        year = years.text
        if year == "2018":
            years.click()
            break


    #month
    act_month = driver.find_elements_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option')
    for months in act_month:
        month = months.text
        if month == "12":
            months.click()
            break



    #date
    allDates = driver.find_elements_by_xpath("//table[@class='ui-datepicker-calendar']//td")
    for dates in allDates:
        date = dates.text

        if date == "22":
            dates.click()
            break


    driver.find_element_by_xpath('//*[@id="project_date_range_to_date"]').click()
    #year
    act_year = driver.find_elements_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option')
    for years in act_year:
        year = years.text
        if year == "2022":
            years.click()
            break


    #month
    act_month = driver.find_elements_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option')
    for months in act_month:
        month = months.text
        if month == "12":
            months.click()
            break



    #date
    allDates = driver.find_elements_by_xpath("//table[@class='ui-datepicker-calendar']//td")
    for dates in allDates:
        date = dates.text

        if date == "22":
            dates.click()

    #click the approved time sheets
    driver.find_element_by_xpath('//*[@id="only_include_approved_timesheets"]').click()
    #click view button
    driver.find_element_by_xpath('//*[@id="viewbutton"]').click()
if __name__ == "__main__":
    employ_report()
    launch()