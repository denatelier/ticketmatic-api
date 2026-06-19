"""Endpoint functions for communication and design documents."""

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
from ticketmatic.models.settings import Document, DocumentQuery

_URL = "/{accountname}/settings/communicationanddesign/documents"
_ITEM = "/{accountname}/settings/communicationanddesign/documents/{id}"
DocumentsList = make_list_type(Document)
_FIELDS = ["typeid", "filter", "lastupdatesince"]


def get_list(
    client: Client, params: DocumentQuery | dict | None = None
) -> DocumentsList:
    """Get a list of documents.

    :param client: Ticketmatic API client.
    :param params: Optional filter/query parameters.
    :returns: A :class:`~ticketmatic.models.settings.Document` list result.
    """
    return crud_get_list(client, _URL, DocumentQuery, params, DocumentsList, _FIELDS)


def get(client: Client, id: int) -> Document:
    """Get a single document.

    :param client: Ticketmatic API client.
    :param id: Document ID.
    :returns: The requested :class:`~ticketmatic.models.settings.Document`.
    """
    return crud_get(client, _ITEM, id, Document)


def create(client: Client, data: Document | dict) -> Document:
    """Create a new document.

    :param client: Ticketmatic API client.
    :param data: Document data to create.
    :returns: The created :class:`~ticketmatic.models.settings.Document`.
    """
    return crud_create(client, _URL, data, Document)


def update(client: Client, id: int, data: Document | dict) -> Document:
    """Modify an existing document.

    :param client: Ticketmatic API client.
    :param id: Document ID.
    :param data: Updated document data.
    :returns: The updated :class:`~ticketmatic.models.settings.Document`.
    """
    return crud_update(client, _ITEM, id, data, Document)


def delete(client: Client, id: int) -> None:
    """Remove a document.

    :param client: Ticketmatic API client.
    :param id: Document ID.
    """
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    """Fetch translatable fields.

    Returns a dictionary with string values in all languages for each
    translatable field.

    :param client: Ticketmatic API client.
    :param id: Document ID.
    :returns: A mapping of translatable field values by language.
    """
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    """Update translations.

    Sets updated translation strings.

    :param client: Ticketmatic API client.
    :param id: Document ID.
    :param data: Translation strings to update.
    :returns: The updated translation mapping.
    """
    return crud_translate(client, f"{_ITEM}/translate", id, data)
