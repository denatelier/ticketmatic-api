"""Endpoint functions for phone number type settings."""

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
from ticketmatic.models.contact import PhoneNumberType, PhoneNumberTypeQuery

_URL = "/{accountname}/settings/system/phonenumbertypes"
_ITEM = "/{accountname}/settings/system/phonenumbertypes/{id}"
PhoneNumberTypesList = make_list_type(PhoneNumberType)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(client: Client, params=None) -> PhoneNumberTypesList:
    """Get a list of phone number types.

    :param client: Ticketmatic API client.
    :param params: Optional query parameters
        (:class:`~ticketmatic.models.contact.PhoneNumberTypeQuery`).
    :returns: A list of
        :class:`~ticketmatic.models.contact.PhoneNumberType` results.
    """
    return crud_get_list(
        client, _URL, PhoneNumberTypeQuery, params, PhoneNumberTypesList, _FIELDS
    )


def get(client: Client, id: int) -> PhoneNumberType:
    """Get a single phone number type.

    :param client: Ticketmatic API client.
    :param id: Phone number type ID.
    :returns: The requested
        :class:`~ticketmatic.models.contact.PhoneNumberType`.
    """
    return crud_get(client, _ITEM, id, PhoneNumberType)


def create(client: Client, data) -> PhoneNumberType:
    """Create a new phone number type.

    :param client: Ticketmatic API client.
    :param data: Phone number type data
        (:class:`~ticketmatic.models.contact.PhoneNumberType` or dict).
    :returns: The created
        :class:`~ticketmatic.models.contact.PhoneNumberType`.
    """
    return crud_create(client, _URL, data, PhoneNumberType)


def update(client: Client, id: int, data) -> PhoneNumberType:
    """Modify an existing phone number type.

    :param client: Ticketmatic API client.
    :param id: Phone number type ID.
    :param data: Updated phone number type data
        (:class:`~ticketmatic.models.contact.PhoneNumberType` or dict).
    :returns: The updated
        :class:`~ticketmatic.models.contact.PhoneNumberType`.
    """
    return crud_update(client, _ITEM, id, data, PhoneNumberType)


def delete(client: Client, id: int) -> None:
    """Remove a phone number type.

    Phone number types are archivable: this call won't actually delete the
    object from the database. Instead, it will mark the object as archived,
    which means it won't show up anymore in most places.

    :param client: Ticketmatic API client.
    :param id: Phone number type ID.
    """
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    """Fetch translatable fields.

    Returns a dictionary with string values in all languages for each
    translatable field.

    :param client: Ticketmatic API client.
    :param id: Phone number type ID.
    :returns: Dictionary of translatable field values.
    """
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    """Update translations.

    Sets updated translation strings.

    :param client: Ticketmatic API client.
    :param id: Phone number type ID.
    :param data: Translation strings to set.
    :returns: Updated dictionary of translatable field values.
    """
    return crud_translate(client, f"{_ITEM}/translate", id, data)
