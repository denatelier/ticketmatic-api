from __future__ import annotations

from typing import Any

from ticketmatic.client import Client
from ticketmatic.endpoints.settings._crud import *
from ticketmatic.models.pricing import PriceType, PriceTypeQuery

_URL = "/{accountname}/settings/pricing/pricetypes"
_ITEM = "/{accountname}/settings/pricing/pricetypes/{id}"
PriceTypesList = make_list_type(PriceType)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]

def get_list(client: Client, params: PriceTypeQuery | dict | None = None) -> PriceTypesList:
    return crud_get_list(client, _URL, PriceTypeQuery, params, PriceTypesList, _FIELDS)
def get(client: Client, id: int) -> PriceType:
    return crud_get(client, _ITEM, id, PriceType)
def create(client: Client, data: PriceType | dict) -> PriceType:
    return crud_create(client, _URL, data, PriceType)
def update(client: Client, id: int, data: PriceType | dict) -> PriceType:
    return crud_update(client, _ITEM, id, data, PriceType)
def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)
def translations(client: Client, id: int) -> Any:
    return crud_translations(client, f"{_ITEM}/translate", id)
def translate(client: Client, id: int, data: dict) -> Any:
    return crud_translate(client, f"{_ITEM}/translate", id, data)
