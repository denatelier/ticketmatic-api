from __future__ import annotations
from typing import Any
from ticketmatic.client import Client
from ticketmatic.endpoints.settings._crud import *
from ticketmatic.models.settings import FilterDefinition, FilterDefinitionQuery

_URL = "/{accountname}/settings/system/filterdefinitions"
_ITEM = "/{accountname}/settings/system/filterdefinitions/{id}"
FilterDefinitionsList = make_list_type(FilterDefinition)
_FIELDS = ["typeid", "filter", "includearchived", "lastupdatesince"]


def get_list(client: Client, params=None) -> FilterDefinitionsList:
    return crud_get_list(
        client, _URL, FilterDefinitionQuery, params, FilterDefinitionsList, _FIELDS
    )


def get(client: Client, id: int) -> FilterDefinition:
    return crud_get(client, _ITEM, id, FilterDefinition)


def create(client: Client, data) -> FilterDefinition:
    return crud_create(client, _URL, data, FilterDefinition)


def update(client: Client, id: int, data) -> FilterDefinition:
    return crud_update(client, _ITEM, id, data, FilterDefinition)


def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    return crud_translate(client, f"{_ITEM}/translate", id, data)
