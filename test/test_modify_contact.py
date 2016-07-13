from model.contact import Contact


def test_modify_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname='Susan', lastname='Ivanova'))
    app.contact.modify_first_contact(Contact(firstname='New Vasya'))

def test_modify_first_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname='Susan', lastname='Ivanova'))
    app.contact.modify_first_contact(Contact(lastname='New Pupkin'))