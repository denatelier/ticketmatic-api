"""Endpoint functions for contact title settings."""

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
from ticketmatic.models.contact import ContactTitle, ContactTitleQuery

_URL = "/{accountname}/settings/system/contacttitles"
_ITEM = "/{accountname}/settings/system/contacttitles/{id}"
ContactTitlesList = make_list_type(ContactTitle)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(client: Client, params=None) -> ContactTitlesList:
    """Get a list of contact titles.

    :param client: Ticketmatic API client.
    :param params: Optional filter parameters
        (:class:`~ticketmatic.models.contact.ContactTitleQuery`).
    :returns: List of
        :class:`~ticketmatic.models.contact.ContactTitle` objects.
    """
    return crud_get_list(
        client, _URL, ContactTitleQuery, params, ContactTitlesList, _FIELDS
    )


def get(client: Client, id: int) -> ContactTitle:
    """Get a single contact title.

    :param client: Ticketmatic API client.
    :param id: Contact title ID.
    :returns: The requested
        :class:`~ticketmatic.models.contact.ContactTitle`.
    """
    return crud_get(client, _ITEM, id, ContactTitle)


def create(client: Client, data) -> ContactTitle:
    """Create a new contact title.

    :param client: Ticketmatic API client.
    :param data: Contact title data
        (:class:`~ticketmatic.models.contact.ContactTitle` or dict).
    :returns: The created
        :class:`~ticketmatic.models.contact.ContactTitle`.
    """
    return crud_create(client, _URL, data, ContactTitle)


def update(client: Client, id: int, data) -> ContactTitle:
    """Modify an existing contact title.

    :param client: Ticketmatic API client.
    :param id: Contact title ID.
    :param data: Updated contact title data
        (:class:`~ticketmatic.models.contact.ContactTitle` or dict).
    :returns: The updated
        :class:`~ticketmatic.models.contact.ContactTitle`.
    """
    return crud_update(client, _ITEM, id, data, ContactTitle)


def delete(client: Client, id: int) -> None:
    """Remove a contact title.

    Contact titles are archivable: this call won't actually delete the object
    from the database. Instead, it will mark the object as archived, which
    means it won't show up anymore in most places.

    :param client: Ticketmatic API client.
    :param id: Contact title ID.
    """
    crud_delete(client, _ITEM, id)
