"""Endpoint functions for relation type settings."""

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
from ticketmatic.models.settings import RelationType, RelationTypeQuery

_URL = "/{accountname}/settings/system/relationtypes"
_ITEM = "/{accountname}/settings/system/relationtypes/{id}"
RelationTypesList = make_list_type(RelationType)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(client: Client, params=None) -> RelationTypesList:
    """Get a list of relation types.

    :param client: Ticketmatic API client.
    :param params: Optional query parameters
        (:class:`~ticketmatic.models.settings.RelationTypeQuery`).
    :returns: A list of
        :class:`~ticketmatic.models.settings.RelationType` results.
    """
    return crud_get_list(
        client, _URL, RelationTypeQuery, params, RelationTypesList, _FIELDS
    )


def get(client: Client, id: int) -> RelationType:
    """Get a single relation type.

    :param client: Ticketmatic API client.
    :param id: Relation type ID.
    :returns: The requested
        :class:`~ticketmatic.models.settings.RelationType`.
    """
    return crud_get(client, _ITEM, id, RelationType)


def create(client: Client, data) -> RelationType:
    """Create a new relation type.

    :param client: Ticketmatic API client.
    :param data: Relation type data
        (:class:`~ticketmatic.models.settings.RelationType` or dict).
    :returns: The created
        :class:`~ticketmatic.models.settings.RelationType`.
    """
    return crud_create(client, _URL, data, RelationType)


def update(client: Client, id: int, data) -> RelationType:
    """Modify an existing relation type.

    :param client: Ticketmatic API client.
    :param id: Relation type ID.
    :param data: Updated relation type data
        (:class:`~ticketmatic.models.settings.RelationType` or dict).
    :returns: The updated
        :class:`~ticketmatic.models.settings.RelationType`.
    """
    return crud_update(client, _ITEM, id, data, RelationType)


def delete(client: Client, id: int) -> None:
    """Remove a relation type.

    Relation types are archivable: this call won't actually delete the object
    from the database. Instead, it will mark the object as archived, which
    means it won't show up anymore in most places.

    :param client: Ticketmatic API client.
    :param id: Relation type ID.
    """
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    """Fetch translatable fields.

    Returns a dictionary with string values in all languages for each
    translatable field.

    :param client: Ticketmatic API client.
    :param id: Relation type ID.
    :returns: Dictionary of translatable field values.
    """
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    """Update translations.

    Sets updated translation strings.

    :param client: Ticketmatic API client.
    :param id: Relation type ID.
    :param data: Translation strings to set.
    :returns: Updated dictionary of translatable field values.
    """
    return crud_translate(client, f"{_ITEM}/translate", id, data)
