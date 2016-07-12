from selenium import webdriver
from selenium.webdriver import ActionChains
import unittest
from contact import Contact


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(20)

    def get_home_page(self):
        wd = self.wd
        wd.get("https://hq.contactzilla.com/")

    def login(self, username, password):
        wd = self.wd
        self.get_home_page()
        wd.find_element_by_id("Email").click()
        wd.find_element_by_id("Email").clear()
        wd.find_element_by_id("Email").send_keys(username)
        wd.find_element_by_id("Password").click()
        wd.find_element_by_id("Password").clear()
        wd.find_element_by_id("Password").send_keys(password)
        wd.find_element_by_xpath("//div[@class='text--right']/div/input").click()

    def add_contact(self, Contact):
        wd = self.wd
        self.open_add_contact_page()
        wd.find_element_by_id("givenName").click()
        wd.find_element_by_id("givenName").clear()
        wd.find_element_by_id("givenName").send_keys(Contact.firstname)
        wd.find_element_by_id("familyName").click()
        wd.find_element_by_id("familyName").clear()
        wd.find_element_by_id("familyName").send_keys(Contact.lastname)
        wd.find_element_by_css_selector("button.btn.primary").click()

    def open_add_contact_page(self):
        wd = self.wd
        wd.find_element_by_link_text("Add contact").click()

    def logout(self):
        wd = self.wd
        media_body = wd.find_element_by_class_name('media-heading')
        actions = ActionChains(wd)
        actions.move_to_element(media_body).click().perform()
        wd.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.wd.quit()
