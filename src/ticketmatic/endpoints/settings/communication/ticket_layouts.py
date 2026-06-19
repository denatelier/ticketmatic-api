"""Endpoint functions for ticket layouts and ticket layout templates."""

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
from ticketmatic.models.ticket import (
    TicketLayout,
    TicketLayoutQuery,
    TicketLayoutTemplate,
    TicketLayoutTemplateQuery,
)

_URL = "/{accountname}/settings/communicationanddesign/ticketlayouts"
_ITEM = "/{accountname}/settings/communicationanddesign/ticketlayouts/{id}"
TicketLayoutsList = make_list_type(TicketLayout)

_TPL_URL = "/{accountname}/settings/communicationanddesign/ticketlayouttemplates"
_TPL_ITEM = "/{accountname}/settings/communicationanddesign/ticketlayouttemplates/{id}"
TicketLayoutTemplatesList = make_list_type(TicketLayoutTemplate)

_FIELDS = ["typeid", "filter", "includearchived", "lastupdatesince"]


def get_list(
    client: Client, params: TicketLayoutQuery | dict | None = None
) -> TicketLayoutsList:
    """Get a list of ticket layouts.

    :param client: Ticketmatic API client.
    :param params: Optional filter/query parameters.
    :returns: A :class:`~ticketmatic.models.ticket.TicketLayout` list result.
    """
    return crud_get_list(
        client, _URL, TicketLayoutQuery, params, TicketLayoutsList, _FIELDS
    )


def get(client: Client, id: int) -> TicketLayout:
    """Get a single ticket layout.

    :param client: Ticketmatic API client.
    :param id: Ticket layout ID.
    :returns: The requested :class:`~ticketmatic.models.ticket.TicketLayout`.
    """
    return crud_get(client, _ITEM, id, TicketLayout)


def create(client: Client, data: TicketLayout | dict) -> TicketLayout:
    """Create a new ticket layout.

    :param client: Ticketmatic API client.
    :param data: Ticket layout data to create.
    :returns: The created :class:`~ticketmatic.models.ticket.TicketLayout`.
    """
    return crud_create(client, _URL, data, TicketLayout)


def update(client: Client, id: int, data: TicketLayout | dict) -> TicketLayout:
    """Modify an existing ticket layout.

    :param client: Ticketmatic API client.
    :param id: Ticket layout ID.
    :param data: Updated ticket layout data.
    :returns: The updated :class:`~ticketmatic.models.ticket.TicketLayout`.
    """
    return crud_update(client, _ITEM, id, data, TicketLayout)


def delete(client: Client, id: int) -> None:
    """Remove a ticket layout.

    Ticket layouts are archivable: this call will mark the object as archived
    rather than deleting it from the database.

    :param client: Ticketmatic API client.
    :param id: Ticket layout ID.
    """
    crud_delete(client, _ITEM, id)


# Templates
def templates_get_list(
    client: Client, params: TicketLayoutTemplateQuery | dict | None = None
) -> TicketLayoutTemplatesList:
    """Get a list of ticket layout templates.

    :param client: Ticketmatic API client.
    :param params: Optional filter/query parameters.
    :returns: A :class:`~ticketmatic.models.ticket.TicketLayoutTemplate` list
        result.
    """
    return crud_get_list(
        client,
        _TPL_URL,
        TicketLayoutTemplateQuery,
        params,
        TicketLayoutTemplatesList,
        _FIELDS,
    )


def templates_get(client: Client, id: int) -> TicketLayoutTemplate:
    """Get a single ticket layout template.

    :param client: Ticketmatic API client.
    :param id: Ticket layout template ID.
    :returns: The requested
        :class:`~ticketmatic.models.ticket.TicketLayoutTemplate`.
    """
    return crud_get(client, _TPL_ITEM, id, TicketLayoutTemplate)


def templates_create(
    client: Client, data: TicketLayoutTemplate | dict
) -> TicketLayoutTemplate:
    """Create a new ticket layout template.

    :param client: Ticketmatic API client.
    :param data: Ticket layout template data to create.
    :returns: The created
        :class:`~ticketmatic.models.ticket.TicketLayoutTemplate`.
    """
    return crud_create(client, _TPL_URL, data, TicketLayoutTemplate)


def templates_update(
    client: Client, id: int, data: TicketLayoutTemplate | dict
) -> TicketLayoutTemplate:
    """Modify an existing ticket layout template.

    :param client: Ticketmatic API client.
    :param id: Ticket layout template ID.
    :param data: Updated ticket layout template data.
    :returns: The updated
        :class:`~ticketmatic.models.ticket.TicketLayoutTemplate`.
    """
    return crud_update(client, _TPL_ITEM, id, data, TicketLayoutTemplate)


def templates_delete(client: Client, id: int) -> None:
    """Remove a ticket layout template.

    Ticket layout templates are archivable: this call will mark the object as
    archived rather than deleting it from the database.

    :param client: Ticketmatic API client.
    :param id: Ticket layout template ID.
    """
    crud_delete(client, _TPL_ITEM, id)
