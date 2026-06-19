"""Endpoint functions for managing order fee definitions."""

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
from ticketmatic.models.pricing import OrderFeeDefinition, OrderFeeDefinitionQuery

_URL = "/{accountname}/settings/pricing/orderfeedefinitions"
_ITEM = "/{accountname}/settings/pricing/orderfeedefinitions/{id}"
OrderFeeDefinitionsList = make_list_type(OrderFeeDefinition)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(
    client: Client, params: OrderFeeDefinitionQuery | dict | None = None
) -> OrderFeeDefinitionsList:
    """Get a list of order fee definitions.

    :param client: Ticketmatic API client.
    :param params: Optional query/filter parameters.
    :returns: A list of
        :class:`~ticketmatic.models.pricing.OrderFeeDefinition` objects.
    """
    return crud_get_list(
        client, _URL, OrderFeeDefinitionQuery, params, OrderFeeDefinitionsList, _FIELDS
    )


def get(client: Client, id: int) -> OrderFeeDefinition:
    """Get a single order fee definition.

    :param client: Ticketmatic API client.
    :param id: Order fee definition ID.
    :returns: The requested
        :class:`~ticketmatic.models.pricing.OrderFeeDefinition`.
    """
    return crud_get(client, _ITEM, id, OrderFeeDefinition)


def create(client: Client, data: OrderFeeDefinition | dict) -> OrderFeeDefinition:
    """Create a new order fee definition.

    :param client: Ticketmatic API client.
    :param data: Order fee definition data.
    :returns: The created
        :class:`~ticketmatic.models.pricing.OrderFeeDefinition`.
    """
    return crud_create(client, _URL, data, OrderFeeDefinition)


def delete(client: Client, id: int) -> None:
    """Remove an order fee definition.

    Order fee definitions are archivable: this call won't actually delete the
    object from the database. Instead, it will mark the object as archived,
    which means it won't show up anymore in most places.

    :param client: Ticketmatic API client.
    :param id: Order fee definition ID.
    """
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    """Fetch translatable fields.

    Returns a dictionary with string values in all languages for each
    translatable field.

    :param client: Ticketmatic API client.
    :param id: Order fee definition ID.
    :returns: Dictionary of translatable field values.
    """
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    """Update translations.

    Sets updated translation strings.

    :param client: Ticketmatic API client.
    :param id: Order fee definition ID.
    :param data: Translation strings to set.
    :returns: Updated dictionary of translatable field values.
    """
    return crud_translate(client, f"{_ITEM}/translate", id, data)
