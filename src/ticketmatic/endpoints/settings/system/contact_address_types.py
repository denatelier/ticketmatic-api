"""Endpoint functions for contact address type settings."""

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
from ticketmatic.models.contact import ContactAddressType, ContactAddressTypeQuery

_URL = "/{accountname}/settings/system/contactaddresstypes"
_ITEM = "/{accountname}/settings/system/contactaddresstypes/{id}"
ContactAddressTypesList = make_list_type(ContactAddressType)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(client: Client, params=None) -> ContactAddressTypesList:
    """Get a list of contact address types.

    :param client: Ticketmatic API client.
    :param params: Optional filter parameters
        (:class:`~ticketmatic.models.contact.ContactAddressTypeQuery`).
    :returns: List of
        :class:`~ticketmatic.models.contact.ContactAddressType` objects.
    """
    return crud_get_list(
        client, _URL, ContactAddressTypeQuery, params, ContactAddressTypesList, _FIELDS
    )


def get(client: Client, id: int) -> ContactAddressType:
    """Get a single contact address type.

    :param client: Ticketmatic API client.
    :param id: Contact address type ID.
    :returns: The requested
        :class:`~ticketmatic.models.contact.ContactAddressType`.
    """
    return crud_get(client, _ITEM, id, ContactAddressType)


def create(client: Client, data) -> ContactAddressType:
    """Create a new contact address type.

    :param client: Ticketmatic API client.
    :param data: Contact address type data
        (:class:`~ticketmatic.models.contact.ContactAddressType` or dict).
    :returns: The created
        :class:`~ticketmatic.models.contact.ContactAddressType`.
    """
    return crud_create(client, _URL, data, ContactAddressType)


def update(client: Client, id: int, data) -> ContactAddressType:
    """Modify an existing contact address type.

    :param client: Ticketmatic API client.
    :param id: Contact address type ID.
    :param data: Updated contact address type data
        (:class:`~ticketmatic.models.contact.ContactAddressType` or dict).
    :returns: The updated
        :class:`~ticketmatic.models.contact.ContactAddressType`.
    """
    return crud_update(client, _ITEM, id, data, ContactAddressType)


def delete(client: Client, id: int) -> None:
    """Remove a contact address type.

    Contact address types are archivable: this call won't actually delete the
    object from the database. Instead, it will mark the object as archived,
    which means it won't show up anymore in most places.

    :param client: Ticketmatic API client.
    :param id: Contact address type ID.
    """
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    """Fetch translatable fields.

    Returns a dictionary with string values in all languages for each
    translatable field.

    :param client: Ticketmatic API client.
    :param id: Contact address type ID.
    :returns: Dictionary of translation strings.
    """
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    """Update translations.

    Sets updated translation strings.

    :param client: Ticketmatic API client.
    :param id: Contact address type ID.
    :param data: Dictionary of translation strings to set.
    :returns: Updated dictionary of translation strings.
    """
    return crud_translate(client, f"{_ITEM}/translate", id, data)
