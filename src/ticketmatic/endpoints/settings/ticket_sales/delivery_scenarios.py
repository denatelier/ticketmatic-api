"""Endpoint functions for delivery scenario settings."""

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
from ticketmatic.models.settings import DeliveryScenario, DeliveryScenarioQuery

_URL = "/{accountname}/settings/ticketsales/deliveryscenarios"
_ITEM = "/{accountname}/settings/ticketsales/deliveryscenarios/{id}"
DeliveryScenariosList = make_list_type(DeliveryScenario)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(client: Client, params=None) -> DeliveryScenariosList:
    """Get a list of delivery scenarios.

    :param client: Ticketmatic API client.
    :param params: Optional query parameters
        (:class:`~ticketmatic.models.settings.DeliveryScenarioQuery`).
    :returns: A list of
        :class:`~ticketmatic.models.settings.DeliveryScenario` objects.
    """
    return crud_get_list(
        client, _URL, DeliveryScenarioQuery, params, DeliveryScenariosList, _FIELDS
    )


def get(client: Client, id: int) -> DeliveryScenario:
    """Get a single delivery scenario.

    :param client: Ticketmatic API client.
    :param id: Delivery scenario ID.
    :returns: The requested
        :class:`~ticketmatic.models.settings.DeliveryScenario`.
    """
    return crud_get(client, _ITEM, id, DeliveryScenario)


def create(client: Client, data) -> DeliveryScenario:
    """Create a new delivery scenario.

    :param client: Ticketmatic API client.
    :param data: Delivery scenario data
        (:class:`~ticketmatic.models.settings.DeliveryScenario`).
    :returns: The created
        :class:`~ticketmatic.models.settings.DeliveryScenario`.
    """
    return crud_create(client, _URL, data, DeliveryScenario)


def update(client: Client, id: int, data) -> DeliveryScenario:
    """Modify an existing delivery scenario.

    :param client: Ticketmatic API client.
    :param id: Delivery scenario ID.
    :param data: Updated delivery scenario data
        (:class:`~ticketmatic.models.settings.DeliveryScenario`).
    :returns: The updated
        :class:`~ticketmatic.models.settings.DeliveryScenario`.
    """
    return crud_update(client, _ITEM, id, data, DeliveryScenario)


def delete(client: Client, id: int) -> None:
    """Remove a delivery scenario.

    Delivery scenarios are archivable: this call won't actually delete the
    object from the database. Instead, it will mark the object as archived,
    which means it won't show up anymore in most places.

    :param client: Ticketmatic API client.
    :param id: Delivery scenario ID.
    """
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    """Fetch translatable fields.

    Returns a dictionary with string values in all languages for each
    translatable field.

    :param client: Ticketmatic API client.
    :param id: Delivery scenario ID.
    :returns: Translation strings keyed by language and field name.
    """
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    """Update translations.

    Sets updated translation strings.

    :param client: Ticketmatic API client.
    :param id: Delivery scenario ID.
    :param data: Translation strings to update.
    :returns: Updated translation strings keyed by language and field name.
    """
    return crud_translate(client, f"{_ITEM}/translate", id, data)
