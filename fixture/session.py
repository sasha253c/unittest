from selenium.webdriver import ActionChains

class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.get_home_page()
        wd.find_element_by_id("Email").click()
        wd.find_element_by_id("Email").clear()
        wd.find_element_by_id("Email").send_keys(username)
        wd.find_element_by_id("Password").click()
        wd.find_element_by_id("Password").clear()
        wd.find_element_by_id("Password").send_keys(password)
        wd.find_element_by_xpath("//div[@class='text--right']/div/input").click()

    def logout(self):
        wd = self.app.wd
        media_body = wd.find_element_by_class_name('media-heading')
        actions = ActionChains(wd)
        actions.move_to_element(media_body).click().perform()
        wd.find_element_by_link_text("Logout").click()

