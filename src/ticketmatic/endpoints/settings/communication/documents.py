from __future__ import annotations

from typing import Any

from ticketmatic.client import Client
from ticketmatic.endpoints.settings._crud import *
from ticketmatic.models.settings import Document, DocumentQuery

_URL = "/{accountname}/settings/communicationanddesign/documents"
_ITEM = "/{accountname}/settings/communicationanddesign/documents/{id}"
DocumentsList = make_list_type(Document)
_FIELDS = ["typeid", "filter", "lastupdatesince"]

def get_list(client: Client, params: DocumentQuery | dict | None = None) -> DocumentsList:
    return crud_get_list(client, _URL, DocumentQuery, params, DocumentsList, _FIELDS)
def get(client: Client, id: int) -> Document:
    return crud_get(client, _ITEM, id, Document)
def create(client: Client, data: Document | dict) -> Document:
    return crud_create(client, _URL, data, Document)
def update(client: Client, id: int, data: Document | dict) -> Document:
    return crud_update(client, _ITEM, id, data, Document)
def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)
def translations(client: Client, id: int) -> Any:
    return crud_translations(client, f"{_ITEM}/translate", id)
def translate(client: Client, id: int, data: dict) -> Any:
    return crud_translate(client, f"{_ITEM}/translate", id, data)
