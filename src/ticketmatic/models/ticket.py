from __future__ import annotations

import dataclasses
from datetime import datetime
from typing import Any

from ticketmatic.models.base import Model


@dataclasses.dataclass
class TicketLayout(Model):
    id: int | None = None
    typeid: int | None = None
    name: str | None = None
    isarchived: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class TicketLayoutQuery(Model):
    typeid: int | None = None
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None


@dataclasses.dataclass
class TicketLayoutTemplate(Model):
    id: int | None = None
    typeid: int | None = None
    name: str | None = None
    css: str | None = None
    deliveryscenarios: list[int] | None = None
    htmltemplate: str | None = None
    ticketsperpage: int | None = None
    translations: list[str] | None = None
    isarchived: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class TicketLayoutTemplateQuery(Model):
    typeid: int | None = None
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None


@dataclasses.dataclass
class TicketsalesFlowConfig(Model):
    from_: datetime | None = None
    until: datetime | None = None
    widget: str | None = None
    widgetparams: list[str] | None = None

    @classmethod
    def from_dict(cls, data: dict | None) -> TicketsalesFlowConfig | None:
        if data is None:
            return None
        from ticketmatic.json_utils import unpack_timestamp
        return cls(
            from_=unpack_timestamp(data.get("from")),
            until=unpack_timestamp(data.get("until")),
            widget=data.get("widget"),
            widgetparams=data.get("widgetparams"),
        )

    def to_dict(self) -> dict[str, Any]:
        from ticketmatic.json_utils import pack_timestamp
        result: dict[str, Any] = {}
        if self.from_ is not None:
            result["from"] = pack_timestamp(self.from_)
        if self.until is not None:
            result["until"] = pack_timestamp(self.until)
        if self.widget is not None:
            result["widget"] = self.widget
        if self.widgetparams is not None:
            result["widgetparams"] = self.widgetparams
        return result


@dataclasses.dataclass
class Ticketsalesflow(Model):
    id: int | None = None
    name: str | None = None
    availabilityfielddefinition: str | None = None
    code: str | None = None
    config: list[TicketsalesFlowConfig] | None = None
    description: str | None = None
    productavailability: list[int] | None = None
    supportedparameters: list[str] | None = None
    testmode: bool | None = None
    ticketsalessetupid: int | None = None


@dataclasses.dataclass
class TicketsalesflowQuery(Model):
    filter: str | None = None
    lastupdatesince: datetime | None = None


@dataclasses.dataclass
class Ticketsalessetup(Model):
    id: int | None = None
    name: str | None = None
    code: str | None = None
    integrated: bool | None = None
    widgetparams: list[str] | None = None


@dataclasses.dataclass
class TicketsalessetupQuery(Model):
    filter: str | None = None
    lastupdatesince: datetime | None = None


# --- Web Sales Skins ---

@dataclasses.dataclass
class WebSalesSkinConfiguration(Model):
    favicon: str | None = None
    googleanalyticsid: str | None = None
    googletagmanagerid: str | None = None
    title: str | None = None


@dataclasses.dataclass
class WebSalesSkin(Model):
    id: int | None = None
    name: str | None = None
    asseturl: str | None = None
    configuration: WebSalesSkinConfiguration | None = None
    css: str | None = None
    html: str | None = None
    translations: list[str] | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class WebSalesSkinQuery(Model):
    filter: str | None = None
    lastupdatesince: datetime | None = None
