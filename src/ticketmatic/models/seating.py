"""Data models for seating plans, seat ranks, lock types, and related structures."""

from __future__ import annotations

import dataclasses
from datetime import datetime

from ticketmatic.models.base import Model


@dataclasses.dataclass
class LogicalPlanSeat(Model):
    """The definition of a seat."""

    id: str | None = None
    """The ID of the seat."""

    name: str | None = None
    """The name of the seat."""

    center: list[float] | None = None
    """The center point [x,y] of the seat."""

    coord: int | None = None
    """The coordinate of the seat."""

    priority: int | None = None
    """Should this seat be sold prior to other seats."""

    rowname: str | None = None
    """The rowname of the seat."""

    seatdescriptionid: int | None = None
    """The seat description template for this seat."""

    seatrankid: int | None = None
    """The seat rank for this seat."""

    size: list[float] | None = None
    """The width and height of the seat."""


@dataclasses.dataclass
class LogicalPlanRow(Model):
    """A row contains a set of seats."""

    name: str | None = None
    """The name of the row."""

    coord: int | None = None
    """The coordinate of the row."""

    seats: list[LogicalPlanSeat] | None = None
    """The seats in this row."""


@dataclasses.dataclass
class LogicalPlan(Model):
    """The logical plan describes the structure and layout of seats in a zone."""

    id: int | None = None
    """The ID of the zone."""

    name: str | None = None
    """The name of the zone."""

    rows: list[LogicalPlanRow] | None = None
    """The rows layout."""


@dataclasses.dataclass
class SeatDescriptionTemplate(Model):
    """Templates to allow different seat description for seats."""

    id: int | None = None
    """The ID of the template."""

    name: str | None = None
    """The name of the template."""

    template: str | None = None
    """The template itself with placeholders for rowname, seatname and zonename."""


@dataclasses.dataclass
class LockTemplate(Model):
    """Mapping of which type of lock is applied to which seats."""

    name: str | None = None
    """The name of the template."""

    seats: list[int] | None = None
    """A map where seat id is the key and the lock type is the value."""


@dataclasses.dataclass
class SeatingPlan(Model):
    """A single seating plan."""

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new seating plan.

    **Note:** Ignored when updating an existing seating plan.
    """

    name: str | None = None
    """The name for the seating plan."""

    jointjs_dump: str | None = None
    """JointJS seating plan dump.

    **Note:** Not set when retrieving a list of seating plans.
    """

    status: str | None = None
    """The status this seating plan is in."""

    translations: list[str] | None = None
    """Translations for the seat description templates.

    **Note:** Not set when retrieving a list of seating plans.
    """

    useszones: bool | None = None
    """When true: treat as a multi-zoned seatingplan."""

    zones: list[int] | None = None
    """IDs of the seat zones defined.

    **Note:** Ignored when creating a new seating plan.

    **Note:** Ignored when updating an existing seating plan.

    **Note:** Not set when retrieving a list of seating plans.
    """

    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new seating plan.

    **Note:** Ignored when updating an existing seating plan.
    """

    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new seating plan.

    **Note:** Ignored when updating an existing seating plan.
    """

    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new seating plan.

    **Note:** Ignored when updating an existing seating plan.
    """


@dataclasses.dataclass
class SeatingPlanQuery(Model):
    """Set of parameters used to filter seating plans."""

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


@dataclasses.dataclass
class SeatRank(Model):
    """A single seat rank."""

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new seat rank.

    **Note:** Ignored when updating an existing seat rank.
    """

    name: str | None = None
    """Name for the seat rank."""

    color: str | None = None
    """The color of the seat rank."""

    priority: int | None = None
    """Priority of the seat rank.

    **Note:** Not set when retrieving a list of seat ranks.
    """

    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new seat rank.

    **Note:** Ignored when updating an existing seat rank.
    """

    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new seat rank.

    **Note:** Ignored when updating an existing seat rank.
    """

    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new seat rank.

    **Note:** Ignored when updating an existing seat rank.
    """


@dataclasses.dataclass
class SeatRankQuery(Model):
    """Set of parameters used to filter seat ranks."""

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


@dataclasses.dataclass
class LockType(Model):
    """A single lock type."""

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new lock type.

    **Note:** Ignored when updating an existing lock type.
    """

    name: str | None = None
    """Name for the lock type."""

    color: str | None = None
    """The color of the lock type."""

    hideseats: bool | None = None
    """Hides seats in online sales if this is true."""

    ishardlock: bool | None = None
    """Indicates whether this lock is a hard lock (meaning that it normally
    never will be released and does not count for the inventory) or a soft
    lock.
    """

    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new lock type.

    **Note:** Ignored when updating an existing lock type.
    """

    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new lock type.

    **Note:** Ignored when updating an existing lock type.
    """

    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new lock type.

    **Note:** Ignored when updating an existing lock type.
    """


@dataclasses.dataclass
class LockTypeQuery(Model):
    """Set of parameters used to filter lock types."""

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
