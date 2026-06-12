from __future__ import annotations
from typing import Any
from ticketmatic.client import Client
from ticketmatic.endpoints.settings._crud import *
from ticketmatic.models.settings import SalesChannel, SalesChannelQuery

_URL = "/{accountname}/settings/ticketsales/saleschannels"
_ITEM = "/{accountname}/settings/ticketsales/saleschannels/{id}"
SalesChannelsList = make_list_type(SalesChannel)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(client: Client, params=None) -> SalesChannelsList:
    return crud_get_list(
        client, _URL, SalesChannelQuery, params, SalesChannelsList, _FIELDS
    )


def get(client: Client, id: int) -> SalesChannel:
    return crud_get(client, _ITEM, id, SalesChannel)


def create(client: Client, data) -> SalesChannel:
    return crud_create(client, _URL, data, SalesChannel)


def update(client: Client, id: int, data) -> SalesChannel:
    return crud_update(client, _ITEM, id, data, SalesChannel)


def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    return crud_translate(client, f"{_ITEM}/translate", id, data)
