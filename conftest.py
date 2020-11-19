import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("e:\\Python\\FreeAddressBookPortable\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture


