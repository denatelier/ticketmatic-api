from __future__ import annotations
from ticketmatic.client import Client
from ticketmatic.endpoints.settings._crud import *
from ticketmatic.models.contact import ContactTitle, ContactTitleQuery

_URL = "/{accountname}/settings/system/contacttitles"
_ITEM = "/{accountname}/settings/system/contacttitles/{id}"
ContactTitlesList = make_list_type(ContactTitle)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(client: Client, params=None) -> ContactTitlesList:
    return crud_get_list(
        client, _URL, ContactTitleQuery, params, ContactTitlesList, _FIELDS
    )


def get(client: Client, id: int) -> ContactTitle:
    return crud_get(client, _ITEM, id, ContactTitle)


def create(client: Client, data) -> ContactTitle:
    return crud_create(client, _URL, data, ContactTitle)


def update(client: Client, id: int, data) -> ContactTitle:
    return crud_update(client, _ITEM, id, data, ContactTitle)


def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)
