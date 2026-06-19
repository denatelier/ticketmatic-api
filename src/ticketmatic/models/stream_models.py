"""Data models for event streams, subscribers, and waiting list requests."""

from __future__ import annotations

import dataclasses
from datetime import datetime
from typing import Any, ClassVar

from ticketmatic.models.base import Model


@dataclasses.dataclass
class EventstreamItem(Model):
    """Results of polling the stream."""

    id: str | None = None
    """Id of the event."""
    data: Any | None = None
    """Eventstream data."""
    ts: str | None = None
    """ISO-8601 timestamp of the event."""
    type: str | None = None
    """Eventstream item type."""


@dataclasses.dataclass
class EventstreamRequest(Model):
    """Parameters for requesting eventstream events."""

    id: str | None = None
    """Minimum id to start reading the stream."""
    eventtypes: str | None = None
    """Comma separated list of event types to filter on."""
    ts: str | None = None
    """Timestamp in ISO-8601 format to start reading the stream, mutually
    exclusive with the id.
    """


@dataclasses.dataclass
class EventstreamResult(Model):
    """Result of polling the eventstream."""

    moreresults: bool | None = None
    """The stream possibly contains more events, polling might need to catch up."""
    nextid: str | None = None
    """Id to use as startid in next poll."""
    results: list[EventstreamItem] | None = None
    """The results of polling the stream."""


@dataclasses.dataclass
class SubscriberCommunication(Model):
    """A newly created communication."""

    name: str | None = None
    """Name of the communication."""
    addresses: list[str] | None = None
    """E-mail addresses to which the communication has been sent."""
    remark: str | None = None
    """Optional description of the communication."""
    ts: datetime | None = None
    """Timestamp for the communication."""


@dataclasses.dataclass
class SubscriberSync(Model):
    """A subscriber record to sync state back to Ticketmatic."""

    email: str | None = None
    """Subscriber e-mail."""
    firstname: str | None = None
    """Subscriber first name."""
    lastname: str | None = None
    """Subscriber last name."""
    oldemail: str | None = None
    """Previous value of the ``email`` field, to indicate a changed e-mail
    address.

    Used to find the correct contact. The normal ``email`` field will be used
    when this field is omitted or empty.
    """
    subscribed: bool | None = None
    """Whether or not the subscriber is still subscribed."""


# --- Waiting List ---


@dataclasses.dataclass
class WaitingListRequestItemTicket(Model):
    """A ticket requested in a waitinglistrequestitem."""

    tickettypepriceid: int | None = None
    """The tickettypepriceid of the ticket."""


@dataclasses.dataclass
class WaitingListRequestItem(Model):
    """A waitinglistrequestitem is a single event and the requested tickets
    in a waitinglistrequest.
    """

    _has_custom_fields: ClassVar[bool] = True

    eventid: int | None = None
    """The event for which there are tickets requested."""
    tickets: list[WaitingListRequestItemTicket] | None = None
    """The requested tickets for the event, identified by tickettypepriceid."""
    custom_fields: dict[str, Any] | None = None
    """Custom field values keyed by name (``c_``-prefixed in the API)."""


@dataclasses.dataclass
class WaitingListRequest(Model):
    """A single waiting list request."""

    _has_custom_fields: ClassVar[bool] = True

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new waiting list request.

    **Note:** Ignored when updating an existing waiting list request.
    """
    orderid: int | None = None
    """The id of the order the request is converted to."""
    contactid: int | None = None
    """Contact id."""
    itemsstatus: int | None = None
    """Show the status of the related items, ``29101`` = no information
    provided, ``29102`` = partial information provided and ``29103`` = full
    information provided.
    """
    requeststatus: int | None = None
    """Show the status of the request, ``29201`` = requested, ``29202`` =
    processed, ``29203`` = conversion in progress.
    """
    saleschannelid: int | None = None
    """The id of the saleschannel used to make the request."""
    sortorder: int | None = None
    """Randomly generated identifier on create, provides random but consistent
    ordering of the request (for casting lots).

    **Note:** Ignored when updating an existing waiting list request.
    """
    waitinglistrequestitems: list[WaitingListRequestItem] | None = None
    """The request items per event.

    **Note:** Not set when retrieving a list of waiting list requests.
    """
    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new waiting list request.

    **Note:** Ignored when updating an existing waiting list request.
    """
    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new waiting list request.

    **Note:** Ignored when updating an existing waiting list request.
    """
    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new waiting list request.

    **Note:** Ignored when updating an existing waiting list request.
    """
    custom_fields: dict[str, Any] | None = None
    """Custom field values keyed by name (``c_``-prefixed in the API)."""


@dataclasses.dataclass
class WaitingListRequestQuery(Model):
    """Set of parameters used to filter waiting list requests."""

    filter: str | None = None
    """Filter the returned items by specifying a query on the public datamodel
    that returns the ids.
    """
    includearchived: bool | None = None
    """If this parameter is true, archived items will be returned as well."""
    lastupdatesince: datetime | None = None
    """All items that were updated since this timestamp will be returned.
    Timestamp should be passed in ``YYYY-MM-DD hh:mm:ss`` format.
    """
