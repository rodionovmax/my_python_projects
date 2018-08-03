from model.contact import Contact #create class contact in model -- OK


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


def test_contact_add_new(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Mikhail", lastname="Portnov", company="Portnov Computer School", address="100 Main st, Mountain View, CA, 10151", cellphone="(670)123-4567", email="portnov@school.com")) #create class contact in fixture to describe methods and class contact in model to describe test data
    app.session.logout()


def test_contact_add_empty(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="_", lastname="_", company="_", address="_", cellphone="_", email="_"))  # create class contact in fixture to describe methods and class contact in model to describe test data
    app.session.logout()

