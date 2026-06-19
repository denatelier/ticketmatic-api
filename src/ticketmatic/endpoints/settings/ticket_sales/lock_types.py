"""Endpoint functions for lock type settings."""

from __future__ import annotations

from typing import Any

from ticketmatic.client import Client
from ticketmatic.endpoints.settings._crud import (
    crud_create,
    crud_delete,
    crud_get,
    crud_get_list,
    crud_translate,
    crud_translations,
    crud_update,
    make_list_type,
)
from ticketmatic.models.seating import LockType, LockTypeQuery

_URL = "/{accountname}/settings/ticketsales/locktypes"
_ITEM = "/{accountname}/settings/ticketsales/locktypes/{id}"
LockTypesList = make_list_type(LockType)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(client: Client, params=None) -> LockTypesList:
    """Get a list of lock types.

    :param client: Ticketmatic API client.
    :param params: Optional query parameters
        (:class:`~ticketmatic.models.seating.LockTypeQuery`).
    :returns: A list of :class:`~ticketmatic.models.seating.LockType` objects.
    """
    return crud_get_list(client, _URL, LockTypeQuery, params, LockTypesList, _FIELDS)


def get(client: Client, id: int) -> LockType:
    """Get a single lock type.

    :param client: Ticketmatic API client.
    :param id: Lock type ID.
    :returns: The requested :class:`~ticketmatic.models.seating.LockType`.
    """
    return crud_get(client, _ITEM, id, LockType)


def create(client: Client, data) -> LockType:
    """Create a new lock type.

    :param client: Ticketmatic API client.
    :param data: Lock type data
        (:class:`~ticketmatic.models.seating.LockType`).
    :returns: The created :class:`~ticketmatic.models.seating.LockType`.
    """
    return crud_create(client, _URL, data, LockType)


def update(client: Client, id: int, data) -> LockType:
    """Modify an existing lock type.

    :param client: Ticketmatic API client.
    :param id: Lock type ID.
    :param data: Updated lock type data
        (:class:`~ticketmatic.models.seating.LockType`).
    :returns: The updated :class:`~ticketmatic.models.seating.LockType`.
    """
    return crud_update(client, _ITEM, id, data, LockType)


def delete(client: Client, id: int) -> None:
    """Remove a lock type.

    Lock types are archivable: this call won't actually delete the object
    from the database. Instead, it will mark the object as archived, which
    means it won't show up anymore in most places.

    :param client: Ticketmatic API client.
    :param id: Lock type ID.
    """
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    """Fetch translatable fields.

    Returns a dictionary with string values in all languages for each
    translatable field.

    :param client: Ticketmatic API client.
    :param id: Lock type ID.
    :returns: Translation strings keyed by language and field name.
    """
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    """Update translations.

    Sets updated translation strings.

    :param client: Ticketmatic API client.
    :param id: Lock type ID.
    :param data: Translation strings to update.
    :returns: Updated translation strings keyed by language and field name.
    """
    return crud_translate(client, f"{_ITEM}/translate", id, data)
