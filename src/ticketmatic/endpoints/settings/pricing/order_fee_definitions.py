from __future__ import annotations

from typing import Any

from ticketmatic.client import Client
from ticketmatic.endpoints.settings._crud import *
from ticketmatic.models.pricing import OrderFeeDefinition, OrderFeeDefinitionQuery

_URL = "/{accountname}/settings/pricing/orderfeedefinitions"
_ITEM = "/{accountname}/settings/pricing/orderfeedefinitions/{id}"
OrderFeeDefinitionsList = make_list_type(OrderFeeDefinition)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]

def get_list(client: Client, params: OrderFeeDefinitionQuery | dict | None = None) -> OrderFeeDefinitionsList:
    return crud_get_list(client, _URL, OrderFeeDefinitionQuery, params, OrderFeeDefinitionsList, _FIELDS)
def get(client: Client, id: int) -> OrderFeeDefinition:
    return crud_get(client, _ITEM, id, OrderFeeDefinition)
def create(client: Client, data: OrderFeeDefinition | dict) -> OrderFeeDefinition:
    return crud_create(client, _URL, data, OrderFeeDefinition)
def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)
def translations(client: Client, id: int) -> Any:
    return crud_translations(client, f"{_ITEM}/translate", id)
def translate(client: Client, id: int, data: dict) -> Any:
    return crud_translate(client, f"{_ITEM}/translate", id, data)
