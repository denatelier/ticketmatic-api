"""Endpoint functions for order fee settings."""

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
    make_list_type,
)
from ticketmatic.models.pricing import OrderFee, OrderFeeQuery

_URL = "/{accountname}/settings/ticketsales/orderfees"
_ITEM = "/{accountname}/settings/ticketsales/orderfees/{id}"
OrderFeesList = make_list_type(OrderFee)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(client: Client, params=None) -> OrderFeesList:
    """Get a list of order fees.

    :param client: Ticketmatic API client.
    :param params: Optional query parameters
        (:class:`~ticketmatic.models.pricing.OrderFeeQuery`).
    :returns: A list of
        :class:`~ticketmatic.models.pricing.OrderFee` objects.
    """
    return crud_get_list(client, _URL, OrderFeeQuery, params, OrderFeesList, _FIELDS)


def get(client: Client, id: int) -> OrderFee:
    """Get a single order fee.

    :param client: Ticketmatic API client.
    :param id: Order fee ID.
    :returns: The requested :class:`~ticketmatic.models.pricing.OrderFee`.
    """
    return crud_get(client, _ITEM, id, OrderFee)


def create(client: Client, data) -> OrderFee:
    """Create a new order fee.

    :param client: Ticketmatic API client.
    :param data: Order fee data
        (:class:`~ticketmatic.models.pricing.OrderFee`).
    :returns: The created :class:`~ticketmatic.models.pricing.OrderFee`.
    """
    return crud_create(client, _URL, data, OrderFee)


def delete(client: Client, id: int) -> None:
    """Remove an order fee.

    Order fees are archivable: this call won't actually delete the object
    from the database. Instead, it will mark the object as archived, which
    means it won't show up anymore in most places.

    :param client: Ticketmatic API client.
    :param id: Order fee ID.
    """
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    """Fetch translatable fields.

    Returns a dictionary with string values in all languages for each
    translatable field.

    :param client: Ticketmatic API client.
    :param id: Order fee ID.
    :returns: Translation strings keyed by language and field name.
    """
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    """Update translations.

    Sets updated translation strings.

    :param client: Ticketmatic API client.
    :param id: Order fee ID.
    :param data: Translation strings to update.
    :returns: Updated translation strings keyed by language and field name.
    """
    return crud_translate(client, f"{_ITEM}/translate", id, data)
