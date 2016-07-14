from model.contact import Contact
from random import randrange

def test_modify_contact_firstname_by_index(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname='Susan', lastname='Ivanova'))

    old_contact_list = app.contact.get_contact_list()
    index = randrange(len(old_contact_list))

    new_firstname = 'Petro'
    contact = Contact(firstname=new_firstname)
    contact.id = new_firstname.rjust(20, '_') + old_contact_list[index].id[20:]

    app.contact.modify_contact_by_index(contact, index)
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) == len(new_contact_list)

    old_contact_list[index] = contact
    assert sorted(old_contact_list) == sorted(new_contact_list)

#def test_modify_first_contact_lastname(app):
#    if app.contact.count() == 0:
#        app.contact.add(Contact(firstname='Susan', lastname='Ivanova'))

#    old_contact_list = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(lastname='Pupkin2'))
#    new_contact_list = app.contact.get_contact_list()
#    assert len(old_contact_list) == len(new_contact_list)