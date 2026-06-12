from __future__ import annotations
from typing import Any
from ticketmatic.client import Client
from ticketmatic.endpoints.settings._crud import *
from ticketmatic.models.settings import Report, ReportQuery

_URL = "/{accountname}/settings/system/reports"
_ITEM = "/{accountname}/settings/system/reports/{id}"
ReportsList = make_list_type(Report)
_FIELDS = ["filter", "lastupdatesince"]


def get_list(client: Client, params=None) -> ReportsList:
    return crud_get_list(client, _URL, ReportQuery, params, ReportsList, _FIELDS)


def get(client: Client, id: int) -> Report:
    return crud_get(client, _ITEM, id, Report)


def create(client: Client, data) -> Report:
    return crud_create(client, _URL, data, Report)


def update(client: Client, id: int, data) -> Report:
    return crud_update(client, _ITEM, id, data, Report)


def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    return crud_translate(client, f"{_ITEM}/translate", id, data)
