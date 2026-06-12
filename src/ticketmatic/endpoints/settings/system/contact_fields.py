from __future__ import annotations
from typing import Any
from ticketmatic.client import Client
from ticketmatic.endpoints.settings._crud import *
from ticketmatic.models.contact import ContactField

_URL = "/{accountname}/settings/system/contactfields"
_ITEM = "/{accountname}/settings/system/contactfields/{id}"
ContactFieldsList = make_list_type(ContactField)


def get_list(client: Client) -> ContactFieldsList:
    req = client.new_request("GET", _URL)
    return ContactFieldsList.from_dict(req.run())


def get(client: Client, id: int) -> ContactField:
    return crud_get(client, _ITEM, id, ContactField)


def translations(client: Client, id: int) -> Any:
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    return crud_translate(client, f"{_ITEM}/translate", id, data)
