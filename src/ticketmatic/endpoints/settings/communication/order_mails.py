"""Endpoint functions for order mail templates."""

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
from ticketmatic.models.order import OrderMailTemplate, OrderMailTemplateQuery

_URL = "/{accountname}/settings/communicationanddesign/ordermails"
_ITEM = "/{accountname}/settings/communicationanddesign/ordermails/{id}"
OrderMailsList = make_list_type(OrderMailTemplate)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(
    client: Client, params: OrderMailTemplateQuery | dict | None = None
) -> OrderMailsList:
    """Get a list of order mail templates.

    :param client: Ticketmatic API client.
    :param params: Optional filter/query parameters.
    :returns: An :class:`~ticketmatic.models.order.OrderMailTemplate` list result.
    """
    return crud_get_list(
        client, _URL, OrderMailTemplateQuery, params, OrderMailsList, _FIELDS
    )


def get(client: Client, id: int) -> OrderMailTemplate:
    """Get a single order mail template.

    :param client: Ticketmatic API client.
    :param id: Order mail template ID.
    :returns: The requested :class:`~ticketmatic.models.order.OrderMailTemplate`.
    """
    return crud_get(client, _ITEM, id, OrderMailTemplate)


def create(client: Client, data: OrderMailTemplate | dict) -> OrderMailTemplate:
    """Create a new order mail template.

    :param client: Ticketmatic API client.
    :param data: Order mail template data to create.
    :returns: The created :class:`~ticketmatic.models.order.OrderMailTemplate`.
    """
    return crud_create(client, _URL, data, OrderMailTemplate)


def update(
    client: Client, id: int, data: OrderMailTemplate | dict
) -> OrderMailTemplate:
    """Modify an existing order mail template.

    :param client: Ticketmatic API client.
    :param id: Order mail template ID.
    :param data: Updated order mail template data.
    :returns: The updated :class:`~ticketmatic.models.order.OrderMailTemplate`.
    """
    return crud_update(client, _ITEM, id, data, OrderMailTemplate)


def delete(client: Client, id: int) -> None:
    """Remove an order mail template.

    Order mail templates are archivable: this call will mark the object as
    archived rather than deleting it from the database.

    :param client: Ticketmatic API client.
    :param id: Order mail template ID.
    """
    crud_delete(client, _ITEM, id)
