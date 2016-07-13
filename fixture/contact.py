class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/contacts') and len(wd.find_elements_by_link_text('Add contact')) > 0):
            wd.find_element_by_link_text('Contacts').click()

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Add contact").click()

    def add(self, Contact):
        wd = self.app.wd
        self.open_contact_page()
        self.open_add_contact_page()
        self.fill_contact_form(Contact)
        wd.find_element_by_css_selector("button.btn.primary").click()
        self.return_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field('givenName', contact.firstname)
        self.change_field('familyName', contact.lastname)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_id(field_name).click()
            wd.find_element_by_id(field_name).clear()
            wd.find_element_by_id(field_name).send_keys(text)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_class_name('contact-avatar').click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        self.select_first_contact()

        #submit deletion
        wd.find_element_by_id('lnkDelete').click()
        wd.find_element_by_xpath('//div[@class="modal-footer"]/button[2]').click()
        self.return_home_page()



    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        self.select_first_contact()

        #open modification form
        wd.find_element_by_link_text('Edit contact').click()

        #fill contact form
        self.fill_contact_form(new_contact_data)

        #submit contact form
        wd.find_element_by_xpath("//div[@id='form-actions']//button[.='Save changes']").click()
        self.return_home_page()

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_id('contactzilla-logo').click()

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_class_name('check-area'))



