from __future__ import annotations
from typing import Any
from ticketmatic.client import Client
from ticketmatic.endpoints.settings._crud import *
from ticketmatic.models.settings import View, ViewQuery

_URL = "/{accountname}/settings/system/views"
_ITEM = "/{accountname}/settings/system/views/{id}"
ViewsList = make_list_type(View)
_FIELDS = ["typeid", "filter", "includearchived", "lastupdatesince"]


def get_list(client: Client, params=None) -> ViewsList:
    return crud_get_list(client, _URL, ViewQuery, params, ViewsList, _FIELDS)


def get(client: Client, id: int) -> View:
    return crud_get(client, _ITEM, id, View)


def create(client: Client, data) -> View:
    return crud_create(client, _URL, data, View)


def update(client: Client, id: int, data) -> View:
    return crud_update(client, _ITEM, id, data, View)


def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    return crud_translate(client, f"{_ITEM}/translate", id, data)
