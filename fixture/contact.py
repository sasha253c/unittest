import time

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Add contact").click()

    def add(self, Contact):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_id("givenName").click()
        wd.find_element_by_id("givenName").clear()
        wd.find_element_by_id("givenName").send_keys(Contact.firstname)
        wd.find_element_by_id("familyName").click()
        wd.find_element_by_id("familyName").clear()
        wd.find_element_by_id("familyName").send_keys(Contact.lastname)
        wd.find_element_by_css_selector("button.btn.primary").click()

    def delete_first_contact(self):
        wd = self.app.wd

        #select first contact
        wd.find_element_by_class_name('check-area').click()
        time.sleep(1)


        #submit deletion
        wd.find_element_by_link_text('Delete').click()

        wd.find_element_by_xpath('//div[@class="modal-footer"]/button[2]').click()

