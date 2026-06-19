"""Endpoint functions for managing price types."""

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
from ticketmatic.models.pricing import PriceType, PriceTypeQuery

_URL = "/{accountname}/settings/pricing/pricetypes"
_ITEM = "/{accountname}/settings/pricing/pricetypes/{id}"
PriceTypesList = make_list_type(PriceType)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(
    client: Client, params: PriceTypeQuery | dict | None = None
) -> PriceTypesList:
    """Get a list of price types.

    :param client: Ticketmatic API client.
    :param params: Optional query/filter parameters.
    :returns: A list of :class:`~ticketmatic.models.pricing.PriceType` objects.
    """
    return crud_get_list(client, _URL, PriceTypeQuery, params, PriceTypesList, _FIELDS)


def get(client: Client, id: int) -> PriceType:
    """Get a single price type.

    :param client: Ticketmatic API client.
    :param id: Price type ID.
    :returns: The requested :class:`~ticketmatic.models.pricing.PriceType`.
    """
    return crud_get(client, _ITEM, id, PriceType)


def create(client: Client, data: PriceType | dict) -> PriceType:
    """Create a new price type.

    :param client: Ticketmatic API client.
    :param data: Price type data.
    :returns: The created :class:`~ticketmatic.models.pricing.PriceType`.
    """
    return crud_create(client, _URL, data, PriceType)


def update(client: Client, id: int, data: PriceType | dict) -> PriceType:
    """Modify an existing price type.

    :param client: Ticketmatic API client.
    :param id: Price type ID.
    :param data: Updated price type data.
    :returns: The updated :class:`~ticketmatic.models.pricing.PriceType`.
    """
    return crud_update(client, _ITEM, id, data, PriceType)


def delete(client: Client, id: int) -> None:
    """Remove a price type.

    Price types are archivable: this call won't actually delete the object
    from the database. Instead, it will mark the object as archived, which
    means it won't show up anymore in most places.

    :param client: Ticketmatic API client.
    :param id: Price type ID.
    """
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    """Fetch translatable fields.

    Returns a dictionary with string values in all languages for each
    translatable field.

    :param client: Ticketmatic API client.
    :param id: Price type ID.
    :returns: Dictionary of translatable field values.
    """
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    """Update translations.

    Sets updated translation strings.

    :param client: Ticketmatic API client.
    :param id: Price type ID.
    :param data: Translation strings to set.
    :returns: Updated dictionary of translatable field values.
    """
    return crud_translate(client, f"{_ITEM}/translate", id, data)
