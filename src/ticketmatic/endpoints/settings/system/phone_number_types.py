from __future__ import annotations

from typing import Any

from ticketmatic.client import Client
from ticketmatic.endpoints.settings._crud import (
    crud_create,
    crud_delete,
    crud_get,
    crud_get_list,
    crud_translate,
    crud_translations,
    crud_update,
    make_list_type,
)
from ticketmatic.models.contact import PhoneNumberType, PhoneNumberTypeQuery

_URL = "/{accountname}/settings/system/phonenumbertypes"
_ITEM = "/{accountname}/settings/system/phonenumbertypes/{id}"
PhoneNumberTypesList = make_list_type(PhoneNumberType)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(client: Client, params=None) -> PhoneNumberTypesList:
    return crud_get_list(
        client, _URL, PhoneNumberTypeQuery, params, PhoneNumberTypesList, _FIELDS
    )


def get(client: Client, id: int) -> PhoneNumberType:
    return crud_get(client, _ITEM, id, PhoneNumberType)


def create(client: Client, data) -> PhoneNumberType:
    return crud_create(client, _URL, data, PhoneNumberType)


def update(client: Client, id: int, data) -> PhoneNumberType:
    return crud_update(client, _ITEM, id, data, PhoneNumberType)


def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    return crud_translate(client, f"{_ITEM}/translate", id, data)
