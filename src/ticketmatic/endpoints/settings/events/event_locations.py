"""Endpoint functions for managing event locations."""

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
from ticketmatic.models.event import EventLocation, EventLocationQuery

_URL = "/{accountname}/settings/events/eventlocations"
_ITEM = "/{accountname}/settings/events/eventlocations/{id}"
EventLocationsList = make_list_type(EventLocation)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(
    client: Client, params: EventLocationQuery | dict | None = None
) -> EventLocationsList:
    """Get a list of event locations.

    :param client: Ticketmatic API client.
    :param params: Optional query/filter parameters.
    :returns: A list of :class:`~ticketmatic.models.event.EventLocation` objects.
    """
    return crud_get_list(
        client, _URL, EventLocationQuery, params, EventLocationsList, _FIELDS
    )


def get(client: Client, id: int) -> EventLocation:
    """Get a single event location.

    :param client: Ticketmatic API client.
    :param id: Event location ID.
    :returns: The requested :class:`~ticketmatic.models.event.EventLocation`.
    """
    return crud_get(client, _ITEM, id, EventLocation)


def create(client: Client, data: EventLocation | dict) -> EventLocation:
    """Create a new event location.

    :param client: Ticketmatic API client.
    :param data: Event location data.
    :returns: The created :class:`~ticketmatic.models.event.EventLocation`.
    """
    return crud_create(client, _URL, data, EventLocation)


def update(client: Client, id: int, data: EventLocation | dict) -> EventLocation:
    """Modify an existing event location.

    :param client: Ticketmatic API client.
    :param id: Event location ID.
    :param data: Updated event location data.
    :returns: The updated :class:`~ticketmatic.models.event.EventLocation`.
    """
    return crud_update(client, _ITEM, id, data, EventLocation)


def delete(client: Client, id: int) -> None:
    """Remove an event location.

    Event locations are archivable: this call won't actually delete the object
    from the database. Instead, it will mark the object as archived, which
    means it won't show up anymore in most places.

    :param client: Ticketmatic API client.
    :param id: Event location ID.
    """
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    """Fetch translatable fields.

    Returns a dictionary with string values in all languages for each
    translatable field.

    :param client: Ticketmatic API client.
    :param id: Event location ID.
    :returns: Dictionary of translatable field values.
    """
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    """Update translations.

    Sets updated translation strings.

    :param client: Ticketmatic API client.
    :param id: Event location ID.
    :param data: Translation strings to set.
    :returns: Updated dictionary of translatable field values.
    """
    return crud_translate(client, f"{_ITEM}/translate", id, data)
