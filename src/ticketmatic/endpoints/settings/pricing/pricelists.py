"""Endpoint functions for managing price lists."""

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
from ticketmatic.models.pricing import PriceList, PriceListQuery

_URL = "/{accountname}/settings/pricing/pricelists"
_ITEM = "/{accountname}/settings/pricing/pricelists/{id}"
PriceListsList = make_list_type(PriceList)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(
    client: Client, params: PriceListQuery | dict | None = None
) -> PriceListsList:
    """Get a list of price lists.

    :param client: Ticketmatic API client.
    :param params: Optional query/filter parameters.
    :returns: A list of :class:`~ticketmatic.models.pricing.PriceList` objects.
    """
    return crud_get_list(client, _URL, PriceListQuery, params, PriceListsList, _FIELDS)


def get(client: Client, id: int) -> PriceList:
    """Get a single price list.

    :param client: Ticketmatic API client.
    :param id: Price list ID.
    :returns: The requested :class:`~ticketmatic.models.pricing.PriceList`.
    """
    return crud_get(client, _ITEM, id, PriceList)


def create(client: Client, data: PriceList | dict) -> PriceList:
    """Create a new price list.

    :param client: Ticketmatic API client.
    :param data: Price list data.
    :returns: The created :class:`~ticketmatic.models.pricing.PriceList`.
    """
    return crud_create(client, _URL, data, PriceList)


def update(client: Client, id: int, data: PriceList | dict) -> PriceList:
    """Modify an existing price list.

    :param client: Ticketmatic API client.
    :param id: Price list ID.
    :param data: Updated price list data.
    :returns: The updated :class:`~ticketmatic.models.pricing.PriceList`.
    """
    return crud_update(client, _ITEM, id, data, PriceList)


def delete(client: Client, id: int) -> None:
    """Remove a price list.

    Price lists are archivable: this call won't actually delete the object
    from the database. Instead, it will mark the object as archived, which
    means it won't show up anymore in most places.

    :param client: Ticketmatic API client.
    :param id: Price list ID.
    """
    crud_delete(client, _ITEM, id)
