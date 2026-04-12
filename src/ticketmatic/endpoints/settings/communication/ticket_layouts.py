from __future__ import annotations

from typing import Any

from ticketmatic.client import Client
from ticketmatic.endpoints.settings._crud import *
from ticketmatic.models.ticket import TicketLayout, TicketLayoutQuery, TicketLayoutTemplate, TicketLayoutTemplateQuery

_URL = "/{accountname}/settings/communicationanddesign/ticketlayouts"
_ITEM = "/{accountname}/settings/communicationanddesign/ticketlayouts/{id}"
TicketLayoutsList = make_list_type(TicketLayout)

_TPL_URL = "/{accountname}/settings/communicationanddesign/ticketlayouttemplates"
_TPL_ITEM = "/{accountname}/settings/communicationanddesign/ticketlayouttemplates/{id}"
TicketLayoutTemplatesList = make_list_type(TicketLayoutTemplate)

_FIELDS = ["typeid", "filter", "includearchived", "lastupdatesince"]

def get_list(client: Client, params: TicketLayoutQuery | dict | None = None) -> TicketLayoutsList:
    return crud_get_list(client, _URL, TicketLayoutQuery, params, TicketLayoutsList, _FIELDS)
def get(client: Client, id: int) -> TicketLayout:
    return crud_get(client, _ITEM, id, TicketLayout)
def create(client: Client, data: TicketLayout | dict) -> TicketLayout:
    return crud_create(client, _URL, data, TicketLayout)
def update(client: Client, id: int, data: TicketLayout | dict) -> TicketLayout:
    return crud_update(client, _ITEM, id, data, TicketLayout)
def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)

# Templates
def templates_get_list(client: Client, params: TicketLayoutTemplateQuery | dict | None = None) -> TicketLayoutTemplatesList:
    return crud_get_list(client, _TPL_URL, TicketLayoutTemplateQuery, params, TicketLayoutTemplatesList, _FIELDS)
def templates_get(client: Client, id: int) -> TicketLayoutTemplate:
    return crud_get(client, _TPL_ITEM, id, TicketLayoutTemplate)
def templates_create(client: Client, data: TicketLayoutTemplate | dict) -> TicketLayoutTemplate:
    return crud_create(client, _TPL_URL, data, TicketLayoutTemplate)
def templates_update(client: Client, id: int, data: TicketLayoutTemplate | dict) -> TicketLayoutTemplate:
    return crud_update(client, _TPL_ITEM, id, data, TicketLayoutTemplate)
def templates_delete(client: Client, id: int) -> None:
    crud_delete(client, _TPL_ITEM, id)
