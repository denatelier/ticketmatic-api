from __future__ import annotations
from typing import Any
from ticketmatic.client import Client
from ticketmatic.endpoints.settings._crud import *
from ticketmatic.json_utils import unpack_array
from ticketmatic.models.settings import (
    FieldDefinition,
    FieldDefinitionQuery,
    FielddefinitionsDataRequest,
    FielddefinitionsDataResult,
)

_URL = "/{accountname}/settings/system/fielddefinitions"
_ITEM = "/{accountname}/settings/system/fielddefinitions/{id}"
FieldDefinitionsList = make_list_type(FieldDefinition)
_FIELDS = ["typeid", "filter", "includearchived", "lastupdatesince"]


def get_list(client: Client, params=None) -> FieldDefinitionsList:
    return crud_get_list(
        client, _URL, FieldDefinitionQuery, params, FieldDefinitionsList, _FIELDS
    )


def get(client: Client, id: int) -> FieldDefinition:
    return crud_get(client, _ITEM, id, FieldDefinition)


def create(client: Client, data) -> FieldDefinition:
    return crud_create(client, _URL, data, FieldDefinition)


def update(client: Client, id: int, data) -> FieldDefinition:
    return crud_update(client, _ITEM, id, data, FieldDefinition)


def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    return crud_translate(client, f"{_ITEM}/translate", id, data)


def get_data(
    client: Client, data: FielddefinitionsDataRequest | dict
) -> list[FielddefinitionsDataResult]:
    if isinstance(data, dict):
        data = FielddefinitionsDataRequest.from_dict(data)
    req = client.new_request("POST", f"{_URL}/data")
    req.set_body(data.to_dict())
    return unpack_array(FielddefinitionsDataResult, req.run())
