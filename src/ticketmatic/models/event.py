"""Data models for events, event tickets, event locations, and related types."""

from __future__ import annotations

import dataclasses
from datetime import datetime
from typing import Any, ClassVar

from ticketmatic.models.base import Model
from ticketmatic.models.common import Layout
from ticketmatic.models.pricing import (
    EventPrices,
    PricelistPrices,
)


@dataclasses.dataclass
class EventContingentLock(Model):
    """Information about locked tickets in a contingent."""

    amount: int | None = None
    """Number of tickets in the contingent."""
    locktypeid: int | None = None
    """Lock type ID."""
    tickettypeid: int | None = None
    """Contingent ID."""


@dataclasses.dataclass
class EventContingent(Model):
    """Information about a contingent for an event."""

    id: int | None = None
    """Contingent ID."""
    name: str | None = None
    """Name of the contingent."""
    amount: int | None = None
    """Number of tickets in the contingent."""
    eventid: int | None = None
    """Event ID."""
    eventspecificprices: PricelistPrices | None = None
    """Event specific prices in addition to the prices defined in ``pricelistid``.

    Prices from the pricelist and the event specific prices are combined in one
    pricelist. The optional position attribute defines where the event specific
    prices will be positioned in the resulting pricelist.
    """
    locks: list[EventContingentLock] | None = None
    """Locked tickets for the contingent."""
    pricelistid: int | None = None
    """Price list ID for this contingent."""
    withimportedbarcodes: bool | None = None
    """Whether the barcodes for the tickets in this contingent were imported (true),
    or were generated internally (false).
    """


@dataclasses.dataclass
class EventContingentAvailability(Model):
    """Information about the availability of tickets for a contingent."""

    complimentary: int | None = None
    """Number of complimentary tickets."""
    free: int | None = None
    """Number of available tickets."""
    locked_hard: int | None = None
    """Number of locked tickets with a hard lock type."""
    locked_soft: int | None = None
    """Number of locked tickets with a soft lock type."""
    reserved: int | None = None
    """Number of tickets reserved in unconfirmed orders."""
    sold_paid: int | None = None
    """Number of tickets in confirmed orders that are completely paid."""
    sold_unpaid: int | None = None
    """Number of tickets in confirmed orders that are not completely paid."""
    tickettypeid: int | None = None
    """Contingent ID."""
    total: int | None = None
    """Total number of tickets in the contingent."""
    lastupdatets: datetime | None = None
    """Last updated timestamp."""


@dataclasses.dataclass
class EventPreview(Model):
    """Preview information for an event."""

    linkurl: str | None = None
    """Link URL."""
    previewimage: str | None = None
    """Link to preview image."""
    subtitle: str | None = None
    """Preview subtitle."""
    title: str | None = None
    """Preview title."""
    type: int | None = None
    """Preview type. Currently supported values are: itunes (30001), youtube (30002),
    soundcloud (30003).
    """
    url: str | None = None
    """Preview URL."""


@dataclasses.dataclass
class EventSalesChannel(Model):
    """Information about the sales period for a specific sales channel in an event."""

    eventid: int | None = None
    """Event ID."""
    haswaitinglist: bool | None = None
    """Whether or not this sales channel has a waiting list for this event."""
    isactive: bool | None = None
    """Whether or not this sales channel is active for this event."""
    saleendts: datetime | None = None
    """When the sales end."""
    saleschannelid: int | None = None
    """Sales channel ID."""
    salestartts: datetime | None = None
    """When the sales start."""


@dataclasses.dataclass
class EventSeatingplanContingent(Model):
    """Information about a contingent in the seating plan for an event."""

    id: int | None = None
    """Contingent ID."""
    name: str | None = None
    """Name of the contingent."""
    amount: int | None = None
    """Number of tickets in the contingent."""
    eventid: int | None = None
    """Event ID."""
    seatrankid: int | None = None
    """Seat rank ID."""


@dataclasses.dataclass
class Event(Model):
    """A single event.

    The ``currentstatus`` field can have any of the following values:

    * **Draft (``19001``)**
    * **Active (``19002``)**
    * **Closed (``19003``)**
    """

    _has_custom_fields: ClassVar[bool] = True

    id: int | None = None
    """Event ID.

    **Note:** Ignored when creating a new event.

    **Note:** Ignored when updating an existing event.
    """
    name: str | None = None
    """Event name."""
    audiopreviewurl: str | None = None
    """The audio preview URL for the event."""
    availability: list[EventContingentAvailability] | None = None
    """Information on the availability of tickets per contingent. Read-only.

    **Note:** Ignored when creating a new event.

    **Note:** Ignored when updating an existing event.
    """
    cancellationpolicy: list[str] | None = None
    """Cancellation policy."""
    code: str | None = None
    """Event code. Used as a unique identifier in web sales.

    **Note:** Ignored when creating a new event.

    **Note:** Ignored when updating an existing event.
    """
    contingents: list[EventContingent] | None = None
    """Information about the contingents in the event that are not in the
    seating plan.
    """
    currentstatus: int | None = None
    """Event status. The available values for this field can be found on the
    :class:`Event` page.
    """
    description: str | None = None
    """Description of the event, visible for ticket buyers."""
    endts: datetime | None = None
    """Event end time."""
    externalcode: str | None = None
    """External event code. This field is typically set when importing data from other
    systems.
    """
    image: str | None = None
    """The image URL for the event display image.

    **Note:** Ignored when creating a new event.

    **Note:** Ignored when updating an existing event.
    """
    info: str | None = None
    """Practical info for the event, visible for ticket buyers."""
    layout: Layout | None = None
    """Layout parameters for the event."""
    locationid: int | None = None
    """Event location ID. See event locations for more information."""
    locationname: str | None = None
    """Event location name. Automatically derived using ``locationid``.

    **Note:** Ignored when creating a new event.

    **Note:** Ignored when updating an existing event.
    """
    maxnbrofticketsperbasket: int | None = None
    """Maximum number of tickets for this event that can be added to a basket."""
    optinsetid: int | None = None
    """Opt-in set ID."""
    previews: list[EventPreview] | None = None
    """Preview URLs for the event."""
    prices: EventPrices | None = None
    """Information on the available prices for the event.

    **Note:** Ignored when creating a new event.

    **Note:** Ignored when updating an existing event.
    """
    productionid: int | None = None
    """Production ID."""
    publishedts: datetime | None = None
    """Event publish time.

    **Note:** Ignored when creating a new event.

    **Note:** Ignored when updating an existing event.
    """
    queuetoken: int | None = None
    """Queue ID."""
    revenuesplitid: int | None = None
    """DEPRECATED."""
    saleendts: datetime | None = None
    """Time of end of sales. Used for all sales channels for which no specific sales
    period has been defined.
    """
    saleschannels: list[EventSalesChannel] | None = None
    """Per-sales channel information about when this event is for sale."""
    salestartts: datetime | None = None
    """Time of start of sales. Used for all sales channels for which no specific sales
    period has been defined.
    """
    salestatusmessagesid: int | None = None
    """Sale status messages ID."""
    schedule: str | None = None
    """Schedule for the event, visible for ticket buyers."""
    seatallowsingle: bool | None = None
    """Allow or disallow leaving single seats on their own."""
    seated_chartkey: str | None = None
    """Chart key for the seated event layout."""
    seated_contingents: list[EventContingent] | None = None
    """Seated contingents."""
    seatingplancontingents: list[EventSeatingplanContingent] | None = None
    """Information about the contingents defined in the seating plan. Read-only.

    **Note:** Ignored when creating a new event.

    **Note:** Ignored when updating an existing event.
    """
    seatingplaneventspecificprices: PricelistPrices | None = None
    """Event specific prices in addition to the prices defined in
    ``seatingplanpricelistid``. Prices from the pricelist and the event specific
    prices are combined in one pricelist for the event. The optional position
    attribute defines where the event specific prices will be positioned in the
    resulting pricelist.
    """
    seatingplanid: int | None = None
    """Seating plan ID. Only set for events with fixed seats."""
    seatingplanlocktemplate: str | None = None
    """Name of the seating plan lock template to apply when linking a seating plan to
    this event. This is not a numeric ID but the name of the lock template as
    specified in the seating plan's logical plan.

    **Note:** Ignored when creating a new event.

    **Note:** Ignored when updating an existing event.
    """
    seatingplanpricelistid: int | None = None
    """Price list ID for fixed seats. Only set for events with fixed seats. See price
    lists for more information.
    """
    seatselection: bool | None = None
    """Enable or disable seat selection for customers."""
    segmentationtags: list[str] | None = None
    """Segmentation tags."""
    servicemailids: list[int] | None = None
    """Service mail IDs."""
    shortdescription: str | None = None
    """Short description of the event, visible for ticket buyers."""
    socialdistance: int | None = None
    """Social distance type. Determines if social distance must be practiced."""
    startts: datetime | None = None
    """Event start time."""
    subtitle: str | None = None
    """Event subtitle."""
    subtitle2: str | None = None
    """Event subtitle (2)."""
    tags: list[str] | None = None
    """Event tags."""
    ticketfeeid: int | None = None
    """Ticket fee ID. Determines which ticket fee rules are used for this event. See
    ticket fees for more information.
    """
    ticketinfoid: int | None = None
    """Ticket info ID."""
    ticketlayoutid: int | None = None
    """Ticket layout ID. See ticket layouts for more information."""
    totalmaxtickets: int | None = None
    """Determines the total maximum amount of tickets that can be sold for event."""
    translations: list[str] | None = None
    """Translation of event fields."""
    upsellid: int | None = None
    """Upsell ID."""
    waitinglisttype: int | None = None
    """The type of the waiting list the event uses."""
    webremark: str | None = None
    """Small description that will be shown on the sales pages of this event."""
    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new event.

    **Note:** Ignored when updating an existing event.
    """
    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new event.

    **Note:** Ignored when updating an existing event.
    """
    custom_fields: dict[str, Any] | None = None
    """Custom field values keyed by name (``c_``-prefixed in the API)."""


@dataclasses.dataclass
class EventContext(Model):
    """Used when requesting events, to restrict the event information to a specific
    context.

    Currently allows you to filter the event information (both the events and the
    pricing information within each event) to a specific sales channel. If a sales
    channel is specified, only events that are **currently** for sale in that specific
    sales channel will be returned.
    """

    saleschannelid: int | None = None
    """The ID of the sales channel used to restrict the event information."""


@dataclasses.dataclass
class EventFilter(Model):
    """Used when requesting events, to filter events. Currently allows you to filter
    based on the production ID.
    """

    productionid: int | None = None
    """The ID of the production."""
    status: list[int] | None = None
    """The event status. By default, events with status Active or Closed will be
    returned.
    """


@dataclasses.dataclass
class EventQuery(Model):
    """Filter parameters to fetch a list of events."""

    context: EventContext | None = None
    """Restrict the event information to a specific context.

    Currently allows you to filter the event information (both the events and the
    pricing information within each event) to a specific sales channel. This makes it
    very easy to show the correct information on a website.
    """
    filter: str | None = None
    """A SQL query that returns event IDs. Can be used to do arbitrary filtering. See
    the database documentation for event for more information.
    """
    lastupdatesince: datetime | None = None
    """Only include events that have been updated since the given timestamp."""
    limit: int | None = None
    """Limit results to at most the given amount of events."""
    offset: int | None = None
    """Skip the first X events."""
    orderby: str | None = None
    """Order by the given field. Supported values: ``name``, ``startts``."""
    output: str | None = None
    """Output format.

    Possible values:

    * **ids**: Only fill the ID field.
    * **default**: Return all event fields (also used when the output parameter is
      omitted).
    * **withlookup**: Returns all event fields and an additional ``lookup`` field
      which contains all dependent objects.
    """
    searchterm: str | None = None
    """A text filter string. Matches against the start of the event name, the
    production name or the subtitle.
    """
    simplefilter: EventFilter | None = None
    """Filters the events based on a given set of fields. Currently supports:
    ``productionid``, ``status`` and ``pricetypeids``.
    """


@dataclasses.dataclass
class EventLockTickets(Model):
    """Used when locking a set of tickets. Contains the lock type ID and the set of
    ticket IDs.
    """

    locktypeid: int | None = None
    """ID of the lock type to use for the lock."""
    ticketids: list[int] | None = None
    """Array of ticket IDs to lock."""


@dataclasses.dataclass
class EventUnlockTickets(Model):
    """Used when unlocking a set of tickets."""

    ticketids: list[int] | None = None
    """Array of ticket IDs to unlock."""


@dataclasses.dataclass
class EventUpdateSeatRankForTickets(Model):
    """Used when updating the seat rank for a set of tickets."""

    seatrankid: int | None = None
    """The seat rank."""
    ticketids: list[int] | None = None
    """Array of ticket IDs to update."""


@dataclasses.dataclass
class EventScanTicketsOut(Model):
    """Scan out all tickets that are scanned in."""

    tickettypeids: list[int] | None = None
    """Array of ticket type IDs."""


@dataclasses.dataclass
class EventTicketFilter(Model):
    """Used when requesting tickets for an event, to filter the tickets."""

    tickettypeid: int | None = None
    """The ID of the ticket type (contingent)."""


@dataclasses.dataclass
class EventTicketQuery(Model):
    """Filter parameters to fetch a list of tickets for an event."""

    simplefilter: EventTicketFilter | None = None
    """Filters the tickets based on a given set of fields."""


@dataclasses.dataclass
class EventTicket(Model):
    """A single ticket."""

    _has_custom_fields: ClassVar[bool] = True

    id: int | None = None
    """Ticket ID."""
    orderid: int | None = None
    """Link to the order the ticket is contained in.

    **Note:** Ignored when updating tickets.
    """
    accesscontrollastenteredscandeviceid: int | None = None
    """The ID of the scanner used for the last successful entry.

    **Note:** Ignored when updating tickets.
    """
    accesscontrollastenteredts: datetime | None = None
    """The timestamp of the last successful entry with this ticket.

    **Note:** Ignored when updating tickets.
    """
    accesscontrollastexitscandeviceid: int | None = None
    """The ID of the scanner used for the last successful exit.

    **Note:** Ignored when updating tickets.
    """
    accesscontrollastexitts: datetime | None = None
    """The timestamp of the last successful exit with this ticket.

    **Note:** Ignored when updating tickets.
    """
    accesscontrolstatus: int | None = None
    """The access control status for this ticket. 0 means not scanned, 1 means
    successful entry, 2 means successful exit.

    **Note:** Ignored when updating tickets.
    """
    barcode: str | None = None
    """Ticket barcode."""
    bundleid: int | None = None
    """Link to the bundle (order product) that this ticket belongs to.

    **Note:** Ignored when updating tickets.
    """
    locktypeid: int | None = None
    """Link to the lock type used for locking the ticket.

    **Note:** Ignored when updating tickets.
    """
    orderfee: float | None = None
    """Fee for the ticket in the order.

    **Note:** Ignored when updating tickets.
    """
    price: float | None = None
    """Price for the ticket in the order (without fee).

    **Note:** Ignored when updating tickets.
    """
    properties: list[str] | None = None
    """String to string key-value mapping of properties."""
    seatdescription: str | None = None
    """The seat description for this ticket (only for seated tickets).

    **Note:** Ignored when updating tickets.
    """
    seatid: str | None = None
    """Seat ID (for seated tickets).

    **Note:** Ignored when updating tickets.
    """
    seatpriority: int | None = None
    """Number indicating the priority for this ticket for the best available algorithm.
    Tickets with a higher priority will be considered first when performing a best
    available allocation.

    **Note:** Ignored when updating tickets.
    """
    seatrownumber: str | None = None
    """Row number for the ticket (only for seated tickets).

    **Note:** Ignored when updating tickets.
    """
    seatseatnumber: str | None = None
    """Seat number for the ticket (only for seated tickets).

    **Note:** Ignored when updating tickets.
    """
    seatzoneid: int | None = None
    """Optional seat zone for the ticket.

    **Note:** Ignored when updating tickets.
    """
    seatzonename: str | None = None
    """Zone name for the ticket (only for seated tickets).

    **Note:** Ignored when updating tickets.
    """
    ticketholderid: int | None = None
    """Optional link to the contact that is the ticket holder for this ticket.

    **Note:** Ignored when updating tickets.
    """
    ticketname: str | None = None
    """Optional name on the ticket.

    **Note:** Ignored when updating tickets.
    """
    tickettypeid: int | None = None
    """Link to the contingent this ticket belongs to.

    **Note:** Ignored when updating tickets.
    """
    tickettypepriceid: int | None = None
    """Link to the ticket type price that is assigned to this ticket for the order.
    Through the ticket type price you can retrieve the price type.

    **Note:** Ignored when updating tickets.
    """
    vouchercodeid: int | None = None
    """Link to the voucher code that was used to reserve this ticket.

    **Note:** Ignored when updating tickets.
    """
    custom_fields: dict[str, Any] | None = None
    """Custom field values keyed by name (``c_``-prefixed in the API)."""


@dataclasses.dataclass
class EventUpsellitem(Model):
    """Upsell items for the event."""

    id: int | None = None
    """ID of the linked item."""
    type: str | None = None
    """Upsell item type. Currently supported values are: event, product."""


@dataclasses.dataclass
class EventLocation(Model):
    """A single event location."""

    _has_custom_fields: ClassVar[bool] = True

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new event location.

    **Note:** Ignored when updating an existing event location.
    """
    name: str | None = None
    """Name of the location."""
    city: str | None = None
    """City."""
    countrycode: str | None = None
    """Country code. Should be an ISO 3166-1 alpha-2 two-letter code."""
    geostatus: int | None = None
    """Geocode status for the address of this location."""
    info: str | None = None
    """Practical info on the event location (route description, public transport,
    parking, ...).
    """
    lat: float | None = None
    """Latitude coordinate for the event location.

    **Note:** Ignored when creating a new event location.

    **Note:** Ignored when updating an existing event location.
    """
    long: float | None = None
    """Longitude coordinate for the event location.

    **Note:** Ignored when creating a new event location.

    **Note:** Ignored when updating an existing event location.
    """
    state: str | None = None
    """State."""
    street1: str | None = None
    """Street name."""
    street2: str | None = None
    """Number and box."""
    street3: str | None = None
    """Additional address line 3."""
    street4: str | None = None
    """Additional address line 4."""
    zip: str | None = None
    """Zip code."""
    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new event location.

    **Note:** Ignored when updating an existing event location.
    """
    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new event location.

    **Note:** Ignored when updating an existing event location.
    """
    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new event location.

    **Note:** Ignored when updating an existing event location.
    """
    custom_fields: dict[str, Any] | None = None
    """Custom field values keyed by name (``c_``-prefixed in the API)."""


@dataclasses.dataclass
class EventLocationQuery(Model):
    """Set of parameters used to filter event locations."""

    filter: str | None = None
    """Filter the returned items by specifying a query on the public data model that
    returns the IDs.
    """
    includearchived: bool | None = None
    """If this parameter is true, archived items will be returned as well."""
    lastupdatesince: datetime | None = None
    """All items that were updated since this timestamp will be returned. Timestamp
    should be passed in ``YYYY-MM-DD hh:mm:ss`` format.
    """


# --- Batch event operations ---


@dataclasses.dataclass
class BatchEventUpdateField(Model):
    """Field to update on an event."""

    key: str | None = None
    """The name of the field. Can either be a custom field or one of the following
    fixed fields (``name``, ``subtitle``, ``webremark``, ``startts``, ``endts``,
    ``locationid``, ``ticketlayoutid``, ``seatselection``).
    """
    updatetype: str | None = None
    """The type of update to perform on the field. Can either be ``set`` (default),
    ``add`` or ``remove`` when used in combination with multi-value fields.
    """
    value: Any | None = None
    """The value of the field."""


@dataclasses.dataclass
class BatchEventParameters(Model):
    """Parameters for batch operations performed on events."""

    updatefields: list[BatchEventUpdateField] | None = None
    """Set of fields to update, used for operation ``update``. Custom fields are also
    supported.
    """


@dataclasses.dataclass
class BatchEventOperation(Model):
    """Batch operations performed on events."""

    ids: list[int] | None = None
    """Restrict operation to supplied IDs. If these IDs are not specified, **all**
    events are updated.
    """
    operation: str | None = None
    """Operation to perform. Possible values are: ``duplicate``, ``publish``,
    ``delete``, ``close``, ``update``, ``redraft``, ``reopen``.
    """
    parameters: BatchEventParameters | None = None
    """Operation-specific parameters."""
