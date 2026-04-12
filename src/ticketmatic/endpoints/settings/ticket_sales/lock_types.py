from __future__ import annotations
from typing import Any
from ticketmatic.client import Client
from ticketmatic.endpoints.settings._crud import *
from ticketmatic.models.seating import LockType, LockTypeQuery

_URL = "/{accountname}/settings/ticketsales/locktypes"
_ITEM = "/{accountname}/settings/ticketsales/locktypes/{id}"
LockTypesList = make_list_type(LockType)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]

def get_list(client: Client, params=None) -> LockTypesList:
    return crud_get_list(client, _URL, LockTypeQuery, params, LockTypesList, _FIELDS)
def get(client: Client, id: int) -> LockType:
    return crud_get(client, _ITEM, id, LockType)
def create(client: Client, data) -> LockType:
    return crud_create(client, _URL, data, LockType)
def update(client: Client, id: int, data) -> LockType:
    return crud_update(client, _ITEM, id, data, LockType)
def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)
def translations(client: Client, id: int) -> Any:
    return crud_translations(client, f"{_ITEM}/translate", id)
def translate(client: Client, id: int, data: dict) -> Any:
    return crud_translate(client, f"{_ITEM}/translate", id, data)
