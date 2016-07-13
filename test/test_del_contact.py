def test_delete_first_contact(app):
    app.session.login(username='kochynsashatest@gmail.com', password='123456')
    app.contact.delete_first_contact()
    app.session.logout()
