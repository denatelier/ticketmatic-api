"""Endpoint functions for filter definition settings."""

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
from ticketmatic.models.settings import FilterDefinition, FilterDefinitionQuery

_URL = "/{accountname}/settings/system/filterdefinitions"
_ITEM = "/{accountname}/settings/system/filterdefinitions/{id}"
FilterDefinitionsList = make_list_type(FilterDefinition)
_FIELDS = ["typeid", "filter", "includearchived", "lastupdatesince"]


def get_list(client: Client, params=None) -> FilterDefinitionsList:
    """Get a list of filter definitions.

    :param client: Ticketmatic API client.
    :param params: Optional filter parameters
        (:class:`~ticketmatic.models.settings.FilterDefinitionQuery`).
    :returns: List of
        :class:`~ticketmatic.models.settings.FilterDefinition` objects.
    """
    return crud_get_list(
        client, _URL, FilterDefinitionQuery, params, FilterDefinitionsList, _FIELDS
    )


def get(client: Client, id: int) -> FilterDefinition:
    """Get a single filter definition.

    :param client: Ticketmatic API client.
    :param id: Filter definition ID.
    :returns: The requested
        :class:`~ticketmatic.models.settings.FilterDefinition`.
    """
    return crud_get(client, _ITEM, id, FilterDefinition)


def create(client: Client, data) -> FilterDefinition:
    """Create a new filter definition.

    :param client: Ticketmatic API client.
    :param data: Filter definition data
        (:class:`~ticketmatic.models.settings.FilterDefinition` or dict).
    :returns: The created
        :class:`~ticketmatic.models.settings.FilterDefinition`.
    """
    return crud_create(client, _URL, data, FilterDefinition)


def update(client: Client, id: int, data) -> FilterDefinition:
    """Modify an existing filter definition.

    :param client: Ticketmatic API client.
    :param id: Filter definition ID.
    :param data: Updated filter definition data
        (:class:`~ticketmatic.models.settings.FilterDefinition` or dict).
    :returns: The updated
        :class:`~ticketmatic.models.settings.FilterDefinition`.
    """
    return crud_update(client, _ITEM, id, data, FilterDefinition)


def delete(client: Client, id: int) -> None:
    """Remove a filter definition.

    Filter definitions are archivable: this call won't actually delete the
    object from the database. Instead, it will mark the object as archived,
    which means it won't show up anymore in most places.

    :param client: Ticketmatic API client.
    :param id: Filter definition ID.
    """
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    """Fetch translatable fields.

    Returns a dictionary with string values in all languages for each
    translatable field.

    :param client: Ticketmatic API client.
    :param id: Filter definition ID.
    :returns: Dictionary of translation strings.
    """
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    """Update translations.

    Sets updated translation strings.

    :param client: Ticketmatic API client.
    :param id: Filter definition ID.
    :param data: Dictionary of translation strings to set.
    :returns: Updated dictionary of translation strings.
    """
    return crud_translate(client, f"{_ITEM}/translate", id, data)
