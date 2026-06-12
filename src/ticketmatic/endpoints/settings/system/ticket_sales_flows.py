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
from ticketmatic.models.order import Flowinfo, Flowsession
from ticketmatic.models.ticket import (
    Ticketsalesflow,
    TicketsalesflowQuery,
    Ticketsalessetup,
    TicketsalessetupQuery,
)

_URL = "/{accountname}/settings/system/ticketsalesflows"
_ITEM = "/{accountname}/settings/system/ticketsalesflows/{id}"
TicketsalesflowsList = make_list_type(Ticketsalesflow)
_FIELDS = ["filter", "lastupdatesince"]

_SETUP_URL = "/{accountname}/settings/system/ticketsalessetups"
_SETUP_ITEM = "/{accountname}/settings/system/ticketsalessetups/{id}"
TicketsalessetupsList = make_list_type(Ticketsalessetup)


def get_list(client: Client, params=None) -> TicketsalesflowsList:
    return crud_get_list(
        client, _URL, TicketsalesflowQuery, params, TicketsalesflowsList, _FIELDS
    )


def get(client: Client, id: int) -> Ticketsalesflow:
    return crud_get(client, _ITEM, id, Ticketsalesflow)


def create(client: Client, data) -> Ticketsalesflow:
    return crud_create(client, _URL, data, Ticketsalesflow)


def update(client: Client, id: int, data) -> Ticketsalesflow:
    return crud_update(client, _ITEM, id, data, Ticketsalesflow)


def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)


def flow_session(client: Client, id: int, data: Flowsession | dict) -> Flowinfo:
    if isinstance(data, dict):
        data = Flowsession.from_dict(data)
    req = client.new_request("POST", f"{_ITEM}/flowsession")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Flowinfo.from_dict(req.run())


def flow_info(client: Client, id: int, data: Flowsession | dict) -> Flowinfo:
    if isinstance(data, dict):
        data = Flowsession.from_dict(data)
    req = client.new_request("POST", f"{_ITEM}/flowinfo")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Flowinfo.from_dict(req.run())


# Setups
def setups_get_list(client: Client, params=None) -> TicketsalessetupsList:
    return crud_get_list(
        client,
        _SETUP_URL,
        TicketsalessetupQuery,
        params,
        TicketsalessetupsList,
        _FIELDS,
    )


def setups_get(client: Client, id: int) -> Ticketsalessetup:
    return crud_get(client, _SETUP_ITEM, id, Ticketsalessetup)


def setups_create(client: Client, data) -> Ticketsalessetup:
    return crud_create(client, _SETUP_URL, data, Ticketsalessetup)


def setups_update(client: Client, id: int, data) -> Ticketsalessetup:
    return crud_update(client, _SETUP_ITEM, id, data, Ticketsalessetup)


def setups_delete(client: Client, id: int) -> None:
    crud_delete(client, _SETUP_ITEM, id)
