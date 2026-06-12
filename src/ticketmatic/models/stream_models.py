from __future__ import annotations

import dataclasses
from datetime import datetime
from typing import Any, ClassVar

from ticketmatic.models.base import Model


@dataclasses.dataclass
class EventstreamItem(Model):
    id: str | None = None
    data: Any | None = None
    ts: str | None = None
    type: str | None = None


@dataclasses.dataclass
class EventstreamRequest(Model):
    id: str | None = None
    eventtypes: str | None = None
    ts: str | None = None


@dataclasses.dataclass
class EventstreamResult(Model):
    moreresults: bool | None = None
    nextid: str | None = None
    results: list[EventstreamItem] | None = None


@dataclasses.dataclass
class SubscriberCommunication(Model):
    name: str | None = None
    addresses: list[str] | None = None
    remark: str | None = None
    ts: datetime | None = None


@dataclasses.dataclass
class SubscriberSync(Model):
    email: str | None = None
    firstname: str | None = None
    lastname: str | None = None
    oldemail: str | None = None
    subscribed: bool | None = None


# --- Waiting List ---


@dataclasses.dataclass
class WaitingListRequestItemTicket(Model):
    tickettypepriceid: int | None = None


@dataclasses.dataclass
class WaitingListRequestItem(Model):
    _has_custom_fields: ClassVar[bool] = True

    eventid: int | None = None
    tickets: list[WaitingListRequestItemTicket] | None = None
    custom_fields: dict[str, Any] | None = None


@dataclasses.dataclass
class WaitingListRequest(Model):
    _has_custom_fields: ClassVar[bool] = True

    id: int | None = None
    orderid: int | None = None
    contactid: int | None = None
    itemsstatus: int | None = None
    requeststatus: int | None = None
    saleschannelid: int | None = None
    sortorder: int | None = None
    waitinglistrequestitems: list[WaitingListRequestItem] | None = None
    isarchived: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None
    custom_fields: dict[str, Any] | None = None


@dataclasses.dataclass
class WaitingListRequestQuery(Model):
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None
