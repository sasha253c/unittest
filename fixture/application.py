from selenium import webdriver
from selenium.webdriver import ActionChains


from fixture.session import SessionHelper
from fixture.contact import ContactHelper

class Application:
    def __init__(self, browser, baseUrl):
        if browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError('Unrecognized browser %s' % browser)

        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)
        self.baseUrl = baseUrl

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def get_home_page(self):
        wd = self.wd
        wd.get(self.baseUrl)


    def destroy(self):
        self.wd.quit()
