"""Endpoint functions for sales channel settings."""

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
from ticketmatic.models.settings import SalesChannel, SalesChannelQuery

_URL = "/{accountname}/settings/ticketsales/saleschannels"
_ITEM = "/{accountname}/settings/ticketsales/saleschannels/{id}"
SalesChannelsList = make_list_type(SalesChannel)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(client: Client, params=None) -> SalesChannelsList:
    """Get a list of sales channels.

    :param client: Ticketmatic API client.
    :param params: Optional query parameters
        (:class:`~ticketmatic.models.settings.SalesChannelQuery`).
    :returns: A list of
        :class:`~ticketmatic.models.settings.SalesChannel` objects.
    """
    return crud_get_list(
        client, _URL, SalesChannelQuery, params, SalesChannelsList, _FIELDS
    )


def get(client: Client, id: int) -> SalesChannel:
    """Get a single sales channel.

    :param client: Ticketmatic API client.
    :param id: Sales channel ID.
    :returns: The requested
        :class:`~ticketmatic.models.settings.SalesChannel`.
    """
    return crud_get(client, _ITEM, id, SalesChannel)


def create(client: Client, data) -> SalesChannel:
    """Create a new sales channel.

    :param client: Ticketmatic API client.
    :param data: Sales channel data
        (:class:`~ticketmatic.models.settings.SalesChannel`).
    :returns: The created
        :class:`~ticketmatic.models.settings.SalesChannel`.
    """
    return crud_create(client, _URL, data, SalesChannel)


def update(client: Client, id: int, data) -> SalesChannel:
    """Modify an existing sales channel.

    :param client: Ticketmatic API client.
    :param id: Sales channel ID.
    :param data: Updated sales channel data
        (:class:`~ticketmatic.models.settings.SalesChannel`).
    :returns: The updated
        :class:`~ticketmatic.models.settings.SalesChannel`.
    """
    return crud_update(client, _ITEM, id, data, SalesChannel)


def delete(client: Client, id: int) -> None:
    """Remove a sales channel.

    Sales channels are archivable: this call won't actually delete the
    object from the database. Instead, it will mark the object as archived,
    which means it won't show up anymore in most places.

    :param client: Ticketmatic API client.
    :param id: Sales channel ID.
    """
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    """Fetch translatable fields.

    Returns a dictionary with string values in all languages for each
    translatable field.

    :param client: Ticketmatic API client.
    :param id: Sales channel ID.
    :returns: Translation strings keyed by language and field name.
    """
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    """Update translations.

    Sets updated translation strings.

    :param client: Ticketmatic API client.
    :param id: Sales channel ID.
    :param data: Translation strings to update.
    :returns: Updated translation strings keyed by language and field name.
    """
    return crud_translate(client, f"{_ITEM}/translate", id, data)
