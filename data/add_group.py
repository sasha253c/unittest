# -*- coding: utf-8 -*-

from model.contact import Contact
import random
import string


constant = [
    Contact(firstname='firstname1', lastname='lastname1'),
    Contact(firstname='firstname2', lastname='lastname2'),

]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=firstname, lastname=lastname)
    for firstname in ['f', random_string('firstname', 10)]
    for lastname in ['l', random_string('lastname', 10)]
]