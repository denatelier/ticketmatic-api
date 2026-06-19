"""Endpoint functions for managing seat ranks."""

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
from ticketmatic.models.seating import SeatRank, SeatRankQuery

_URL = "/{accountname}/settings/seatingplans/seatranks"
_ITEM = "/{accountname}/settings/seatingplans/seatranks/{id}"
SeatRanksList = make_list_type(SeatRank)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(
    client: Client, params: SeatRankQuery | dict | None = None
) -> SeatRanksList:
    """Get a list of seat ranks.

    :param client: Ticketmatic API client.
    :param params: Optional query/filter parameters.
    :returns: A list of
        :class:`~ticketmatic.models.seating.SeatRank` objects.
    """
    return crud_get_list(client, _URL, SeatRankQuery, params, SeatRanksList, _FIELDS)


def get(client: Client, id: int) -> SeatRank:
    """Get a single seat rank.

    :param client: Ticketmatic API client.
    :param id: Seat rank ID.
    :returns: The requested
        :class:`~ticketmatic.models.seating.SeatRank`.
    """
    return crud_get(client, _ITEM, id, SeatRank)


def create(client: Client, data: SeatRank | dict) -> SeatRank:
    """Create a new seat rank.

    :param client: Ticketmatic API client.
    :param data: Seat rank data.
    :returns: The created
        :class:`~ticketmatic.models.seating.SeatRank`.
    """
    return crud_create(client, _URL, data, SeatRank)


def update(client: Client, id: int, data: SeatRank | dict) -> SeatRank:
    """Modify an existing seat rank.

    :param client: Ticketmatic API client.
    :param id: Seat rank ID.
    :param data: Updated seat rank data.
    :returns: The updated
        :class:`~ticketmatic.models.seating.SeatRank`.
    """
    return crud_update(client, _ITEM, id, data, SeatRank)


def delete(client: Client, id: int) -> None:
    """Remove a seat rank.

    Seat ranks are archivable: this call won't actually delete the object
    from the database. Instead, it will mark the object as archived, which
    means it won't show up anymore in most places.

    :param client: Ticketmatic API client.
    :param id: Seat rank ID.
    """
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    """Fetch translatable fields.

    Returns a dictionary with string values in all languages for each
    translatable field.

    :param client: Ticketmatic API client.
    :param id: Seat rank ID.
    :returns: Dictionary of translatable field values.
    """
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    """Update translations.

    Sets updated translation strings.

    :param client: Ticketmatic API client.
    :param id: Seat rank ID.
    :param data: Translation strings to set.
    :returns: Updated dictionary of translatable field values.
    """
    return crud_translate(client, f"{_ITEM}/translate", id, data)
