#! usr/bin/python3
# -*- coding: utf-8 -*-

import pytest

from data.add_group import testdata
#from data.add_group import constant as testdata



@pytest.mark.parametrize('contact', testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contact_list = app.contact.get_contact_list()
    app.contact.add(contact)
    assert len(old_contact_list) + 1 == app.contact.count()
    new_contact_list = app.contact.get_contact_list()
    old_contact_list.append(contact)
    assert sorted(old_contact_list) == sorted(new_contact_list)
