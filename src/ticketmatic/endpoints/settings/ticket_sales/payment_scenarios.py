from __future__ import annotations
from typing import Any
from ticketmatic.client import Client
from ticketmatic.endpoints.settings._crud import *
from ticketmatic.models.payment import PaymentScenario, PaymentScenarioQuery

_URL = "/{accountname}/settings/ticketsales/paymentscenarios"
_ITEM = "/{accountname}/settings/ticketsales/paymentscenarios/{id}"
PaymentScenariosList = make_list_type(PaymentScenario)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]

def get_list(client: Client, params=None) -> PaymentScenariosList:
    return crud_get_list(client, _URL, PaymentScenarioQuery, params, PaymentScenariosList, _FIELDS)
def get(client: Client, id: int) -> PaymentScenario:
    return crud_get(client, _ITEM, id, PaymentScenario)
def create(client: Client, data) -> PaymentScenario:
    return crud_create(client, _URL, data, PaymentScenario)
def update(client: Client, id: int, data) -> PaymentScenario:
    return crud_update(client, _ITEM, id, data, PaymentScenario)
def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)
def translations(client: Client, id: int) -> Any:
    return crud_translations(client, f"{_ITEM}/translate", id)
def translate(client: Client, id: int, data: dict) -> Any:
    return crud_translate(client, f"{_ITEM}/translate", id, data)
