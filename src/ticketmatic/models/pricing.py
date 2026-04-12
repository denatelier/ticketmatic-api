from __future__ import annotations

import dataclasses
from datetime import datetime
from typing import Any, ClassVar

from ticketmatic.models.base import Model


@dataclasses.dataclass
class PricelistPriceCondition(Model):
    type: str | None = None
    value: Any | None = None


@dataclasses.dataclass
class EventPricesCost(Model):
    cost: float | None = None
    costid: int | None = None


@dataclasses.dataclass
class EventPricesSaleschannel(Model):
    conditions: list[PricelistPriceCondition] | None = None
    costs: list[EventPricesCost] | None = None
    price: float | None = None
    saleschannelid: int | None = None
    servicecharge: float | None = None
    tickettypepriceid: int | None = None


@dataclasses.dataclass
class EventPricesPricetype(Model):
    pricetypeid: int | None = None
    saleschannels: list[EventPricesSaleschannel] | None = None
    tickettypepriceid: int | None = None


@dataclasses.dataclass
class EventPricesContingent(Model):
    contingentid: int | None = None
    pricetypes: list[EventPricesPricetype] | None = None


@dataclasses.dataclass
class EventPrices(Model):
    contingents: list[EventPricesContingent] | None = None


@dataclasses.dataclass
class PricelistPrice(Model):
    availabilities: list[bool] | None = None
    conditions: list[PricelistPriceCondition] | None = None
    position: int | None = None
    prices: list[float] | None = None
    pricetypeid: int | None = None
    saleschannels: list[int] | None = None


@dataclasses.dataclass
class PricelistPrices(Model):
    prices: list[PricelistPrice] | None = None
    seatrankids: list[int] | None = None


@dataclasses.dataclass
class PriceList(Model):
    id: int | None = None
    name: str | None = None
    hasranks: bool | None = None
    prices: PricelistPrices | None = None
    isarchived: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class PriceListQuery(Model):
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None


@dataclasses.dataclass
class PriceType(Model):
    _has_custom_fields: ClassVar[bool] = True

    id: int | None = None
    typeid: int | None = None
    name: str | None = None
    remark: str | None = None
    isarchived: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None
    custom_fields: dict[str, Any] | None = None


@dataclasses.dataclass
class PriceTypeQuery(Model):
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None


# --- Ticket Fee models ---

@dataclasses.dataclass
class TicketfeeSaleschannelRule(Model):
    saleschannelid: int | None = None
    status: str | None = None
    value: float | None = None


@dataclasses.dataclass
class TicketfeeException(Model):
    pricetypeid: int | None = None
    saleschannels: list[TicketfeeSaleschannelRule] | None = None


@dataclasses.dataclass
class TicketfeeRules(Model):
    default: list[TicketfeeSaleschannelRule] | None = None
    exceptions: list[TicketfeeException] | None = None


@dataclasses.dataclass
class TicketFee(Model):
    id: int | None = None
    name: str | None = None
    rules: TicketfeeRules | None = None
    isarchived: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class TicketFeeQuery(Model):
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None


# --- Order Fee models ---

@dataclasses.dataclass
class OrderfeeAutoRule(Model):
    deliveryscenarioids: list[int] | None = None
    paymentscenarioids: list[int] | None = None
    saleschannelids: list[int] | None = None
    status: str | None = None
    value: float | None = None


@dataclasses.dataclass
class OrderfeeScriptContext(Model):
    cacheable: bool | None = None
    key: str | None = None
    query: str | None = None


@dataclasses.dataclass
class OrderfeeRule(Model):
    auto: list[OrderfeeAutoRule] | None = None
    context: list[OrderfeeScriptContext] | None = None
    script: str | None = None


@dataclasses.dataclass
class OrderFee(Model):
    id: int | None = None
    typeid: int | None = None
    name: str | None = None
    rule: OrderfeeRule | None = None
    isarchived: bool | None = None
    archivedts: datetime | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class OrderFeeQuery(Model):
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None


@dataclasses.dataclass
class OrderFeeDefinition(Model):
    id: int | None = None
    typeid: int | None = None
    name: str | None = None
    rule: OrderfeeRule | None = None
    isarchived: bool | None = None
    archivedts: datetime | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class OrderFeeDefinitionQuery(Model):
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None
