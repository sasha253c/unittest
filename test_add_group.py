# -*- coding: utf-8 -*-

from selenium import webdriver


import time, unittest


class TestAddressBook(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        #self.wd = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs')
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        wd.get("https://www.plaxo.com/")

    def login(self, wd, username, password):
        wd.find_element_by_class_name('toggleHeaderMenu').click()
        wd.find_element_by_link_text("SIGN IN").click()
        wd.find_element_by_id("identity").click()
        wd.find_element_by_id("identity").clear()
        wd.find_element_by_id("identity").send_keys(username)
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys(password)
        wd.find_element_by_css_selector("button.plaxo-button.signin-button").click()

    def logout(self, wd):
        wd.find_element_by_class_name("identity").click()
        wd.find_element_by_link_text("Signout").click()

    def add_contact(self, wd):
        wd.find_element_by_link_text('Address Book').click()
        wd.find_element_by_link_text('Add Contacts').click()







    def test_test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username='kochynsashatest@gmail.com', password='123456')
        self.add_contact(wd)
        self.logout(wd)


    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
