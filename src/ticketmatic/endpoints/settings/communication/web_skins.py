"""Endpoint functions for web sales skins."""

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
from ticketmatic.models.ticket import WebSalesSkin, WebSalesSkinQuery

_URL = "/{accountname}/settings/communicationanddesign/webskins"
_ITEM = "/{accountname}/settings/communicationanddesign/webskins/{id}"
WebSkinsList = make_list_type(WebSalesSkin)
_FIELDS = ["filter", "lastupdatesince"]


def get_list(
    client: Client, params: WebSalesSkinQuery | dict | None = None
) -> WebSkinsList:
    """Get a list of web sales skins.

    :param client: Ticketmatic API client.
    :param params: Optional filter/query parameters.
    :returns: A :class:`~ticketmatic.models.ticket.WebSalesSkin` list result.
    """
    return crud_get_list(client, _URL, WebSalesSkinQuery, params, WebSkinsList, _FIELDS)


def get(client: Client, id: int) -> WebSalesSkin:
    """Get a single web sales skin.

    :param client: Ticketmatic API client.
    :param id: Web sales skin ID.
    :returns: The requested :class:`~ticketmatic.models.ticket.WebSalesSkin`.
    """
    return crud_get(client, _ITEM, id, WebSalesSkin)


def create(client: Client, data: WebSalesSkin | dict) -> WebSalesSkin:
    """Create a new web sales skin.

    :param client: Ticketmatic API client.
    :param data: Web sales skin data to create.
    :returns: The created :class:`~ticketmatic.models.ticket.WebSalesSkin`.
    """
    return crud_create(client, _URL, data, WebSalesSkin)


def update(client: Client, id: int, data: WebSalesSkin | dict) -> WebSalesSkin:
    """Modify an existing web sales skin.

    :param client: Ticketmatic API client.
    :param id: Web sales skin ID.
    :param data: Updated web sales skin data.
    :returns: The updated :class:`~ticketmatic.models.ticket.WebSalesSkin`.
    """
    return crud_update(client, _ITEM, id, data, WebSalesSkin)


def delete(client: Client, id: int) -> None:
    """Remove a web sales skin.

    :param client: Ticketmatic API client.
    :param id: Web sales skin ID.
    """
    crud_delete(client, _ITEM, id)
