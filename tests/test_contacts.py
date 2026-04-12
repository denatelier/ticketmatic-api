import pytest

from ticketmatic.endpoints import contacts
from ticketmatic.endpoints.settings.system import contact_address_types, contact_titles, phone_number_types
from ticketmatic.models.contact import ContactGetQuery, ContactQuery

pytestmark = pytest.mark.integration


def test_get(tm_client):
    result = contacts.get_list(tm_client)
    assert len(result.data) > 0

    contact = contacts.get(tm_client, result.data[0].id)
    assert contact.id == result.data[0].id


def test_batch(tm_client):
    c1 = contacts.create(tm_client, {"firstname": "John"})
    assert c1.id != 0
    assert c1.firstname == "John"

    c2 = contacts.create(tm_client, {"firstname": "Bob"})
    assert c2.id != 0

    contacts.batch(tm_client, {
        "ids": [c1.id],
        "operation": "update",
        "parameters": {"fields": {"languagecode": "EN"}},
    })


def test_create(tm_client):
    contact = contacts.create(tm_client, {"firstname": "John"})
    assert contact.id != 0
    assert contact.firstname == "John"

    updated = contacts.update(tm_client, contact.id, {"lastname": "Doe"})
    assert updated.id == contact.id
    assert updated.firstname == "John"
    assert updated.lastname == "Doe"

    contacts.delete(tm_client, contact.id)


def test_create_custom(tm_client):
    titles = contact_titles.get_list(tm_client)
    assert len(titles.data) > 0

    addrtypes = contact_address_types.get_list(tm_client)
    assert len(addrtypes.data) > 0

    ptypes = phone_number_types.get_list(tm_client)
    assert len(ptypes.data) > 1

    contact = contacts.create(tm_client, {
        "addresses": [{
            "city": "Nieuwerkerk Aan Den Ijssel",
            "countrycode": "NL",
            "street1": "Kerkstraat",
            "street2": "1",
            "typeid": addrtypes.data[0].id,
            "zip": "2914 AH",
        }],
        "birthdate": "1959-09-21",
        "customertitleid": titles.data[0].id,
        "email": "john@worldonline.nl",
        "firstname": "John",
        "lastname": "Johns",
        "middlename": "J",
        "phonenumbers": [
            {"number": "+31222222222", "typeid": ptypes.data[0].id},
            {"number": "+31222222222", "typeid": ptypes.data[1].id},
        ],
    })

    assert contact.id != 0
    assert contact.firstname == "John"
    assert contact.addresses[0].countrycode == "NL"
    assert contact.addresses[0].country == "Netherlands"

    contacts.delete(tm_client, contact.id)


def test_create_unicode(tm_client):
    contact = contacts.create(tm_client, {
        "email": "john@test.com",
        "firstname": "JØhñ",
        "lastname": "ポテト 👌 ไก่",
    })
    assert contact.id != 0
    assert contact.firstname == "JØhñ"
    assert contact.lastname == "ポテト 👌 ไก่"

    contact2 = contacts.get(tm_client, contact.id)
    assert contact2.firstname == "JØhñ"
    assert contact2.lastname == "ポテト 👌 ไก่"

    contact3 = contacts.get(tm_client, 0, ContactGetQuery(email="john@test.com"))
    assert contact3.id != 0

    contacts.delete(tm_client, contact.id)


def test_archived(tm_client):
    contact = contacts.create(tm_client, {"firstname": "John"})
    assert contact.id != 0

    req = contacts.get_list(tm_client, ContactQuery(includearchived=True))
    assert len(req.data) > 0

    contacts.delete(tm_client, contact.id)

    req2 = contacts.get_list(tm_client)
    assert len(req.data) > len(req2.data)

    req3 = contacts.get_list(tm_client, ContactQuery(includearchived=True))
    assert len(req3.data) == len(req.data)


def test_import(tm_client):
    result = contacts.import_contacts(tm_client, [
        {"firstname": "Test", "lastname": "Mc Cheer"},
        {"email": "invalid", "firstname": "Last"},
    ])
    assert result[0].ok is True
    assert result[1].ok is False
    assert result[0].id > 0
    assert result[1].error == "Invalid email"

    contacts.delete(tm_client, result[0].id)


def test_update_with_optins(tm_client):
    contact = contacts.create(tm_client, {"email": "john34@test.com", "firstname": "John"})
    assert contact.id != 0
    assert contact.email == "john34@test.com"
    assert len(contact.optins) == 0

    updated = contacts.update(tm_client, contact.id, {
        "optins": [{
            "info": {"method": "api", "remarks": "remarks"},
            "optinid": 1,
            "status": 7602,
        }],
    })
    assert updated.id == contact.id
    assert len(updated.optins) == 1
    assert updated.optins[0].optinid == 1
    assert updated.optins[0].status == 7602
    assert updated.optins[0].info.method == "api"
    assert updated.optins[0].info.remarks == "remarks"


def test_remarks(tm_client):
    contact = contacts.create(tm_client, {"firstname": "John"})
    assert contact.id != 0

    remark = contacts.create_remark(tm_client, contact.id, {"content": "Hello World"})
    assert remark.id != 0
    assert remark.content == "Hello World"
    assert remark.pinned is False

    updated = contacts.update_remark(tm_client, contact.id, remark.id, {
        "content": "Hello World 2",
        "pinned": True,
    })
    assert updated.content == "Hello World 2"
    assert updated.pinned is True

    fetched = contacts.get_remark(tm_client, contact.id, remark.id)
    assert fetched.id == remark.id
    assert fetched.content == "Hello World 2"
    assert fetched.pinned is True

    contacts.delete_remark(tm_client, contact.id, remark.id)
