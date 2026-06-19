"""Endpoint functions for payment method settings."""

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
from ticketmatic.models.payment import PaymentMethod, PaymentMethodQuery

_URL = "/{accountname}/settings/ticketsales/paymentmethods"
_ITEM = "/{accountname}/settings/ticketsales/paymentmethods/{id}"
PaymentMethodsList = make_list_type(PaymentMethod)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(client: Client, params=None) -> PaymentMethodsList:
    """Get a list of payment methods.

    :param client: Ticketmatic API client.
    :param params: Optional query parameters
        (:class:`~ticketmatic.models.payment.PaymentMethodQuery`).
    :returns: A list of
        :class:`~ticketmatic.models.payment.PaymentMethod` objects.
    """
    return crud_get_list(
        client, _URL, PaymentMethodQuery, params, PaymentMethodsList, _FIELDS
    )


def get(client: Client, id: int) -> PaymentMethod:
    """Get a single payment method.

    :param client: Ticketmatic API client.
    :param id: Payment method ID.
    :returns: The requested
        :class:`~ticketmatic.models.payment.PaymentMethod`.
    """
    return crud_get(client, _ITEM, id, PaymentMethod)


def create(client: Client, data) -> PaymentMethod:
    """Create a new payment method.

    :param client: Ticketmatic API client.
    :param data: Payment method data
        (:class:`~ticketmatic.models.payment.PaymentMethod`).
    :returns: The created
        :class:`~ticketmatic.models.payment.PaymentMethod`.
    """
    return crud_create(client, _URL, data, PaymentMethod)


def update(client: Client, id: int, data) -> PaymentMethod:
    """Modify an existing payment method.

    :param client: Ticketmatic API client.
    :param id: Payment method ID.
    :param data: Updated payment method data
        (:class:`~ticketmatic.models.payment.PaymentMethod`).
    :returns: The updated
        :class:`~ticketmatic.models.payment.PaymentMethod`.
    """
    return crud_update(client, _ITEM, id, data, PaymentMethod)


def delete(client: Client, id: int) -> None:
    """Remove a payment method.

    Payment methods are archivable: this call won't actually delete the
    object from the database. Instead, it will mark the object as archived,
    which means it won't show up anymore in most places.

    :param client: Ticketmatic API client.
    :param id: Payment method ID.
    """
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    """Fetch translatable fields.

    Returns a dictionary with string values in all languages for each
    translatable field.

    :param client: Ticketmatic API client.
    :param id: Payment method ID.
    :returns: Translation strings keyed by language and field name.
    """
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    """Update translations.

    Sets updated translation strings.

    :param client: Ticketmatic API client.
    :param id: Payment method ID.
    :param data: Translation strings to update.
    :returns: Updated translation strings keyed by language and field name.
    """
    return crud_translate(client, f"{_ITEM}/translate", id, data)
