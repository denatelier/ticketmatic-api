"""Endpoint functions for report settings."""

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
from ticketmatic.models.settings import Report, ReportQuery

_URL = "/{accountname}/settings/system/reports"
_ITEM = "/{accountname}/settings/system/reports/{id}"
ReportsList = make_list_type(Report)
_FIELDS = ["filter", "lastupdatesince"]


def get_list(client: Client, params=None) -> ReportsList:
    """Get a list of reports.

    :param client: Ticketmatic API client.
    :param params: Optional query parameters
        (:class:`~ticketmatic.models.settings.ReportQuery`).
    :returns: A list of :class:`~ticketmatic.models.settings.Report` results.
    """
    return crud_get_list(client, _URL, ReportQuery, params, ReportsList, _FIELDS)


def get(client: Client, id: int) -> Report:
    """Get a single report.

    :param client: Ticketmatic API client.
    :param id: Report ID.
    :returns: The requested :class:`~ticketmatic.models.settings.Report`.
    """
    return crud_get(client, _ITEM, id, Report)


def create(client: Client, data) -> Report:
    """Create a new report.

    :param client: Ticketmatic API client.
    :param data: Report data
        (:class:`~ticketmatic.models.settings.Report` or dict).
    :returns: The created :class:`~ticketmatic.models.settings.Report`.
    """
    return crud_create(client, _URL, data, Report)


def update(client: Client, id: int, data) -> Report:
    """Modify an existing report.

    :param client: Ticketmatic API client.
    :param id: Report ID.
    :param data: Updated report data
        (:class:`~ticketmatic.models.settings.Report` or dict).
    :returns: The updated :class:`~ticketmatic.models.settings.Report`.
    """
    return crud_update(client, _ITEM, id, data, Report)


def delete(client: Client, id: int) -> None:
    """Remove a report.

    :param client: Ticketmatic API client.
    :param id: Report ID.
    """
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    """Fetch translatable fields.

    Returns a dictionary with string values in all languages for each
    translatable field.

    :param client: Ticketmatic API client.
    :param id: Report ID.
    :returns: Dictionary of translatable field values.
    """
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    """Update translations.

    Sets updated translation strings.

    :param client: Ticketmatic API client.
    :param id: Report ID.
    :param data: Translation strings to set.
    :returns: Updated dictionary of translatable field values.
    """
    return crud_translate(client, f"{_ITEM}/translate", id, data)
