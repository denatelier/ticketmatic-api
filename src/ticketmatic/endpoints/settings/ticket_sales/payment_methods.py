from __future__ import annotations
from typing import Any
from ticketmatic.client import Client
from ticketmatic.endpoints.settings._crud import *
from ticketmatic.models.payment import PaymentMethod, PaymentMethodQuery

_URL = "/{accountname}/settings/ticketsales/paymentmethods"
_ITEM = "/{accountname}/settings/ticketsales/paymentmethods/{id}"
PaymentMethodsList = make_list_type(PaymentMethod)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]

def get_list(client: Client, params=None) -> PaymentMethodsList:
    return crud_get_list(client, _URL, PaymentMethodQuery, params, PaymentMethodsList, _FIELDS)
def get(client: Client, id: int) -> PaymentMethod:
    return crud_get(client, _ITEM, id, PaymentMethod)
def create(client: Client, data) -> PaymentMethod:
    return crud_create(client, _URL, data, PaymentMethod)
def update(client: Client, id: int, data) -> PaymentMethod:
    return crud_update(client, _ITEM, id, data, PaymentMethod)
def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)
def translations(client: Client, id: int) -> Any:
    return crud_translations(client, f"{_ITEM}/translate", id)
def translate(client: Client, id: int, data: dict) -> Any:
    return crud_translate(client, f"{_ITEM}/translate", id, data)
