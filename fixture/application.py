from selenium import webdriver
from selenium.webdriver import ActionChains


from .session import SessionHelper

class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(20)
        self.session = SessionHelper(self)

    def get_home_page(self):
        wd = self.wd
        wd.get("https://hq.contactzilla.com/")


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

    def destroy(self):
        self.wd.quit()
