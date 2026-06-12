from __future__ import annotations

from ticketmatic.client import Client
from ticketmatic.endpoints.settings._crud import *
from ticketmatic.models.pricing import TicketFee, TicketFeeQuery

_URL = "/{accountname}/settings/pricing/ticketfees"
_ITEM = "/{accountname}/settings/pricing/ticketfees/{id}"
TicketFeesList = make_list_type(TicketFee)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(
    client: Client, params: TicketFeeQuery | dict | None = None
) -> TicketFeesList:
    return crud_get_list(client, _URL, TicketFeeQuery, params, TicketFeesList, _FIELDS)


def get(client: Client, id: int) -> TicketFee:
    return crud_get(client, _ITEM, id, TicketFee)


def create(client: Client, data: TicketFee | dict) -> TicketFee:
    return crud_create(client, _URL, data, TicketFee)


def update(client: Client, id: int, data: TicketFee | dict) -> TicketFee:
    return crud_update(client, _ITEM, id, data, TicketFee)


def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)
