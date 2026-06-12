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
from ticketmatic.models.settings import DupeDetectRule, DupeDetectRuleQuery

_URL = "/{accountname}/settings/system/dupedetectrules"
_ITEM = "/{accountname}/settings/system/dupedetectrules/{id}"
DupeDetectRulesList = make_list_type(DupeDetectRule)
_FIELDS = ["filter", "lastupdatesince"]


def get_list(client: Client, params=None) -> DupeDetectRulesList:
    return crud_get_list(
        client, _URL, DupeDetectRuleQuery, params, DupeDetectRulesList, _FIELDS
    )


def get(client: Client, id: int) -> DupeDetectRule:
    return crud_get(client, _ITEM, id, DupeDetectRule)


def create(client: Client, data) -> DupeDetectRule:
    return crud_create(client, _URL, data, DupeDetectRule)


def update(client: Client, id: int, data) -> DupeDetectRule:
    return crud_update(client, _ITEM, id, data, DupeDetectRule)


def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)
