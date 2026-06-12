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
from ticketmatic.models.settings import (
    CustomField,
    CustomFieldQuery,
    CustomFieldValue,
    CustomFieldValueQuery,
)

_URL = "/{accountname}/settings/system/customfields"
_ITEM = "/{accountname}/settings/system/customfields/{id}"
CustomFieldsList = make_list_type(CustomField)

_VAL_URL = "/{accountname}/settings/system/customfieldvalues"
_VAL_ITEM = "/{accountname}/settings/system/customfieldvalues/{id}"
CustomFieldValuesList = make_list_type(CustomFieldValue)
_FIELDS = ["typeid", "filter", "includearchived", "lastupdatesince"]


def get_list(client: Client, params=None) -> CustomFieldsList:
    return crud_get_list(
        client, _URL, CustomFieldQuery, params, CustomFieldsList, _FIELDS
    )


def get(client: Client, id: int) -> CustomField:
    return crud_get(client, _ITEM, id, CustomField)


def create(client: Client, data) -> CustomField:
    return crud_create(client, _URL, data, CustomField)


def update(client: Client, id: int, data) -> CustomField:
    return crud_update(client, _ITEM, id, data, CustomField)


def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    return crud_translate(client, f"{_ITEM}/translate", id, data)


# Custom field values
def values_get_list(client: Client, params=None) -> CustomFieldValuesList:
    return crud_get_list(
        client, _VAL_URL, CustomFieldValueQuery, params, CustomFieldValuesList, _FIELDS
    )


def values_get(client: Client, id: int) -> CustomFieldValue:
    return crud_get(client, _VAL_ITEM, id, CustomFieldValue)


def values_create(client: Client, data) -> CustomFieldValue:
    return crud_create(client, _VAL_URL, data, CustomFieldValue)


def values_update(client: Client, id: int, data) -> CustomFieldValue:
    return crud_update(client, _VAL_ITEM, id, data, CustomFieldValue)


def values_delete(client: Client, id: int) -> None:
    crud_delete(client, _VAL_ITEM, id)


def values_translations(client: Client, id: int) -> Any:
    return crud_translations(client, f"{_VAL_ITEM}/translate", id)


def values_translate(client: Client, id: int, data: dict) -> Any:
    return crud_translate(client, f"{_VAL_ITEM}/translate", id, data)
