# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

success = True
wd = webdriver.Chrome()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("https://www.plaxo.com/")
    wd.find_element_by_link_text("MENU").click()
    wd.find_element_by_link_text("SIGN IN").click()
    wd.find_element_by_id("identity").click()
    wd.find_element_by_id("identity").clear()
    wd.find_element_by_id("identity").send_keys("kochynsashatest@gmail.com")
    wd.find_element_by_id("password").click()
    wd.find_element_by_id("password").clear()
    wd.find_element_by_id("password").send_keys("123456")
    wd.find_element_by_css_selector("button.plaxo-button.signin-button").click()
    wd.find_element_by_link_text("Address Book").click()
    wd.find_element_by_link_text("Add Contacts").click()

    wd.find_element_by_css_selector("div.identity").click()
    wd.find_element_by_link_text("Signout").click()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")