from model.contact import Contact


def test_modify_first_contact_firstname(app):
    app.session.login(username='kochynsashatest@gmail.com', password='123456')
    app.contact.modify_first_contact(Contact(firstname='New Vasya'))
    app.session.logout()

def test_modify_first_contact_lastname(app):
    app.session.login(username='kochynsashatest@gmail.com', password='123456')
    app.contact.modify_first_contact(Contact(lastname='New Pupkin'))
    app.session.logout()