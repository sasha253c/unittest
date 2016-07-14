class Contact():
    def __init__(self, firstname=None, lastname=None):
        self.firstname = firstname
        self.lastname = lastname

        if firstname is None: firstname = ''
        if lastname is None: lastname = ''
        self.id = firstname.rjust(20, '_') + lastname.rjust(20, '_')

    def __repr__(self):
        return '%s' % (self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __gt__(self, other):
        return self.id > other.id