#! usr/bin/python3
# -*- coding: utf-8 -*-

from model.contact import Contact
from sys import maxsize

def test_add_contact(app):
    old_contact_list = app.contact.get_contact_list()
    contact = Contact(firstname='Vasya', lastname='Pupkin')
    app.contact.add(contact)
    assert len(old_contact_list) + 1 == app.contact.count()
    new_contact_list = app.contact.get_contact_list()
    old_contact_list.append(contact)
    assert sorted(old_contact_list) == sorted(new_contact_list)

#def test_add_empty_contact(app):
#    old_contact_list = app.contact.get_contact_list()
#    app.contact.add(Contact(firstname='', lastname=''))
#    new_contact_list = app.contact.get_contact_list()
#    assert len(old_contact_list) == len(new_contact_list)
