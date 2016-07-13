from selenium import webdriver
from selenium.webdriver import ActionChains


from fixture.session import SessionHelper
from fixture.contact import ContactHelper

class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def get_home_page(self):
        wd = self.wd
        wd.get("https://hq.contactzilla.com/")


    def destroy(self):
        self.wd.quit()
