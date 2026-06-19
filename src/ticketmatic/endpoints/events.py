"""Endpoint functions for the Ticketmatic events API."""

from __future__ import annotations

import dataclasses
from typing import Any

from ticketmatic.client import Client
from ticketmatic.json_utils import unpack_array
from ticketmatic.models.event import (
    BatchEventOperation,
    Event,
    EventLockTickets,
    EventQuery,
    EventScanTicketsOut,
    EventTicket,
    EventTicketQuery,
    EventUnlockTickets,
    EventUpdateSeatRankForTickets,
)
from ticketmatic.stream import Stream


@dataclasses.dataclass
class EventsList:
    """Paged list result returned by :func:`get_list`."""

    data: list[Event]
    """Result data — the list of :class:`~ticketmatic.models.event.Event` objects."""

    nbrofresults: int
    """Total number of results available without considering limit and offset,
    useful for paging.
    """

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> EventsList:
        """Construct an :class:`EventsList` from a raw API response dictionary."""
        return cls(
            data=unpack_array(Event, data.get("data", [])),
            nbrofresults=int(data.get("nbrofresults", 0)),
        )


def get_list(client: Client, params: EventQuery | dict | None = None) -> EventsList:
    """Get a list of events.

    :param client: Ticketmatic API client.
    :param params: Optional query/filter parameters.
    :returns: A :class:`EventsList` containing the matching events.
    """
    if params is None or isinstance(params, dict):
        params = EventQuery.from_dict(params or {})
    req = client.new_request("GET", "/{accountname}/events")
    req.add_query("context", params.context)
    req.add_query("filter", params.filter)
    req.add_query("lastupdatesince", params.lastupdatesince)
    req.add_query("limit", params.limit)
    req.add_query("offset", params.offset)
    req.add_query("orderby", params.orderby)
    req.add_query("output", params.output)
    req.add_query("searchterm", params.searchterm)
    req.add_query("simplefilter", params.simplefilter)
    return EventsList.from_dict(req.run())


def get(client: Client, id: int) -> Event:
    """Get a single event.

    :param client: Ticketmatic API client.
    :param id: Event ID.
    :returns: The requested :class:`~ticketmatic.models.event.Event`.
    """
    req = client.new_request("GET", "/{accountname}/events/{id}")
    req.add_parameter("id", id)
    return Event.from_dict(req.run())


def create(client: Client, data: Event | dict) -> Event:
    """Create a new event.

    :param client: Ticketmatic API client.
    :param data: Event data to create.
    :returns: The created :class:`~ticketmatic.models.event.Event`.
    """
    if isinstance(data, dict):
        data = Event.from_dict(data)
    req = client.new_request("POST", "/{accountname}/events")
    req.set_body(data.to_dict())
    return Event.from_dict(req.run())


def update(client: Client, id: int, data: Event | dict) -> Event:
    """Update an event.

    :param client: Ticketmatic API client.
    :param id: Event ID.
    :param data: Updated event data.
    :returns: The updated :class:`~ticketmatic.models.event.Event`.
    """
    if isinstance(data, dict):
        data = Event.from_dict(data)
    req = client.new_request("PUT", "/{accountname}/events/{id}")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Event.from_dict(req.run())


def batch(client: Client, data: BatchEventOperation | dict) -> None:
    """Apply batch operations to a set of events.

    The parameters required are specific to the type of operation. The
    operation will be applied to the events with given IDs. The amount of
    IDs is limited to 1000 per call.

    Supported operations: ``duplicate``, ``publish``, ``redraft``,
    ``close``, ``reopen``, ``delete``, and ``update``.

    :param client: Ticketmatic API client.
    :param data: Batch operation to apply.
    """
    if isinstance(data, dict):
        data = BatchEventOperation.from_dict(data)
    req = client.new_request("POST", "/{accountname}/events/batch")
    req.set_body(data.to_dict())
    req.run()


def delete(client: Client, id: int) -> None:
    """Delete an event.

    :param client: Ticketmatic API client.
    :param id: Event ID.
    """
    req = client.new_request("DELETE", "/{accountname}/events/{id}")
    req.add_parameter("id", id)
    req.run()


def get_tickets(
    client: Client, id: int, params: EventTicketQuery | dict | None = None
) -> Stream:
    """Get all tickets for an event.

    Returns the list of all tickets that are part of this event.

    :param client: Ticketmatic API client.
    :param id: Event ID.
    :param params: Optional query/filter parameters.
    :returns: A :class:`~ticketmatic.stream.Stream` of event tickets.
    """
    if params is None or isinstance(params, dict):
        params = EventTicketQuery.from_dict(params or {})
    req = client.new_request("GET", "/{accountname}/events/{id}/tickets")
    req.add_parameter("id", id)
    req.add_query("simplefilter", params.simplefilter)
    return req.stream()


def batch_update_tickets(
    client: Client, id: int, data: list[EventTicket | dict]
) -> None:
    """Batch update tickets for an event.

    Update the contents of one or more custom fields for multiple tickets
    in one call. Batch update is limited to 5000 tickets per call.

    **Warning:** Do not change the barcode of a ticket that has been
    delivered: existing printed tickets will no longer work.

    :param client: Ticketmatic API client.
    :param id: Event ID.
    :param data: List of ticket updates to apply.
    """
    body = []
    for item in data:
        if isinstance(item, dict):
            item = EventTicket.from_dict(item)
        body.append(item.to_dict())
    req = client.new_request("PUT", "/{accountname}/events/{id}/tickets/batch")
    req.add_parameter("id", id)
    req.set_body(body)
    req.run()


def lock_tickets(client: Client, id: int, data: EventLockTickets | dict) -> None:
    """Lock a set of tickets.

    The lock call is limited to 100 tickets per call.

    :param client: Ticketmatic API client.
    :param id: Event ID.
    :param data: Lock request parameters.
    """
    if isinstance(data, dict):
        data = EventLockTickets.from_dict(data)
    req = client.new_request("PUT", "/{accountname}/events/{id}/tickets/lock")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    req.run()


def unlock_tickets(client: Client, id: int, data: EventUnlockTickets | dict) -> None:
    """Unlock a set of tickets.

    The unlock call is limited to 100 tickets per call.

    :param client: Ticketmatic API client.
    :param id: Event ID.
    :param data: Unlock request parameters.
    """
    if isinstance(data, dict):
        data = EventUnlockTickets.from_dict(data)
    req = client.new_request("PUT", "/{accountname}/events/{id}/tickets/unlock")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    req.run()


def update_seat_rank_for_tickets(
    client: Client, id: int, data: EventUpdateSeatRankForTickets | dict
) -> None:
    """Update the seat rank for a set of tickets.

    Updates the seat rank for tickets; works only for active events.

    :param client: Ticketmatic API client.
    :param id: Event ID.
    :param data: Seat rank update parameters.
    """
    if isinstance(data, dict):
        data = EventUpdateSeatRankForTickets.from_dict(data)
    req = client.new_request("PUT", "/{accountname}/events/{id}/tickets/seatrank")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    req.run()


def scan_tickets_out(client: Client, id: int, data: EventScanTicketsOut | dict) -> Any:
    """Scan out tickets that are scanned in.

    Scan out tickets that are scanned in; filter on ticket type ID if
    needed.

    :param client: Ticketmatic API client.
    :param id: Event ID.
    :param data: Scan-out request parameters.
    :returns: List of ticket IDs that were scanned out.
    """
    if isinstance(data, dict):
        data = EventScanTicketsOut.from_dict(data)
    req = client.new_request("PUT", "/{accountname}/events/{id}/tickets/scanout")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return req.run()


def translations(client: Client, id: int) -> Any:
    """Fetch translatable fields.

    Returns a dictionary with string values in all languages for each
    translatable field.

    :param client: Ticketmatic API client.
    :param id: Event ID.
    :returns: Dictionary of translatable field values keyed by language.
    """
    req = client.new_request("GET", "/{accountname}/events/{id}/translate")
    req.add_parameter("id", id)
    return req.run()


def translate(client: Client, id: int, data: dict) -> Any:
    """Update translations.

    :param client: Ticketmatic API client.
    :param id: Event ID.
    :param data: Dictionary of translation strings to update.
    :returns: Updated dictionary of translatable field values.
    """
    req = client.new_request("PUT", "/{accountname}/events/{id}/translate")
    req.add_parameter("id", id)
    req.set_body(data)
    return req.run()


def purge(client: Client, id: int) -> None:
    """Purge an event.

    :param client: Ticketmatic API client.
    :param id: Event ID.
    """
    req = client.new_request("PUT", "/{accountname}/events/{id}/purge")
    req.add_parameter("id", id)
    req.run()


def save_image(client: Client, id: int, data: bytes) -> Any:
    """Save an image for an event.

    :param client: Ticketmatic API client.
    :param id: Event ID.
    :param data: Raw JPEG image bytes.
    :returns: URL of the saved image.
    """
    req = client.new_request("POST", "/{accountname}/events/{id}/image")
    req.add_parameter("id", id)
    req.set_body(data, "jpg")
    return req.run()


def delete_image(client: Client, id: int) -> None:
    """Delete the event image.

    :param client: Ticketmatic API client.
    :param id: Event ID.
    """
    req = client.new_request("DELETE", "/{accountname}/events/{id}/image")
    req.add_parameter("id", id)
    req.run()
