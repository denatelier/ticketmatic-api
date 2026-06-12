from __future__ import annotations
from typing import Any
from ticketmatic.client import Client
from ticketmatic.endpoints.settings._crud import *
from ticketmatic.models.settings import RelationType, RelationTypeQuery

_URL = "/{accountname}/settings/system/relationtypes"
_ITEM = "/{accountname}/settings/system/relationtypes/{id}"
RelationTypesList = make_list_type(RelationType)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(client: Client, params=None) -> RelationTypesList:
    return crud_get_list(
        client, _URL, RelationTypeQuery, params, RelationTypesList, _FIELDS
    )


def get(client: Client, id: int) -> RelationType:
    return crud_get(client, _ITEM, id, RelationType)


def create(client: Client, data) -> RelationType:
    return crud_create(client, _URL, data, RelationType)


def update(client: Client, id: int, data) -> RelationType:
    return crud_update(client, _ITEM, id, data, RelationType)


def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    return crud_translate(client, f"{_ITEM}/translate", id, data)
