"""Data models for pricing: price lists, price types, ticket fees, and order fees."""

from __future__ import annotations

import dataclasses
from datetime import datetime
from typing import Any, ClassVar

from ticketmatic.models.base import Model


@dataclasses.dataclass
class PricelistPriceCondition(Model):
    """A condition that restricts when a pricelist price is available.

    Possible condition types are ``ticketlimit``, ``date``, ``promocode``,
    ``orderticketlimit``, and ``voucherids``.
    """

    type: str | None = None
    """The type of condition.

    Possible values: ``ticketlimit``, ``date``, ``promocode``,
    ``orderticketlimit``, ``voucherids``.
    """

    value: Any | None = None
    """The value of this condition. See ``type`` for what should be filled in."""


@dataclasses.dataclass
class EventPricesCost(Model):
    """Information about costs for a price for an event."""

    cost: float | None = None
    """The actual cost."""

    costid: int | None = None
    """Cost ID."""


@dataclasses.dataclass
class EventPricesSaleschannel(Model):
    """Information about the price for a pricetype for the specific sales channel
    for an event.
    """

    conditions: list[PricelistPriceCondition] | None = None
    """Extra conditions for this price (e.g. a promocode or a ticket limit)."""

    costs: list[EventPricesCost] | None = None
    """The costs associated with this price."""

    price: float | None = None
    """The actual price."""

    saleschannelid: int | None = None
    """Saleschannel ID."""

    servicecharge: float | None = None
    """The actual servicecharge."""

    tickettypepriceid: int | None = None
    """Tickettypeprice ID."""


@dataclasses.dataclass
class EventPricesPricetype(Model):
    """Information about the price for a pricetype for the specific sales channel
    for an event.
    """

    pricetypeid: int | None = None
    """Pricetype ID."""

    saleschannels: list[EventPricesSaleschannel] | None = None
    """Price information for this pricetype for the different sales channels."""

    tickettypepriceid: int | None = None
    """Ticket type price ID, used to add tickets to an order."""


@dataclasses.dataclass
class EventPricesContingent(Model):
    """Information about the prices for a contingent for an event."""

    contingentid: int | None = None
    """Contingent ID."""

    pricetypes: list[EventPricesPricetype] | None = None
    """Price information for the pricetypes."""


@dataclasses.dataclass
class EventPrices(Model):
    """Information about the prices for an event."""

    contingents: list[EventPricesContingent] | None = None
    """Price information for the contingents."""


@dataclasses.dataclass
class PricelistPrice(Model):
    """A single price entry in a price list."""

    availabilities: list[bool] | None = None
    """Array of booleans indicating if the corresponding price is available for
    this :class:`PricelistPrice`. Should contain the same number of booleans
    as ``prices``.
    """

    conditions: list[PricelistPriceCondition] | None = None
    """Extra conditions for this price (e.g. a promocode or a ticket limit)."""

    position: int | None = None
    """Optional position of this price in the pricelist.

    Only used for event-specific prices.
    """

    prices: list[float] | None = None
    """The decimal prices for this :class:`PricelistPrice`.

    If no ``seatrankids`` has been set this should consist of 1 price. If
    ``seatrankids`` are set this should contain an equal number of prices as
    the number of seat ranks.
    """

    pricetypeid: int | None = None
    """The pricetype for this price."""

    saleschannels: list[int] | None = None
    """The list of sales channels for which this :class:`PricelistPrice` is
    active.
    """


@dataclasses.dataclass
class PricelistPrices(Model):
    """The prices and seat-rank configuration for a price list."""

    prices: list[PricelistPrice] | None = None
    """The set of prices for this pricelist."""

    seatrankids: list[int] | None = None
    """The seat ranks for which this pricelist lists prices."""


@dataclasses.dataclass
class PriceList(Model):
    """A single price list."""

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new price list.

    **Note:** Ignored when updating an existing price list.
    """

    name: str | None = None
    """Name for the pricelist."""

    hasranks: bool | None = None
    """Boolean indicating whether this pricelist has ranks or not."""

    prices: PricelistPrices | None = None
    """Definition of the actual prices and conditions for the pricelist.

    **Note:** Not set when retrieving a list of price lists.
    """

    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new price list.

    **Note:** Ignored when updating an existing price list.
    """

    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new price list.

    **Note:** Ignored when updating an existing price list.
    """

    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new price list.

    **Note:** Ignored when updating an existing price list.
    """


@dataclasses.dataclass
class PriceListQuery(Model):
    """Set of parameters used to filter price lists."""

    filter: str | None = None
    """Filter the returned items by specifying a query on the public data model
    that returns the ids.
    """

    includearchived: bool | None = None
    """If this parameter is true, archived items will be returned as well."""

    lastupdatesince: datetime | None = None
    """All items that were updated since this timestamp will be returned.

    Timestamp should be passed in ``YYYY-MM-DD hh:mm:ss`` format.
    """


@dataclasses.dataclass
class PriceType(Model):
    """A single price type."""

    _has_custom_fields: ClassVar[bool] = True

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new price type.

    **Note:** Ignored when updating an existing price type.
    """

    typeid: int | None = None
    """The category of this price type, defines how the price is displayed."""

    name: str | None = None
    """Name of the price type."""

    remark: str | None = None
    """A remark that describes the price type. Will be shown to customers."""

    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new price type.

    **Note:** Ignored when updating an existing price type.
    """

    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new price type.

    **Note:** Ignored when updating an existing price type.
    """

    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new price type.

    **Note:** Ignored when updating an existing price type.
    """

    custom_fields: dict[str, Any] | None = None
    """Custom field values keyed by name (``c_``-prefixed in the API)."""


@dataclasses.dataclass
class PriceTypeQuery(Model):
    """Set of parameters used to filter price types."""

    filter: str | None = None
    """Filter the returned items by specifying a query on the public data model
    that returns the ids.
    """

    includearchived: bool | None = None
    """If this parameter is true, archived items will be returned as well."""

    lastupdatesince: datetime | None = None
    """All items that were updated since this timestamp will be returned.

    Timestamp should be passed in ``YYYY-MM-DD hh:mm:ss`` format.
    """


# --- Ticket Fee models ---


@dataclasses.dataclass
class TicketfeeSaleschannelRule(Model):
    """A fee rule for a specific sales channel, based on a fixed amount or a
    percentage.
    """

    saleschannelid: int | None = None
    """The sales channel for which this rule is active."""

    status: str | None = None
    """The status sets the type of rule.

    Possible values:

    * ``fixedfee``: A fixed ticket fee.

    * ``percentagefee``: A fee that is a percentage of the ticket price.
    """

    value: float | None = None
    """The value of this ticket fee.

    Can be an absolute amount (``fixedfee``) or a percentage
    (``percentagefee``). In both cases only provide a decimal.
    """


@dataclasses.dataclass
class TicketfeeException(Model):
    """An exception to the default ticket fee rule for a specific price type and
    a set of sales channels.
    """

    pricetypeid: int | None = None
    """The price type for which this exception is active."""

    saleschannels: list[TicketfeeSaleschannelRule] | None = None
    """The set of rules (one for each sales channel)."""


@dataclasses.dataclass
class TicketfeeRules(Model):
    """Defines which fees are active for specific price types and sales channels.

    It is possible to define a fixed fee and a percentage-based fee. The
    default rule (if none is specified for a specific sales channel) is always
    a fixed fee of 0.
    """

    default: list[TicketfeeSaleschannelRule] | None = None
    """The default ticket fee rule, one rule for each sales channel."""

    exceptions: list[TicketfeeException] | None = None
    """An array of exception rules for specific price types."""


@dataclasses.dataclass
class TicketFee(Model):
    """A single ticket fee."""

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new ticket fee.

    **Note:** Ignored when updating an existing ticket fee.
    """

    name: str | None = None
    """Name for the ticket fee scheme."""

    rules: TicketfeeRules | None = None
    """Definition of the rules that define when the ticket fee will be applied.

    **Note:** Not set when retrieving a list of ticket fees.
    """

    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new ticket fee.

    **Note:** Ignored when updating an existing ticket fee.
    """

    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new ticket fee.

    **Note:** Ignored when updating an existing ticket fee.
    """

    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new ticket fee.

    **Note:** Ignored when updating an existing ticket fee.
    """


@dataclasses.dataclass
class TicketFeeQuery(Model):
    """Set of parameters used to filter ticket fees."""

    filter: str | None = None
    """Filter the returned items by specifying a query on the public data model
    that returns the ids.
    """

    includearchived: bool | None = None
    """If this parameter is true, archived items will be returned as well."""

    lastupdatesince: datetime | None = None
    """All items that were updated since this timestamp will be returned.

    Timestamp should be passed in ``YYYY-MM-DD hh:mm:ss`` format.
    """


# --- Order Fee models ---


@dataclasses.dataclass
class OrderfeeAutoRule(Model):
    """An automatic order fee rule specifying when and how the fee is applied."""

    deliveryscenarioids: list[int] | None = None
    """The delivery scenarios that this order fee is applicable for.

    If not set it defaults to 'all'. This is only needed if the order fee
    type is set to automatic.
    """

    paymentscenarioids: list[int] | None = None
    """The payment scenarios that this order fee is applicable for.

    If not set it defaults to 'all'. This is only needed if the order fee
    type is set to automatic.
    """

    saleschannelids: list[int] | None = None
    """The sales channels that this order fee is applicable for.

    If not set it defaults to 'all'. This is only needed if the order fee
    type is set to automatic.
    """

    status: str | None = None
    """Can be ``fixedfee`` or ``percentagefee``. Defaults to ``fixedfee``.

    This is only needed if the order fee type is set to automatic.
    """

    value: float | None = None
    """The value (amount) that will be added to the order.

    Is required if the order fee type is set to automatic.
    """


@dataclasses.dataclass
class OrderfeeScriptContext(Model):
    """Extra context data made available to an order fee script."""

    cacheable: bool | None = None
    """If set to true the query will be cached for 60 seconds.

    If not set the query will be executed again every time a script is
    executed.
    """

    key: str | None = None
    """The name of the variable that will be added to the script environment."""

    query: str | None = None
    """The query that will be executed on the public data model.

    The result will be available in the script environment.
    """


@dataclasses.dataclass
class OrderfeeRule(Model):
    """The rule definition for an order fee."""

    auto: list[OrderfeeAutoRule] | None = None
    """Required when the order fee type is set to automatic.

    A set of rules that define the order fee.
    """

    context: list[OrderfeeScriptContext] | None = None
    """Optional extra information added to the script environment.

    Can be set when the order fee type is set to script.
    """

    script: str | None = None
    """Required when the order fee type is set to script.

    The JavaScript code must return a value.
    """


@dataclasses.dataclass
class OrderFee(Model):
    """A single order fee."""

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new order fee definition.

    **Note:** Ignored when creating a new order fee.
    """

    typeid: int | None = None
    """Type of the order fee.

    Can be Automatic (2401), Script (2402) or Manual (2403).
    """

    name: str | None = None
    """Name for the order fee."""

    rule: OrderfeeRule | None = None
    """Definition of the rule that defines when the order fee will be applied.

    **Note:** Not set when retrieving a list of order fee definitions.

    **Note:** Not set when retrieving a list of order fees.
    """

    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new order fee definition.

    **Note:** Ignored when creating a new order fee.
    """

    archivedts: datetime | None = None
    """Archived timestamp.

    **Note:** Ignored when creating a new order fee definition.

    **Note:** Ignored when creating a new order fee.
    """

    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new order fee definition.

    **Note:** Ignored when creating a new order fee.
    """

    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new order fee definition.

    **Note:** Ignored when creating a new order fee.
    """


@dataclasses.dataclass
class OrderFeeQuery(Model):
    """Set of parameters used to filter order fees."""

    filter: str | None = None
    """Filter the returned items by specifying a query on the public data model
    that returns the ids.
    """

    includearchived: bool | None = None
    """If this parameter is true, archived items will be returned as well."""

    lastupdatesince: datetime | None = None
    """All items that were updated since this timestamp will be returned.

    Timestamp should be passed in ``YYYY-MM-DD hh:mm:ss`` format.
    """


@dataclasses.dataclass
class OrderFeeDefinition(Model):
    """A single order fee definition."""

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new order fee definition.

    **Note:** Ignored when creating a new order fee.
    """

    typeid: int | None = None
    """Type of the order fee.

    Can be Automatic (2401), Script (2402) or Manual (2403).
    """

    name: str | None = None
    """Name for the order fee."""

    rule: OrderfeeRule | None = None
    """Definition of the rule that defines when the order fee will be applied.

    **Note:** Not set when retrieving a list of order fee definitions.

    **Note:** Not set when retrieving a list of order fees.
    """

    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new order fee definition.

    **Note:** Ignored when creating a new order fee.
    """

    archivedts: datetime | None = None
    """Archived timestamp.

    **Note:** Ignored when creating a new order fee definition.

    **Note:** Ignored when creating a new order fee.
    """

    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new order fee definition.

    **Note:** Ignored when creating a new order fee.
    """

    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new order fee definition.

    **Note:** Ignored when creating a new order fee.
    """


@dataclasses.dataclass
class OrderFeeDefinitionQuery(Model):
    """Set of parameters used to filter order fee definitions."""

    filter: str | None = None
    """Filter the returned items by specifying a query on the public data model
    that returns the ids.
    """

    includearchived: bool | None = None
    """If this parameter is true, archived items will be returned as well."""

    lastupdatesince: datetime | None = None
    """All items that were updated since this timestamp will be returned.

    Timestamp should be passed in ``YYYY-MM-DD hh:mm:ss`` format.
    """
