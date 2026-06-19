"""Endpoint functions for managing ticket fee schemes."""

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
from ticketmatic.models.pricing import TicketFee, TicketFeeQuery

_URL = "/{accountname}/settings/pricing/ticketfees"
_ITEM = "/{accountname}/settings/pricing/ticketfees/{id}"
TicketFeesList = make_list_type(TicketFee)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(
    client: Client, params: TicketFeeQuery | dict | None = None
) -> TicketFeesList:
    """Get a list of ticket fees.

    :param client: Ticketmatic API client.
    :param params: Optional query/filter parameters.
    :returns: A list of :class:`~ticketmatic.models.pricing.TicketFee` objects.
    """
    return crud_get_list(client, _URL, TicketFeeQuery, params, TicketFeesList, _FIELDS)


def get(client: Client, id: int) -> TicketFee:
    """Get a single ticket fee.

    :param client: Ticketmatic API client.
    :param id: Ticket fee ID.
    :returns: The requested :class:`~ticketmatic.models.pricing.TicketFee`.
    """
    return crud_get(client, _ITEM, id, TicketFee)


def create(client: Client, data: TicketFee | dict) -> TicketFee:
    """Create a new ticket fee.

    :param client: Ticketmatic API client.
    :param data: Ticket fee data.
    :returns: The created :class:`~ticketmatic.models.pricing.TicketFee`.
    """
    return crud_create(client, _URL, data, TicketFee)


def update(client: Client, id: int, data: TicketFee | dict) -> TicketFee:
    """Modify an existing ticket fee.

    :param client: Ticketmatic API client.
    :param id: Ticket fee ID.
    :param data: Updated ticket fee data.
    :returns: The updated :class:`~ticketmatic.models.pricing.TicketFee`.
    """
    return crud_update(client, _ITEM, id, data, TicketFee)


def delete(client: Client, id: int) -> None:
    """Remove a ticket fee.

    Ticket fees are archivable: this call won't actually delete the object
    from the database. Instead, it will mark the object as archived, which
    means it won't show up anymore in most places.

    :param client: Ticketmatic API client.
    :param id: Ticket fee ID.
    """
    crud_delete(client, _ITEM, id)
