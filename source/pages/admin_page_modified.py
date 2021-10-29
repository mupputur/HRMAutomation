from libHRM.selenium_helper import *
from admin_page_locators import *

def navigate_configuration():
    elem = identify_element(ADMIN_CONF_TAB_ID[1],ADMIN_CONF_TAB_ID[0], "Configuration")
    click(elem)

def navigate_email_list():
    pass

def naviagte_email_subscriptions():
    pass

def naviagte_localization():
    pass