#! usr/bin/python3
# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.contact.add(Contact(firstname='Vasya', lastname='Pupkin'))

def test_add_empty_contact(app):
    app.contact.add(Contact(firstname='', lastname=''))
