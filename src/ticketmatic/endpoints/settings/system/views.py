"""Endpoint functions for view settings."""

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
from ticketmatic.models.settings import View, ViewQuery

_URL = "/{accountname}/settings/system/views"
_ITEM = "/{accountname}/settings/system/views/{id}"
ViewsList = make_list_type(View)
_FIELDS = ["typeid", "filter", "includearchived", "lastupdatesince"]


def get_list(client: Client, params=None) -> ViewsList:
    """Get a list of views.

    :param client: Ticketmatic API client.
    :param params: Optional query parameters
        (:class:`~ticketmatic.models.settings.ViewQuery`).
    :returns: A list of :class:`~ticketmatic.models.settings.View` results.
    """
    return crud_get_list(client, _URL, ViewQuery, params, ViewsList, _FIELDS)


def get(client: Client, id: int) -> View:
    """Get a single view.

    :param client: Ticketmatic API client.
    :param id: View ID.
    :returns: The requested :class:`~ticketmatic.models.settings.View`.
    """
    return crud_get(client, _ITEM, id, View)


def create(client: Client, data) -> View:
    """Create a new view.

    :param client: Ticketmatic API client.
    :param data: View data
        (:class:`~ticketmatic.models.settings.View` or dict).
    :returns: The created :class:`~ticketmatic.models.settings.View`.
    """
    return crud_create(client, _URL, data, View)


def update(client: Client, id: int, data) -> View:
    """Modify an existing view.

    :param client: Ticketmatic API client.
    :param id: View ID.
    :param data: Updated view data
        (:class:`~ticketmatic.models.settings.View` or dict).
    :returns: The updated :class:`~ticketmatic.models.settings.View`.
    """
    return crud_update(client, _ITEM, id, data, View)


def delete(client: Client, id: int) -> None:
    """Remove a view.

    Views are archivable: this call won't actually delete the object from the
    database. Instead, it will mark the object as archived, which means it
    won't show up anymore in most places.

    :param client: Ticketmatic API client.
    :param id: View ID.
    """
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    """Fetch translatable fields.

    Returns a dictionary with string values in all languages for each
    translatable field.

    :param client: Ticketmatic API client.
    :param id: View ID.
    :returns: Dictionary of translatable field values.
    """
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    """Update translations.

    Sets updated translation strings.

    :param client: Ticketmatic API client.
    :param id: View ID.
    :param data: Translation strings to set.
    :returns: Updated dictionary of translatable field values.
    """
    return crud_translate(client, f"{_ITEM}/translate", id, data)
