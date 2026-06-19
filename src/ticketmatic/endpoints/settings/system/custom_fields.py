"""Endpoint functions for custom field and custom field value settings."""

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
from ticketmatic.models.settings import (
    CustomField,
    CustomFieldQuery,
    CustomFieldValue,
    CustomFieldValueQuery,
)

_URL = "/{accountname}/settings/system/customfields"
_ITEM = "/{accountname}/settings/system/customfields/{id}"
CustomFieldsList = make_list_type(CustomField)

_VAL_URL = "/{accountname}/settings/system/customfieldvalues"
_VAL_ITEM = "/{accountname}/settings/system/customfieldvalues/{id}"
CustomFieldValuesList = make_list_type(CustomFieldValue)
_FIELDS = ["typeid", "filter", "includearchived", "lastupdatesince"]


def get_list(client: Client, params=None) -> CustomFieldsList:
    """Get a list of custom fields.

    :param client: Ticketmatic API client.
    :param params: Optional filter parameters
        (:class:`~ticketmatic.models.settings.CustomFieldQuery`).
    :returns: List of
        :class:`~ticketmatic.models.settings.CustomField` objects.
    """
    return crud_get_list(
        client, _URL, CustomFieldQuery, params, CustomFieldsList, _FIELDS
    )


def get(client: Client, id: int) -> CustomField:
    """Get a single custom field.

    :param client: Ticketmatic API client.
    :param id: Custom field ID.
    :returns: The requested
        :class:`~ticketmatic.models.settings.CustomField`.
    """
    return crud_get(client, _ITEM, id, CustomField)


def create(client: Client, data) -> CustomField:
    """Create a new custom field.

    :param client: Ticketmatic API client.
    :param data: Custom field data
        (:class:`~ticketmatic.models.settings.CustomField` or dict).
    :returns: The created
        :class:`~ticketmatic.models.settings.CustomField`.
    """
    return crud_create(client, _URL, data, CustomField)


def update(client: Client, id: int, data) -> CustomField:
    """Modify an existing custom field.

    :param client: Ticketmatic API client.
    :param id: Custom field ID.
    :param data: Updated custom field data
        (:class:`~ticketmatic.models.settings.CustomField` or dict).
    :returns: The updated
        :class:`~ticketmatic.models.settings.CustomField`.
    """
    return crud_update(client, _ITEM, id, data, CustomField)


def delete(client: Client, id: int) -> None:
    """Remove a custom field.

    Custom fields are archivable: this call won't actually delete the object
    from the database. Instead, it will mark the object as archived, which
    means it won't show up anymore in most places.

    :param client: Ticketmatic API client.
    :param id: Custom field ID.
    """
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    """Fetch translatable fields.

    Returns a dictionary with string values in all languages for each
    translatable field.

    :param client: Ticketmatic API client.
    :param id: Custom field ID.
    :returns: Dictionary of translation strings.
    """
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    """Update translations.

    Sets updated translation strings.

    :param client: Ticketmatic API client.
    :param id: Custom field ID.
    :param data: Dictionary of translation strings to set.
    :returns: Updated dictionary of translation strings.
    """
    return crud_translate(client, f"{_ITEM}/translate", id, data)


# Custom field values
def values_get_list(client: Client, params=None) -> CustomFieldValuesList:
    """Get a list of custom field values.

    :param client: Ticketmatic API client.
    :param params: Optional filter parameters
        (:class:`~ticketmatic.models.settings.CustomFieldValueQuery`).
    :returns: List of
        :class:`~ticketmatic.models.settings.CustomFieldValue` objects.
    """
    return crud_get_list(
        client, _VAL_URL, CustomFieldValueQuery, params, CustomFieldValuesList, _FIELDS
    )


def values_get(client: Client, id: int) -> CustomFieldValue:
    """Get a single custom field value.

    :param client: Ticketmatic API client.
    :param id: Custom field value ID.
    :returns: The requested
        :class:`~ticketmatic.models.settings.CustomFieldValue`.
    """
    return crud_get(client, _VAL_ITEM, id, CustomFieldValue)


def values_create(client: Client, data) -> CustomFieldValue:
    """Create a new custom field value.

    :param client: Ticketmatic API client.
    :param data: Custom field value data
        (:class:`~ticketmatic.models.settings.CustomFieldValue` or dict).
    :returns: The created
        :class:`~ticketmatic.models.settings.CustomFieldValue`.
    """
    return crud_create(client, _VAL_URL, data, CustomFieldValue)


def values_update(client: Client, id: int, data) -> CustomFieldValue:
    """Modify an existing custom field value.

    :param client: Ticketmatic API client.
    :param id: Custom field value ID.
    :param data: Updated custom field value data
        (:class:`~ticketmatic.models.settings.CustomFieldValue` or dict).
    :returns: The updated
        :class:`~ticketmatic.models.settings.CustomFieldValue`.
    """
    return crud_update(client, _VAL_ITEM, id, data, CustomFieldValue)


def values_delete(client: Client, id: int) -> None:
    """Remove a custom field value.

    Custom field values are archivable: this call won't actually delete the
    object from the database. Instead, it will mark the object as archived,
    which means it won't show up anymore in most places.

    :param client: Ticketmatic API client.
    :param id: Custom field value ID.
    """
    crud_delete(client, _VAL_ITEM, id)


def values_translations(client: Client, id: int) -> Any:
    """Fetch translatable fields for a custom field value.

    Returns a dictionary with string values in all languages for each
    translatable field.

    :param client: Ticketmatic API client.
    :param id: Custom field value ID.
    :returns: Dictionary of translation strings.
    """
    return crud_translations(client, f"{_VAL_ITEM}/translate", id)


def values_translate(client: Client, id: int, data: dict) -> Any:
    """Update translations for a custom field value.

    Sets updated translation strings.

    :param client: Ticketmatic API client.
    :param id: Custom field value ID.
    :param data: Dictionary of translation strings to set.
    :returns: Updated dictionary of translation strings.
    """
    return crud_translate(client, f"{_VAL_ITEM}/translate", id, data)
