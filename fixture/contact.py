

class ContactHelper:
    def __init__(self,app):
        self.app = app

    def add_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        #init contact creation
        self.add_new_contact_page()
        self.fill_contact_form(contact)
        #submit form
        wd.find_element_by_name("submit").click()
        self.return_to_contact_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        wd.change_field_value("firstname", contact.firstname)
        wd.change_field_value("lastname", contact.lastname)
        wd.change_field_value("company", contact.company)
        wd.change_field_value("address", contact.address)
        wd.change_field_value("mobile", contact.mobile)
        wd.change_field_value("email", contact.email)


        #wd.find_element_by_name("lastname").click()
        #wd.find_element_by_name("lastname").clear()
        #wd.find_element_by_name("lastname").send_keys(contact.lastname)
        #wd.find_element_by_name("company").click()
        #wd.find_element_by_name("company").clear()
        #wd.find_element_by_name("company").send_keys(contact.company)
        #wd.find_element_by_name("address").click()
        #wd.find_element_by_name("address").clear()
        #wd.find_element_by_name("address").send_keys(contact.address)
        #wd.find_element_by_name("mobile").click()
        #wd.find_element_by_name("mobile").clear()
        #wd.find_element_by_name("mobile").send_keys(contact.cellphone)
        #wd.find_element_by_name("email").click()
        #wd.find_element_by_name("email").clear()
        #wd.find_element_by_name("email").send_keys(contact.email)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        self.click_edit_contact_pic()
        self.click_delete_button()
        self.return_to_contact_page()

    def click_delete_button(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#content > form:nth-child(3) > input:nth-child(2)").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        #self.open_groups_page()
        self.select_first_contact()
        #open modificaion form
        self.click_edit_contact_pic()
        #fill out form
        self.fill_contact_form(new_contact_data)
        #submit modification
        wd.find_element_by_name("update").click()
        self.return_to_contact_page()

    def click_edit_contact_pic(self):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()

    def open_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()


