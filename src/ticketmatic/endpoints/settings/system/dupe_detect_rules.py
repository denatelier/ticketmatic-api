"""Endpoint functions for duplicate detection rule settings."""

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
from ticketmatic.models.settings import DupeDetectRule, DupeDetectRuleQuery

_URL = "/{accountname}/settings/system/dupedetectrules"
_ITEM = "/{accountname}/settings/system/dupedetectrules/{id}"
DupeDetectRulesList = make_list_type(DupeDetectRule)
_FIELDS = ["filter", "lastupdatesince"]


def get_list(client: Client, params=None) -> DupeDetectRulesList:
    """Get a list of dupe detect rules.

    :param client: Ticketmatic API client.
    :param params: Optional filter parameters
        (:class:`~ticketmatic.models.settings.DupeDetectRuleQuery`).
    :returns: List of
        :class:`~ticketmatic.models.settings.DupeDetectRule` objects.
    """
    return crud_get_list(
        client, _URL, DupeDetectRuleQuery, params, DupeDetectRulesList, _FIELDS
    )


def get(client: Client, id: int) -> DupeDetectRule:
    """Get a single dupe detect rule.

    :param client: Ticketmatic API client.
    :param id: Dupe detect rule ID.
    :returns: The requested
        :class:`~ticketmatic.models.settings.DupeDetectRule`.
    """
    return crud_get(client, _ITEM, id, DupeDetectRule)


def create(client: Client, data) -> DupeDetectRule:
    """Create a new dupe detect rule.

    :param client: Ticketmatic API client.
    :param data: Dupe detect rule data
        (:class:`~ticketmatic.models.settings.DupeDetectRule` or dict).
    :returns: The created
        :class:`~ticketmatic.models.settings.DupeDetectRule`.
    """
    return crud_create(client, _URL, data, DupeDetectRule)


def update(client: Client, id: int, data) -> DupeDetectRule:
    """Modify an existing dupe detect rule.

    :param client: Ticketmatic API client.
    :param id: Dupe detect rule ID.
    :param data: Updated dupe detect rule data
        (:class:`~ticketmatic.models.settings.DupeDetectRule` or dict).
    :returns: The updated
        :class:`~ticketmatic.models.settings.DupeDetectRule`.
    """
    return crud_update(client, _ITEM, id, data, DupeDetectRule)


def delete(client: Client, id: int) -> None:
    """Remove a dupe detect rule.

    :param client: Ticketmatic API client.
    :param id: Dupe detect rule ID.
    """
    crud_delete(client, _ITEM, id)
