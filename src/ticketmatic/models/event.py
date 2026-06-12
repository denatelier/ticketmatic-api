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
    amount: int | None = None
    locktypeid: int | None = None
    tickettypeid: int | None = None


@dataclasses.dataclass
class EventContingent(Model):
    id: int | None = None
    name: str | None = None
    amount: int | None = None
    eventid: int | None = None
    eventspecificprices: PricelistPrices | None = None
    locks: list[EventContingentLock] | None = None
    pricelistid: int | None = None
    withimportedbarcodes: bool | None = None


@dataclasses.dataclass
class EventContingentAvailability(Model):
    complimentary: int | None = None
    free: int | None = None
    locked_hard: int | None = None
    locked_soft: int | None = None
    reserved: int | None = None
    sold_paid: int | None = None
    sold_unpaid: int | None = None
    tickettypeid: int | None = None
    total: int | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class EventPreview(Model):
    linkurl: str | None = None
    previewimage: str | None = None
    subtitle: str | None = None
    title: str | None = None
    type: int | None = None
    url: str | None = None


@dataclasses.dataclass
class EventSalesChannel(Model):
    eventid: int | None = None
    haswaitinglist: bool | None = None
    isactive: bool | None = None
    saleendts: datetime | None = None
    saleschannelid: int | None = None
    salestartts: datetime | None = None


@dataclasses.dataclass
class EventSeatingplanContingent(Model):
    id: int | None = None
    name: str | None = None
    amount: int | None = None
    eventid: int | None = None
    seatrankid: int | None = None


@dataclasses.dataclass
class Event(Model):
    _has_custom_fields: ClassVar[bool] = True

    id: int | None = None
    name: str | None = None
    audiopreviewurl: str | None = None
    availability: list[EventContingentAvailability] | None = None
    cancellationpolicy: list[str] | None = None
    code: str | None = None
    contingents: list[EventContingent] | None = None
    currentstatus: int | None = None
    description: str | None = None
    endts: datetime | None = None
    externalcode: str | None = None
    image: str | None = None
    info: str | None = None
    layout: Layout | None = None
    locationid: int | None = None
    locationname: str | None = None
    maxnbrofticketsperbasket: int | None = None
    optinsetid: int | None = None
    previews: list[EventPreview] | None = None
    prices: EventPrices | None = None
    productionid: int | None = None
    publishedts: datetime | None = None
    queuetoken: int | None = None
    revenuesplitid: int | None = None
    saleendts: datetime | None = None
    saleschannels: list[EventSalesChannel] | None = None
    salestartts: datetime | None = None
    salestatusmessagesid: int | None = None
    schedule: str | None = None
    seatallowsingle: bool | None = None
    seated_chartkey: str | None = None
    seated_contingents: list[EventContingent] | None = None
    seatingplancontingents: list[EventSeatingplanContingent] | None = None
    seatingplaneventspecificprices: PricelistPrices | None = None
    seatingplanid: int | None = None
    seatingplanlocktemplate: str | None = None
    seatingplanpricelistid: int | None = None
    seatselection: bool | None = None
    segmentationtags: list[str] | None = None
    servicemailids: list[int] | None = None
    shortdescription: str | None = None
    socialdistance: int | None = None
    startts: datetime | None = None
    subtitle: str | None = None
    subtitle2: str | None = None
    tags: list[str] | None = None
    ticketfeeid: int | None = None
    ticketinfoid: int | None = None
    ticketlayoutid: int | None = None
    totalmaxtickets: int | None = None
    translations: list[str] | None = None
    upsellid: int | None = None
    waitinglisttype: int | None = None
    webremark: str | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None
    custom_fields: dict[str, Any] | None = None


@dataclasses.dataclass
class EventContext(Model):
    saleschannelid: int | None = None


@dataclasses.dataclass
class EventFilter(Model):
    productionid: int | None = None
    status: list[int] | None = None


@dataclasses.dataclass
class EventQuery(Model):
    context: EventContext | None = None
    filter: str | None = None
    lastupdatesince: datetime | None = None
    limit: int | None = None
    offset: int | None = None
    orderby: str | None = None
    output: str | None = None
    searchterm: str | None = None
    simplefilter: EventFilter | None = None


@dataclasses.dataclass
class EventLockTickets(Model):
    locktypeid: int | None = None
    ticketids: list[int] | None = None


@dataclasses.dataclass
class EventUnlockTickets(Model):
    ticketids: list[int] | None = None


@dataclasses.dataclass
class EventUpdateSeatRankForTickets(Model):
    seatrankid: int | None = None
    ticketids: list[int] | None = None


@dataclasses.dataclass
class EventScanTicketsOut(Model):
    tickettypeids: list[int] | None = None


@dataclasses.dataclass
class EventTicketFilter(Model):
    tickettypeid: int | None = None


@dataclasses.dataclass
class EventTicketQuery(Model):
    simplefilter: EventTicketFilter | None = None


@dataclasses.dataclass
class EventTicket(Model):
    _has_custom_fields: ClassVar[bool] = True

    id: int | None = None
    orderid: int | None = None
    accesscontrollastenteredscandeviceid: int | None = None
    accesscontrollastenteredts: datetime | None = None
    accesscontrollastexitscandeviceid: int | None = None
    accesscontrollastexitts: datetime | None = None
    accesscontrolstatus: int | None = None
    barcode: str | None = None
    bundleid: int | None = None
    locktypeid: int | None = None
    orderfee: float | None = None
    price: float | None = None
    properties: list[str] | None = None
    seatdescription: str | None = None
    seatid: str | None = None
    seatpriority: int | None = None
    seatrownumber: str | None = None
    seatseatnumber: str | None = None
    seatzoneid: int | None = None
    seatzonename: str | None = None
    ticketholderid: int | None = None
    ticketname: str | None = None
    tickettypeid: int | None = None
    tickettypepriceid: int | None = None
    vouchercodeid: int | None = None
    custom_fields: dict[str, Any] | None = None


@dataclasses.dataclass
class EventUpsellitem(Model):
    id: int | None = None
    type: str | None = None


@dataclasses.dataclass
class EventLocation(Model):
    _has_custom_fields: ClassVar[bool] = True

    id: int | None = None
    name: str | None = None
    city: str | None = None
    countrycode: str | None = None
    geostatus: int | None = None
    info: str | None = None
    lat: float | None = None
    long: float | None = None
    state: str | None = None
    street1: str | None = None
    street2: str | None = None
    street3: str | None = None
    street4: str | None = None
    zip: str | None = None
    isarchived: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None
    custom_fields: dict[str, Any] | None = None


@dataclasses.dataclass
class EventLocationQuery(Model):
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None


# --- Batch event operations ---


@dataclasses.dataclass
class BatchEventUpdateField(Model):
    key: str | None = None
    updatetype: str | None = None
    value: Any | None = None


@dataclasses.dataclass
class BatchEventParameters(Model):
    updatefields: list[BatchEventUpdateField] | None = None


@dataclasses.dataclass
class BatchEventOperation(Model):
    ids: list[int] | None = None
    operation: str | None = None
    parameters: BatchEventParameters | None = None
