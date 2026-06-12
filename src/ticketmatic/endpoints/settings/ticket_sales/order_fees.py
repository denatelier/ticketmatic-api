from __future__ import annotations
from typing import Any
from ticketmatic.client import Client
from ticketmatic.endpoints.settings._crud import *
from ticketmatic.models.pricing import OrderFee, OrderFeeQuery

_URL = "/{accountname}/settings/ticketsales/orderfees"
_ITEM = "/{accountname}/settings/ticketsales/orderfees/{id}"
OrderFeesList = make_list_type(OrderFee)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(client: Client, params=None) -> OrderFeesList:
    return crud_get_list(client, _URL, OrderFeeQuery, params, OrderFeesList, _FIELDS)


def get(client: Client, id: int) -> OrderFee:
    return crud_get(client, _ITEM, id, OrderFee)


def create(client: Client, data) -> OrderFee:
    return crud_create(client, _URL, data, OrderFee)


def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    return crud_translate(client, f"{_ITEM}/translate", id, data)
