from __future__ import annotations

import dataclasses
from datetime import datetime

from ticketmatic.models.base import Model


@dataclasses.dataclass
class LogicalPlanSeat(Model):
    id: str | None = None
    name: str | None = None
    center: list[float] | None = None
    coord: int | None = None
    priority: int | None = None
    rowname: str | None = None
    seatdescriptionid: int | None = None
    seatrankid: int | None = None
    size: list[float] | None = None


@dataclasses.dataclass
class LogicalPlanRow(Model):
    name: str | None = None
    coord: int | None = None
    seats: list[LogicalPlanSeat] | None = None


@dataclasses.dataclass
class LogicalPlan(Model):
    id: int | None = None
    name: str | None = None
    rows: list[LogicalPlanRow] | None = None


@dataclasses.dataclass
class SeatDescriptionTemplate(Model):
    id: int | None = None
    name: str | None = None
    template: str | None = None


@dataclasses.dataclass
class LockTemplate(Model):
    name: str | None = None
    seats: list[int] | None = None


@dataclasses.dataclass
class SeatingPlan(Model):
    id: int | None = None
    name: str | None = None
    jointjs_dump: str | None = None
    status: str | None = None
    translations: list[str] | None = None
    useszones: bool | None = None
    zones: list[int] | None = None
    isarchived: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class SeatingPlanQuery(Model):
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None


@dataclasses.dataclass
class SeatRank(Model):
    id: int | None = None
    name: str | None = None
    color: str | None = None
    priority: int | None = None
    isarchived: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class SeatRankQuery(Model):
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None


@dataclasses.dataclass
class LockType(Model):
    id: int | None = None
    name: str | None = None
    color: str | None = None
    hideseats: bool | None = None
    ishardlock: bool | None = None
    isarchived: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class LockTypeQuery(Model):
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None
