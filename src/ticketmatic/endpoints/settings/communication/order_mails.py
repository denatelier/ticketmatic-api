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
from ticketmatic.models.order import OrderMailTemplate, OrderMailTemplateQuery

_URL = "/{accountname}/settings/communicationanddesign/ordermails"
_ITEM = "/{accountname}/settings/communicationanddesign/ordermails/{id}"
OrderMailsList = make_list_type(OrderMailTemplate)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(
    client: Client, params: OrderMailTemplateQuery | dict | None = None
) -> OrderMailsList:
    return crud_get_list(
        client, _URL, OrderMailTemplateQuery, params, OrderMailsList, _FIELDS
    )


def get(client: Client, id: int) -> OrderMailTemplate:
    return crud_get(client, _ITEM, id, OrderMailTemplate)


def create(client: Client, data: OrderMailTemplate | dict) -> OrderMailTemplate:
    return crud_create(client, _URL, data, OrderMailTemplate)


def update(
    client: Client, id: int, data: OrderMailTemplate | dict
) -> OrderMailTemplate:
    return crud_update(client, _ITEM, id, data, OrderMailTemplate)


def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)
