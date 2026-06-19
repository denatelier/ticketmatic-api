"""Endpoint functions for opt-in settings."""

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
from ticketmatic.models.settings import OptIn, OptInQuery

_URL = "/{accountname}/settings/system/optins"
_ITEM = "/{accountname}/settings/system/optins/{id}"
OptInsList = make_list_type(OptIn)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(client: Client, params=None) -> OptInsList:
    """Get a list of opt ins.

    :param client: Ticketmatic API client.
    :param params: Optional query parameters
        (:class:`~ticketmatic.models.settings.OptInQuery`).
    :returns: A list of :class:`~ticketmatic.models.settings.OptIn` results.
    """
    return crud_get_list(client, _URL, OptInQuery, params, OptInsList, _FIELDS)


def get(client: Client, id: int) -> OptIn:
    """Get a single opt in.

    :param client: Ticketmatic API client.
    :param id: Opt-in ID.
    :returns: The requested :class:`~ticketmatic.models.settings.OptIn`.
    """
    return crud_get(client, _ITEM, id, OptIn)


def create(client: Client, data) -> OptIn:
    """Create a new opt in.

    :param client: Ticketmatic API client.
    :param data: Opt-in data (:class:`~ticketmatic.models.settings.OptIn` or dict).
    :returns: The created :class:`~ticketmatic.models.settings.OptIn`.
    """
    return crud_create(client, _URL, data, OptIn)


def update(client: Client, id: int, data) -> OptIn:
    """Modify an existing opt in.

    :param client: Ticketmatic API client.
    :param id: Opt-in ID.
    :param data: Updated opt-in data
        (:class:`~ticketmatic.models.settings.OptIn` or dict).
    :returns: The updated :class:`~ticketmatic.models.settings.OptIn`.
    """
    return crud_update(client, _ITEM, id, data, OptIn)


def delete(client: Client, id: int) -> None:
    """Remove an opt in.

    Opt ins are archivable: this call won't actually delete the object from
    the database. Instead, it will mark the object as archived, which means
    it won't show up anymore in most places.

    :param client: Ticketmatic API client.
    :param id: Opt-in ID.
    """
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    """Fetch translatable fields.

    Returns a dictionary with string values in all languages for each
    translatable field.

    :param client: Ticketmatic API client.
    :param id: Opt-in ID.
    :returns: Dictionary of translatable field values.
    """
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    """Update translations.

    Sets updated translation strings.

    :param client: Ticketmatic API client.
    :param id: Opt-in ID.
    :param data: Translation strings to set.
    :returns: Updated dictionary of translatable field values.
    """
    return crud_translate(client, f"{_ITEM}/translate", id, data)
