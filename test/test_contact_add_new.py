import pytest
from model.contact import Contact #create class contact in model -- OK
from fixture.application import Application


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_contact_add_new(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Mikhail", lastname="Portnov", company="Portnov Computer School", address="100 Main st, Mountain View, CA, 10151", cellphone="(670)123-4567", email="portnov@school.com", notes="Mikhail's new contact")) #create class contact in fixture to describe methods and class contact in model to describe test data
    app.session.logout()


def test_contact_add_empty(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="_", lastname="_", company="_", address="_", cellphone="_", email="_", notes="_"))  # create class contact in fixture to describe methods and class contact in model to describe test data
    app.session.logout()