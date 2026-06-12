from __future__ import annotations
from typing import Any
from ticketmatic.client import Client
from ticketmatic.endpoints.settings._crud import *
from ticketmatic.models.settings import OptIn, OptInQuery

_URL = "/{accountname}/settings/system/optins"
_ITEM = "/{accountname}/settings/system/optins/{id}"
OptInsList = make_list_type(OptIn)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(client: Client, params=None) -> OptInsList:
    return crud_get_list(client, _URL, OptInQuery, params, OptInsList, _FIELDS)


def get(client: Client, id: int) -> OptIn:
    return crud_get(client, _ITEM, id, OptIn)


def create(client: Client, data) -> OptIn:
    return crud_create(client, _URL, data, OptIn)


def update(client: Client, id: int, data) -> OptIn:
    return crud_update(client, _ITEM, id, data, OptIn)


def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    return crud_translate(client, f"{_ITEM}/translate", id, data)
