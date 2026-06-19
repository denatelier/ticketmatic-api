"""Endpoint functions for payment scenario settings."""

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
from ticketmatic.models.payment import PaymentScenario, PaymentScenarioQuery

_URL = "/{accountname}/settings/ticketsales/paymentscenarios"
_ITEM = "/{accountname}/settings/ticketsales/paymentscenarios/{id}"
PaymentScenariosList = make_list_type(PaymentScenario)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(client: Client, params=None) -> PaymentScenariosList:
    """Get a list of payment scenarios.

    :param client: Ticketmatic API client.
    :param params: Optional query parameters
        (:class:`~ticketmatic.models.payment.PaymentScenarioQuery`).
    :returns: A list of
        :class:`~ticketmatic.models.payment.PaymentScenario` objects.
    """
    return crud_get_list(
        client, _URL, PaymentScenarioQuery, params, PaymentScenariosList, _FIELDS
    )


def get(client: Client, id: int) -> PaymentScenario:
    """Get a single payment scenario.

    :param client: Ticketmatic API client.
    :param id: Payment scenario ID.
    :returns: The requested
        :class:`~ticketmatic.models.payment.PaymentScenario`.
    """
    return crud_get(client, _ITEM, id, PaymentScenario)


def create(client: Client, data) -> PaymentScenario:
    """Create a new payment scenario.

    :param client: Ticketmatic API client.
    :param data: Payment scenario data
        (:class:`~ticketmatic.models.payment.PaymentScenario`).
    :returns: The created
        :class:`~ticketmatic.models.payment.PaymentScenario`.
    """
    return crud_create(client, _URL, data, PaymentScenario)


def update(client: Client, id: int, data) -> PaymentScenario:
    """Modify an existing payment scenario.

    :param client: Ticketmatic API client.
    :param id: Payment scenario ID.
    :param data: Updated payment scenario data
        (:class:`~ticketmatic.models.payment.PaymentScenario`).
    :returns: The updated
        :class:`~ticketmatic.models.payment.PaymentScenario`.
    """
    return crud_update(client, _ITEM, id, data, PaymentScenario)


def delete(client: Client, id: int) -> None:
    """Remove a payment scenario.

    Payment scenarios are archivable: this call won't actually delete the
    object from the database. Instead, it will mark the object as archived,
    which means it won't show up anymore in most places.

    :param client: Ticketmatic API client.
    :param id: Payment scenario ID.
    """
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    """Fetch translatable fields.

    Returns a dictionary with string values in all languages for each
    translatable field.

    :param client: Ticketmatic API client.
    :param id: Payment scenario ID.
    :returns: Translation strings keyed by language and field name.
    """
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    """Update translations.

    Sets updated translation strings.

    :param client: Ticketmatic API client.
    :param id: Payment scenario ID.
    :param data: Translation strings to update.
    :returns: Updated translation strings keyed by language and field name.
    """
    return crud_translate(client, f"{_ITEM}/translate", id, data)
