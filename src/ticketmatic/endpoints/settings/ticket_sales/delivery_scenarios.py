from __future__ import annotations
from typing import Any
from ticketmatic.client import Client
from ticketmatic.endpoints.settings._crud import *
from ticketmatic.models.settings import DeliveryScenario, DeliveryScenarioQuery

_URL = "/{accountname}/settings/ticketsales/deliveryscenarios"
_ITEM = "/{accountname}/settings/ticketsales/deliveryscenarios/{id}"
DeliveryScenariosList = make_list_type(DeliveryScenario)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(client: Client, params=None) -> DeliveryScenariosList:
    return crud_get_list(
        client, _URL, DeliveryScenarioQuery, params, DeliveryScenariosList, _FIELDS
    )


def get(client: Client, id: int) -> DeliveryScenario:
    return crud_get(client, _ITEM, id, DeliveryScenario)


def create(client: Client, data) -> DeliveryScenario:
    return crud_create(client, _URL, data, DeliveryScenario)


def update(client: Client, id: int, data) -> DeliveryScenario:
    return crud_update(client, _ITEM, id, data, DeliveryScenario)


def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    return crud_translate(client, f"{_ITEM}/translate", id, data)
