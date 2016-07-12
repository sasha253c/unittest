# -*- coding: utf-8 -*-

from contact import Contact
from application import Application
import pytest



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username='kochynsashatest@gmail.com', password='123456')
    app.add_contact(Contact(firstname='Vasya', lastname='Pupkin'))
    app.logout()

def test_add_empty_contact(app):
    app.get_home_page()
    app.login(username='kochynsashatest@gmail.com', password='123456')
    app.add_contact(Contact(firstname='', lastname=''))
    app.logout()
