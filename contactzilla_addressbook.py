# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver import ActionChains
import time, unittest
from contact import Contact

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class contactzilla_addressbook(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(20)

    def get_home_page(self, wd):
        wd.get("https://hq.contactzilla.com/")

    def login(self, wd, username, password):
        wd.find_element_by_id("Email").click()
        wd.find_element_by_id("Email").clear()
        wd.find_element_by_id("Email").send_keys(username)
        wd.find_element_by_id("Password").click()
        wd.find_element_by_id("Password").clear()
        wd.find_element_by_id("Password").send_keys(password)
        wd.find_element_by_xpath("//div[@class='text--right']/div/input").click()


    def add_contact(self, wd, Contact):
        wd.find_element_by_link_text("Add contact").click()
        wd.find_element_by_id("givenName").click()
        wd.find_element_by_id("givenName").clear()
        wd.find_element_by_id("givenName").send_keys(Contact.firstname)
        wd.find_element_by_id("familyName").click()
        wd.find_element_by_id("familyName").clear()
        wd.find_element_by_id("familyName").send_keys(Contact.lastname)
        wd.find_element_by_css_selector("button.btn.primary").click()

    def logout(self, wd):
        media_body = wd.find_element_by_class_name('media-heading')
        actions = ActionChains(wd)
        actions.move_to_element(media_body).click().perform()
        wd.find_element_by_link_text("Logout").click()


    def test_add_contact(self):
        wd = self.wd
        self.get_home_page(wd)
        self.login(wd, username='kochynsashatest@gmail.com', password='123456')
        self.add_contact(wd, Contact(firstname='Vasya', lastname='Pupkin'))
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.get_home_page(wd)
        self.login(wd, username='kochynsashatest@gmail.com', password='123456')
        self.add_contact(wd, Contact())
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
