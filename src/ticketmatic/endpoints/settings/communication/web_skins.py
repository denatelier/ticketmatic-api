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
from ticketmatic.models.ticket import WebSalesSkin, WebSalesSkinQuery

_URL = "/{accountname}/settings/communicationanddesign/webskins"
_ITEM = "/{accountname}/settings/communicationanddesign/webskins/{id}"
WebSkinsList = make_list_type(WebSalesSkin)
_FIELDS = ["filter", "lastupdatesince"]


def get_list(
    client: Client, params: WebSalesSkinQuery | dict | None = None
) -> WebSkinsList:
    return crud_get_list(client, _URL, WebSalesSkinQuery, params, WebSkinsList, _FIELDS)


def get(client: Client, id: int) -> WebSalesSkin:
    return crud_get(client, _ITEM, id, WebSalesSkin)


def create(client: Client, data: WebSalesSkin | dict) -> WebSalesSkin:
    return crud_create(client, _URL, data, WebSalesSkin)


def update(client: Client, id: int, data: WebSalesSkin | dict) -> WebSalesSkin:
    return crud_update(client, _ITEM, id, data, WebSalesSkin)


def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)
