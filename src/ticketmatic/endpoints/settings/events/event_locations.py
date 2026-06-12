from __future__ import annotations

from typing import Any

from ticketmatic.client import Client
from ticketmatic.endpoints.settings._crud import *
from ticketmatic.models.event import EventLocation, EventLocationQuery

_URL = "/{accountname}/settings/events/eventlocations"
_ITEM = "/{accountname}/settings/events/eventlocations/{id}"
EventLocationsList = make_list_type(EventLocation)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(
    client: Client, params: EventLocationQuery | dict | None = None
) -> EventLocationsList:
    return crud_get_list(
        client, _URL, EventLocationQuery, params, EventLocationsList, _FIELDS
    )


def get(client: Client, id: int) -> EventLocation:
    return crud_get(client, _ITEM, id, EventLocation)


def create(client: Client, data: EventLocation | dict) -> EventLocation:
    return crud_create(client, _URL, data, EventLocation)


def update(client: Client, id: int, data: EventLocation | dict) -> EventLocation:
    return crud_update(client, _ITEM, id, data, EventLocation)


def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    return crud_translate(client, f"{_ITEM}/translate", id, data)
