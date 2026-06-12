from __future__ import annotations

from ticketmatic.client import Client
from ticketmatic.endpoints.settings._crud import (
    crud_create,
    crud_delete,
    crud_get,
    crud_get_list,
    crud_update,
    make_list_type,
)
from ticketmatic.models.pricing import PriceList, PriceListQuery

_URL = "/{accountname}/settings/pricing/pricelists"
_ITEM = "/{accountname}/settings/pricing/pricelists/{id}"
PriceListsList = make_list_type(PriceList)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(
    client: Client, params: PriceListQuery | dict | None = None
) -> PriceListsList:
    return crud_get_list(client, _URL, PriceListQuery, params, PriceListsList, _FIELDS)


def get(client: Client, id: int) -> PriceList:
    return crud_get(client, _ITEM, id, PriceList)


def create(client: Client, data: PriceList | dict) -> PriceList:
    return crud_create(client, _URL, data, PriceList)


def update(client: Client, id: int, data: PriceList | dict) -> PriceList:
    return crud_update(client, _ITEM, id, data, PriceList)


def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)
