from __future__ import annotations

from typing import Any

from ticketmatic.client import Client
from ticketmatic.endpoints.settings._crud import *
from ticketmatic.models.seating import SeatRank, SeatRankQuery

_URL = "/{accountname}/settings/seatingplans/seatranks"
_ITEM = "/{accountname}/settings/seatingplans/seatranks/{id}"
SeatRanksList = make_list_type(SeatRank)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(
    client: Client, params: SeatRankQuery | dict | None = None
) -> SeatRanksList:
    return crud_get_list(client, _URL, SeatRankQuery, params, SeatRanksList, _FIELDS)


def get(client: Client, id: int) -> SeatRank:
    return crud_get(client, _ITEM, id, SeatRank)


def create(client: Client, data: SeatRank | dict) -> SeatRank:
    return crud_create(client, _URL, data, SeatRank)


def update(client: Client, id: int, data: SeatRank | dict) -> SeatRank:
    return crud_update(client, _ITEM, id, data, SeatRank)


def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    return crud_translate(client, f"{_ITEM}/translate", id, data)
