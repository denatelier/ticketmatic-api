"""Endpoint functions for contact field settings."""

from __future__ import annotations

from typing import Any

from ticketmatic.client import Client
from ticketmatic.endpoints.settings._crud import (
    crud_get,
    crud_translate,
    crud_translations,
    make_list_type,
)
from ticketmatic.models.contact import ContactField

_URL = "/{accountname}/settings/system/contactfields"
_ITEM = "/{accountname}/settings/system/contactfields/{id}"
ContactFieldsList = make_list_type(ContactField)


def get_list(client: Client) -> ContactFieldsList:
    """Get the contact fields.

    :param client: Ticketmatic API client.
    :returns: List of
        :class:`~ticketmatic.models.contact.ContactField` objects.
    """
    req = client.new_request("GET", _URL)
    return ContactFieldsList.from_dict(req.run())


def get(client: Client, id: int) -> ContactField:
    """Get the contact field.

    :param client: Ticketmatic API client.
    :param id: Contact field ID.
    :returns: The requested
        :class:`~ticketmatic.models.contact.ContactField`.
    """
    return crud_get(client, _ITEM, id, ContactField)


def translations(client: Client, id: int) -> Any:
    """Get the translations for this field.

    :param client: Ticketmatic API client.
    :param id: Contact field ID.
    :returns: Dictionary of translation strings.
    """
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    """Update the translations for this field.

    :param client: Ticketmatic API client.
    :param id: Contact field ID.
    :param data: Dictionary of translation strings to set.
    :returns: Updated dictionary of translation strings.
    """
    return crud_translate(client, f"{_ITEM}/translate", id, data)
