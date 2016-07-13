#! usr/bin/python3
# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.session.login(username='kochynsashatest@gmail.com', password='123456')
    app.contact.add(Contact(firstname='Vasya', lastname='Pupkin'))
    app.session.logout()

def test_add_empty_contact(app):
    app.get_home_page()
    app.session.login(username='kochynsashatest@gmail.com', password='123456')
    app.contact.add(Contact(firstname='', lastname=''))
    app.session.logout()
