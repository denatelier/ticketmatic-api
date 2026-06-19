"""Endpoint functions for field definition settings."""

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
from ticketmatic.json_utils import unpack_array
from ticketmatic.models.settings import (
    FieldDefinition,
    FieldDefinitionQuery,
    FielddefinitionsDataRequest,
    FielddefinitionsDataResult,
)

_URL = "/{accountname}/settings/system/fielddefinitions"
_ITEM = "/{accountname}/settings/system/fielddefinitions/{id}"
FieldDefinitionsList = make_list_type(FieldDefinition)
_FIELDS = ["typeid", "filter", "includearchived", "lastupdatesince"]


def get_list(client: Client, params=None) -> FieldDefinitionsList:
    """Get a list of field definitions.

    :param client: Ticketmatic API client.
    :param params: Optional filter parameters
        (:class:`~ticketmatic.models.settings.FieldDefinitionQuery`).
    :returns: List of
        :class:`~ticketmatic.models.settings.FieldDefinition` objects.
    """
    return crud_get_list(
        client, _URL, FieldDefinitionQuery, params, FieldDefinitionsList, _FIELDS
    )


def get(client: Client, id: int) -> FieldDefinition:
    """Get a single field definition.

    :param client: Ticketmatic API client.
    :param id: Field definition ID.
    :returns: The requested
        :class:`~ticketmatic.models.settings.FieldDefinition`.
    """
    return crud_get(client, _ITEM, id, FieldDefinition)


def create(client: Client, data) -> FieldDefinition:
    """Create a new field definition.

    :param client: Ticketmatic API client.
    :param data: Field definition data
        (:class:`~ticketmatic.models.settings.FieldDefinition` or dict).
    :returns: The created
        :class:`~ticketmatic.models.settings.FieldDefinition`.
    """
    return crud_create(client, _URL, data, FieldDefinition)


def update(client: Client, id: int, data) -> FieldDefinition:
    """Modify an existing field definition.

    :param client: Ticketmatic API client.
    :param id: Field definition ID.
    :param data: Updated field definition data
        (:class:`~ticketmatic.models.settings.FieldDefinition` or dict).
    :returns: The updated
        :class:`~ticketmatic.models.settings.FieldDefinition`.
    """
    return crud_update(client, _ITEM, id, data, FieldDefinition)


def delete(client: Client, id: int) -> None:
    """Remove a field definition.

    Field definitions are archivable: this call won't actually delete the
    object from the database. Instead, it will mark the object as archived,
    which means it won't show up anymore in most places.

    :param client: Ticketmatic API client.
    :param id: Field definition ID.
    """
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    """Fetch translatable fields.

    Returns a dictionary with string values in all languages for each
    translatable field.

    :param client: Ticketmatic API client.
    :param id: Field definition ID.
    :returns: Dictionary of translation strings.
    """
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    """Update translations.

    Sets updated translation strings.

    :param client: Ticketmatic API client.
    :param id: Field definition ID.
    :param data: Dictionary of translation strings to set.
    :returns: Updated dictionary of translation strings.
    """
    return crud_translate(client, f"{_ITEM}/translate", id, data)


def get_data(
    client: Client, data: FielddefinitionsDataRequest | dict
) -> list[FielddefinitionsDataResult]:
    """Get data for field definitions.

    :param client: Ticketmatic API client.
    :param data: Data request parameters
        (:class:`~ticketmatic.models.settings.FielddefinitionsDataRequest`
        or dict).
    :returns: List of
        :class:`~ticketmatic.models.settings.FielddefinitionsDataResult`
        objects.
    """
    if isinstance(data, dict):
        data = FielddefinitionsDataRequest.from_dict(data)
    req = client.new_request("POST", f"{_URL}/data")
    req.set_body(data.to_dict())
    return unpack_array(FielddefinitionsDataResult, req.run())
