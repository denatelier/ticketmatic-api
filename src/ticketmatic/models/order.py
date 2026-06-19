"""Data models for orders, order tickets, payments, and related operations."""

from __future__ import annotations

import dataclasses
from datetime import datetime
from typing import Any, ClassVar

from ticketmatic.models.base import Model
from ticketmatic.models.common import Address


@dataclasses.dataclass
class Ordercost(Model):
    """A single order fee for an order."""

    orderid: int | None = None
    """Order ID."""
    amount: float | None = None
    """Payment amount."""
    servicechargedefinitionid: int | None = None
    """Order fee ID."""


@dataclasses.dataclass
class SetOrderCost(Model):
    """Used to update order costs in an order."""

    amount: float | None = None
    """The amount for this ordercost."""
    servicechargedefinitionid: int | None = None
    """Id of the service charge to use for this ordercost."""


@dataclasses.dataclass
class OrderProduct(Model):
    """A single product in an order."""

    _has_custom_fields: ClassVar[bool] = True

    id: int | None = None
    """Orderproduct ID."""
    orderid: int | None = None
    """Order ID."""
    code: str | None = None
    """Unique code for this orderproduct."""
    contactid: int | None = None
    """Contact ID: the holder of this product."""
    price: float | None = None
    """Ticket price."""
    productid: int | None = None
    """Product ID."""
    properties: list[str] | None = None
    """Property values for this product."""
    vouchercodeid: int | None = None
    """Vouchercode ID for the voucher that is linked to this orderproduct."""
    custom_fields: dict[str, Any] | None = None
    """Custom field values keyed by name (``c_``-prefixed in the API)."""


@dataclasses.dataclass
class OrderTicket(Model):
    """A single ticket in an order."""

    id: int | None = None
    """Ticket ID."""
    orderid: int | None = None
    """Order ID."""
    barcode: str | None = None
    """The barcode of this ticket, will be visible when the order is confirmed."""
    bundleid: int | None = None
    """The id of the product this ticket is linked to."""
    bundlevariant: str | None = None
    """The key of the fixedseat variant this ticket is linked to."""
    cachedaccesscontrolstatus: int | None = None
    """Accesscontrol status for this ticket."""
    deliveredts: datetime | None = None
    """The timestamp of the last delivery of this ticket."""
    eventid: int | None = None
    """Event id."""
    price: float | None = None
    """Ticket price."""
    pricetypeid: int | None = None
    """Pricetype id."""
    seatcachedvisualx: float | None = None
    """Seat coordinate - x."""
    seatcachedvisualy: float | None = None
    """Seat coordinate - y."""
    seatdescription: str | None = None
    """Description of the ticket."""
    seated_ref: str | None = None
    """Seated ref."""
    seatname: str | None = None
    """Name of the seat."""
    seatzoneid: int | None = None
    """Seatzone ID."""
    servicecharge: float | None = None
    """Service charge."""
    ticketholderid: int | None = None
    """Ticket holder ID."""
    ticketname: str | None = None
    """Name for the ticket holder."""
    tickettypeid: int | None = None
    """Contingent ID."""
    tickettypename: str | None = None
    """Contingent name."""
    tickettypepriceid: int | None = None
    """Id for the tickettypeprice of this ticket for the order."""
    transferredto: int | None = None
    """The contact this ticket is transferred to."""
    vouchercodeid: int | None = None
    """The voucher code that was linked to this ticket."""


@dataclasses.dataclass
class OrderTickettype(Model):
    """A ticket type summary as used within an order."""

    id: int | None = None
    """Ticket type ID."""
    name: str | None = None
    """Ticket type name."""
    fulltypename: str | None = None
    """Full ticket type name."""


@dataclasses.dataclass
class Payment(Model):
    """A single payment."""

    id: int | None = None
    """Payment ID."""
    orderid: int | None = None
    """Order ID."""
    amount: float | None = None
    """Payment amount."""
    paidts: datetime | None = None
    """Timestamp of payment."""
    paymentmethodid: int | None = None
    """Payment method ID."""
    properties: Any | None = None
    """Additional properties for the payment. Structure depends on the payment
    method.
    """
    refundpaymentid: int | None = None
    """Id for the original payment if this payment is a refund."""
    vouchercodeid: int | None = None
    """Id of the vouchercode to use for this payment.

    **Note:** Ignored when importing orders.
    """


@dataclasses.dataclass
class OrderFilter(Model):
    """Used when requesting orders, to filter orders.

    Specify any of the supported fields to filter the list of orders.
    """

    createdsince: datetime | None = None
    """Only include orders older than the given timestamp."""
    customerid: int | None = None
    """Filter orders based on customer."""
    saleschannelid: int | None = None
    """Filter orders based on saleschannel."""
    status: int | None = None
    """Only include orders with a given status.

    Possible values:

    * **21001**: Unconfirmed orders
    * **21002**: Confirmed orders
    * **21003**: Archived orders
    """


@dataclasses.dataclass
class Order(Model):
    """A single Order."""

    _has_custom_fields: ClassVar[bool] = True

    orderid: int | None = None
    """Order ID."""
    amountpaid: float | None = None
    """Total amount paid.

    **Note:** Ignored when importing orders.
    """
    calculate_ordercosts: bool | None = None
    """Whether or not auto / script order fees should be calculated.

    **Note:** Ignored when importing orders.
    """
    code: str | None = None
    """Order code.

    Used as a unique identifier in web sales.
    """
    customerid: int | None = None
    """Customer ID."""
    deferredpaymentproperties: Any | None = None
    """Information on the deferred payment scenario.

    Structure depends on payment method.

    **Note:** Ignored when importing orders.
    """
    deliveryaddress: Address | None = None
    """Address used when delivering physically."""
    deliveryscenarioid: int | None = None
    """Delivery scenario ID."""
    deliverystatus: int | None = None
    """Delivery status.

    Possible values:

    * ``2601``: Not delivered
    * ``2602``: Delivered
    * ``2603``: Changed after delivery
    """
    expiryhandled: bool | None = None
    """Whether the expired order has been handled (and optionally expiry mail
    has been sent).
    """
    expiryts: datetime | None = None
    """When the order will expire."""
    firstname: str | None = None
    """First name (only with minimal output)."""
    hasopenpaymentrequest: bool | None = None
    """Indicates if the order has an open payment request with a PSP.

    **Note:** Ignored when importing orders.
    """
    isauthenticatedcustomer: bool | None = None
    """Has customer authenticated?

    **Note:** Ignored when importing orders.
    """
    lastname: str | None = None
    """Last name (only with minimal output)."""
    lookup: Any | None = None
    """Related objects.

    **Note:** Ignored when importing orders.
    """
    nbroftickets: int | None = None
    """Number of tickets in the order. Read-only.

    **Note:** Ignored when importing orders.
    """
    ordercosts: list[Ordercost] | None = None
    """Order fees for the order."""
    payments: list[Payment] | None = None
    """Payments for the order."""
    paymentscenarioid: int | None = None
    """Payment scenario ID."""
    paymentstatus: int | None = None
    """Payment status.

    Possible values:

    * ``0``: Incomplete
    * ``1``: Fully paid
    * ``2``: Overpaid

    **Note:** Ignored when importing orders.
    """
    products: list[OrderProduct] | None = None
    """Products in the order."""
    promocodes: list[str] | None = None
    """Promocodes active for the order.

    **Note:** Ignored when importing orders.
    """
    queuetokens: list[int] | None = None
    """Queue tokens for rate limiting.

    **Note:** Ignored when importing orders.
    """
    rappelhandled: bool | None = None
    """Whether the overdue order has been handled (and optionally reminder mail
    has been sent).
    """
    rappelts: datetime | None = None
    """When the reminder mail will be sent."""
    saleschannelid: int | None = None
    """Sales channel ID."""
    status: int | None = None
    """Order status.

    Possible values:

    * **21001**: Unconfirmed
    * **21002**: Confirmed
    * **21003**: Archived

    **Note:** Ignored when importing orders.
    """
    tickets: list[OrderTicket] | None = None
    """Tickets in the order."""
    totalamount: float | None = None
    """Total order amount.

    Includes all costs and fees.

    **Note:** Ignored when importing orders.
    """
    webskinid: int | None = None
    """Reference to the webskin that is used for showing the orderdetail page.

    **Note:** Ignored when importing orders.
    """
    createdts: datetime | None = None
    """Created timestamp."""
    lastupdatets: datetime | None = None
    """Last updated timestamp."""
    custom_fields: dict[str, Any] | None = None
    """Custom field values keyed by name (``c_``-prefixed in the API)."""


@dataclasses.dataclass
class OrderQuery(Model):
    """Filter parameters to fetch a list of orders."""

    filter: str | None = None
    """A SQL query that returns order IDs.

    Can be used to do arbitrary filtering. See the database documentation for
    order for more information.
    """
    includearchived: bool | None = None
    """If this parameter is true, archived items will be returned as well."""
    lastupdatesince: datetime | None = None
    """Only include orders that have been updated since the given timestamp."""
    limit: int | None = None
    """Limit results to at most the given amount of orders."""
    offset: int | None = None
    """Skip the first X orders."""
    orderby: str | None = None
    """Order by the given field.

    Supported values: ``createdts``, ``lastupdatets``.
    """
    orderby_asc: bool | None = None
    """Sets the direction for ordering. Default false."""
    output: str | None = None
    """Output format.

    Possible values:

    * **ids**: Only fill the ID field
    * **minimal**: A minimal set of order fields
    * **default**: Return all order fields (also used when the output parameter
      is omitted)
    * **withlookup**: Returns all order fields and an additional ``lookup``
      field which contains all dependent objects
    """
    searchterm: str | None = None
    """A text filter string.

    Matches against the order ID or the customer details.
    """
    simplefilter: OrderFilter | None = None
    """Filters the orders based on a given set of fields.

    Currently supports: ``createdsince``, ``saleschannelid``, ``customerid``,
    ``status``.
    """


@dataclasses.dataclass
class CreateOrder(Model):
    """Required data for creating an order."""

    events: list[int] | None = None
    """Event IDs that might end up in this order, this is optional."""
    products: list[int] | None = None
    """Product IDs that might end up in this order, this is optional."""
    saleschannelid: int | None = None
    """Sales channel in which this order is created."""


@dataclasses.dataclass
class UpdateOrder(Model):
    """Used to update an order.

    Each of the fields is optional. Omitting a field will leave it unchanged.
    """

    customerid: int | None = None
    """New customer ID."""
    customfields: Any | None = None
    """Change custom field values."""
    deliveryaddress: Address | None = None
    """Delivery address."""
    deliveryscenarioid: int | None = None
    """New delivery scenario ID."""
    expiryts: str | None = None
    """Expiry timestamp, as string in ISO 8601 format. Cannot be in the past."""
    ordercosts: list[SetOrderCost] | None = None
    """Set manual order costs.

    Setting the amount to 0 will remove the order cost from the order.
    """
    paymentscenarioid: int | None = None
    """New payment scenario ID."""
    rappelts: str | None = None
    """Rappel timestamp, as string in ISO 8601 format. Cannot be in the past."""


@dataclasses.dataclass
class OrderIdReservation(Model):
    """Order ID reservation."""

    id: int | None = None
    """Maximum ID to reserve."""


@dataclasses.dataclass
class OrderImportStatus(Model):
    """Import status per order."""

    id: int | None = None
    """Order ID."""
    error: str | None = None
    """Error message, if failed."""
    ok: bool | None = None
    """Whether the import succeeded."""


@dataclasses.dataclass
class SplitOrder(Model):
    """Required data for splitting an order."""

    customerid: int | None = None
    """The customer for the new order, when not provided will be the same as
    the current order.
    """
    deliveryscenarioid: int | None = None
    """The delivery scenario for the new order, when not provided will be the
    same as the current order.
    """
    paymentscenarioid: int | None = None
    """The payment scenario for the new order, when not provided will be the
    same as the current order.
    """
    products: list[int] | None = None
    """Product IDs that need to be moved from the current order to the new one."""
    regenerate_barcodes: bool | None = None
    """Assign new barcodes to tickets?"""
    tickets: list[int] | None = None
    """Ticket IDs that need to be moved from the current order to the new one."""


@dataclasses.dataclass
class PurgeOrdersRequest(Model):
    """Info for requesting a purge of all orders."""

    contacts: bool | None = None
    """Also purge contacts."""
    createdsince: str | None = None
    """Only purge orders created since this timestamp."""
    events: bool | None = None
    """Also purge events (incl. vouchers, products and bundles)."""


@dataclasses.dataclass
class CreateTicket(Model):
    """Info for adding a ticket to an order."""

    optionbundleid: int | None = None
    """The id for the optionbundle you want to add a new ticket to.

    Either tickettypepriceid or optionbundleid should be specified, not both.
    """
    ticketid: int | None = None
    """Manually select a specific ticket."""
    tickettypeid: int | None = None
    """Should only be specified when optionbundleid is specified.

    The tickettypeid for the ticket you want to add to the optionbundle.
    """
    tickettypepriceid: int | None = None
    """The ticket type price ID for the new ticket.

    Either tickettypepriceid or optionbundleid should be specified, not both.
    """
    vouchercode: str | None = None
    """Voucher code to use (if any)."""


@dataclasses.dataclass
class AddTickets(Model):
    """Request data used to add tickets to an order.

    The amount of tickets that can be added is limited to 50 per call.
    """

    onlysinglerow: bool | None = None
    """If this is set adding the tickets will only succeed if all tickets can
    be placed on a single row.
    """
    tickets: list[CreateTicket] | None = None
    """Ticket information."""


@dataclasses.dataclass
class UpdateTickets(Model):
    """Individual tickets can be updated.

    Per call you can specify any number of ticket IDs and one operation.
    Each operation accepts different parameters, dependent on the operation
    type:

    * **Set ticket holders**: an array of ticket holder IDs, one for each
      ticket (``ticketholderids``).
    * **Update price type**: an array of ticket price type IDs, one for each
      ticket (``tickettypepriceids``).
    * **Add to bundles**: an array of bundle IDs, one for each ticket.
    * **Remove from bundles**: none.
    """

    operation: str | None = None
    """Operation to execute.

    Supported values: ``setticketholders``, ``updatepricetype``,
    ``addtobundles``, ``removefrombundles``.
    """
    params: Any | None = None
    """Operation parameters."""
    tickets: list[int] | None = None
    """Ticket IDs."""


@dataclasses.dataclass
class DeleteTickets(Model):
    """Request data used to delete tickets from an order."""

    tickets: list[int] | None = None
    """Ticket IDs."""


@dataclasses.dataclass
class AddPayments(Model):
    """Request data used to add a payment to an order."""

    amount: float | None = None
    """Amount for the payment."""
    paymentmethodid: int | None = None
    """Id of the payment method to be used for the payment."""
    vouchercode: str | None = None
    """Voucher code to use for this payment."""
    vouchercodeid: int | None = None
    """Voucher code id to use for this payment."""


@dataclasses.dataclass
class AddRefunds(Model):
    """Request data used to refund a payment for an order."""

    amount: float | None = None
    """Amount that needs to be refunded."""
    paymentid: int | None = None
    """Id of the payment that needs to be refunded."""


@dataclasses.dataclass
class CreateProduct(Model):
    """Info for adding a product to an order."""

    productid: int | None = None
    """The id for the product you want to add."""
    properties: list[str] | None = None
    """The property values for the product."""


@dataclasses.dataclass
class AddProducts(Model):
    """Request data used to add products to an order."""

    products: list[CreateProduct] | None = None
    """Product information."""


@dataclasses.dataclass
class UpdateProducts(Model):
    """Individual products can be updated.

    Per call you can specify any number of product IDs and one operation.
    Each operation accepts different parameters, dependent on the operation
    type:

    * **Set product holders**: an array of ticket holder IDs, one for each
      product (``productholderids``).
    """

    operation: str | None = None
    """Operation to execute.

    Supported values: ``setproductholders``.
    """
    params: Any | None = None
    """Operation parameters."""
    products: list[int] | None = None
    """Product IDs."""


@dataclasses.dataclass
class DeleteProducts(Model):
    """Request data used to delete products from an order."""

    products: list[int] | None = None
    """Product IDs."""


@dataclasses.dataclass
class TicketsEmaildeliveryRequest(Model):
    """Info for requesting an e-mail delivery for an order."""

    templateid: int | None = None
    """Template id."""


@dataclasses.dataclass
class TicketsPdfRequest(Model):
    """Info for requesting a PDF ticket for one or more tickets or
    vouchercodes in an order.
    """

    tickets: list[int] | None = None
    """Ticket IDs."""
    vouchercodes: list[int] | None = None
    """Vouchercode IDs."""


@dataclasses.dataclass
class TicketsprocessedRequest(Model):
    """Required data for requesting the ticketsprocessedstatistics."""

    endts: str | None = None
    """End date of the period."""
    groupby: str | None = None
    """How the results are grouped. Values can be ``day`` or ``month``."""
    startts: str | None = None
    """Start date of the period."""


@dataclasses.dataclass
class TicketsprocessedStatistics(Model):
    """Statistics on the number of tickets processed in a certain period."""

    processed: int | None = None
    """The number of tickets processed."""
    soldonline: int | None = None
    """The number of tickets sold online."""
    ts: datetime | None = None
    """Start of the period."""


@dataclasses.dataclass
class Flowinfo(Model):
    """Info about a finished flow."""

    contactid: int | None = None
    """Contact id."""
    order: Order | None = None
    """Order active in the flow."""
    reason: str | None = None
    """Reason the user was redirected."""


@dataclasses.dataclass
class Flowsession(Model):
    """Required data for a flow session."""

    orderid: int | None = None
    """Order id."""
    contactid: int | None = None
    """Contact id."""


@dataclasses.dataclass
class OrderMailTemplate(Model):
    """A single order mail template."""

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new order mail template.

    **Note:** Ignored when updating an existing order mail template.
    """
    typeid: int | None = None
    """The type of this order mail template, defines where this template is
    used.
    """
    name: str | None = None
    """Name of the order mail template."""
    body: str | None = None
    """Message body.

    **Note:** Not set when retrieving a list of order mail templates.
    """
    subject: str | None = None
    """Subject line for the order mail template.

    **Note:** Not set when retrieving a list of order mail templates.
    """
    translations: list[str] | None = None
    """A map of language codes to gettext .po files.

    **Note:** Not set when retrieving a list of order mail templates.
    """
    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new order mail template.

    **Note:** Ignored when updating an existing order mail template.
    """
    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new order mail template.

    **Note:** Ignored when updating an existing order mail template.
    """
    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new order mail template.

    **Note:** Ignored when updating an existing order mail template.
    """


@dataclasses.dataclass
class OrderMailTemplateQuery(Model):
    """Set of parameters used to filter order mail templates."""

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


# --- Batch order operations ---


@dataclasses.dataclass
class BatchOrderUpdateField(Model):
    """Field to update on an order."""

    key: str | None = None
    """The name of the field, can either be a custom field or one of the
    following fixed fields (``deliveryscenarioid``, ``paymentscenarioid``).
    """
    updatetype: str | None = None
    """The type of update that needs to be done on the field.

    Can either be ``set`` (default), ``add`` or ``remove`` when used in
    combination with multi value fields.
    """
    value: Any | None = None
    """The value of the field."""


@dataclasses.dataclass
class BatchOrderParameters(Model):
    """Parameters for batch operations performed on orders."""

    updatefields: list[BatchOrderUpdateField] | None = None
    """Set of fields to update, used for operation ``update``.

    Custom fields are also supported.
    """


@dataclasses.dataclass
class BatchOrderOperation(Model):
    """Batch operations performed on orders."""

    ids: list[int] | None = None
    """Restrict operation to supplied IDs, if these ids are not specified
    **all** orders are updated.
    """
    operation: str | None = None
    """Operation to perform.

    Possible values: ``emaildelivery``, ``update``, ``pdf``.
    """
    parameters: BatchOrderParameters | None = None
    """Operation-specific parameters."""


# --- Import models ---


@dataclasses.dataclass
class ImportBundleTicket(Model):
    """Used when importing an order with optionbundle tickets."""

    id: int | None = None
    """Manually select a specific ticket."""
    overrideprice: bool | None = None
    """If boolean is set to true, the price field is used (even if set to 0)
    to determine the price for this ticket.
    """
    price: float | None = None
    """The price for this bundle ticket, if this value is greater than 0 it's
    always used. If one of the bundletickets has a price, all bundletickets
    should have a price. Setting this overrides the default behaviour of the
    configured bundle.
    """
    seatzoneid: int | None = None
    """Seatzone ID."""
    tickettypeid: int | None = None
    """The tickettype ID for the ticket."""
    tickettypepriceid: int | None = None
    """The tickettypeprice ID for the ticket.

    This field is required if bundletickets are specified for a fixed bundle.
    When importing an optionbundle, if one of the bundletickets has a
    tickettypepriceid, all bundletickets should have one. Setting this
    overrides the default behaviour of the configured bundle.
    """


@dataclasses.dataclass
class ImportTicket(Model):
    """Used when importing an order."""

    id: int | None = None
    """Manually select a specific ticket."""
    overrideprice: bool | None = None
    """If boolean is set to true, the price field is used (even if set to 0)
    to determine the price for this ticket.
    """
    overrideservicecharge: bool | None = None
    """If boolean is set to true, the servicecharge field is used (even if set
    to 0) to determine the servicecharge for this ticket.
    """
    price: float | None = None
    """Ticket price, will always be used if larger than 0."""
    seatzoneid: int | None = None
    """Seatzone ID."""
    servicecharge: float | None = None
    """Service charge for this ticket."""
    ticketholderid: int | None = None
    """If this ticket should be linked to a contact, set the ticketholderid."""
    ticketholdername: str | None = None
    """DEPRECATED: Use ticketholderid."""
    tickettypeid: int | None = None
    """The tickettype ID for the ticket."""
    tickettypepriceid: int | None = None
    """The ticket type price ID for the new ticket.

    Either tickettypepriceid or optionbundleid should be specified, not both.
    """
    vouchercode: str | None = None
    """Voucher code to use (if any)."""
    vouchercodeid: int | None = None
    """The voucher code to link to this ticket."""


@dataclasses.dataclass
class ImportOrdercost(Model):
    """Used when importing orders."""

    amount: float | None = None
    """The amount for this ordercost, can only be specified with manual
    ordercosts.
    """
    servicechargedefinitionid: int | None = None
    """Id of the service charge to use for this ordercost."""


@dataclasses.dataclass
class ImportPayment(Model):
    """Used when importing an order."""

    amount: float | None = None
    """Amount."""
    paidts: datetime | None = None
    """Timestamp of payment."""
    paymentmethodid: int | None = None
    """Payment method id."""
    properties: Any | None = None
    """Additional properties for the payment. Can contain a variable
    structure.
    """
    vouchercode: str | None = None
    """Voucher code that was used for this payment."""
    vouchercodeid: int | None = None
    """Voucher code id that was used for this payment."""


@dataclasses.dataclass
class ImportProduct(Model):
    """Used when importing orders."""

    bundletickets: list[ImportBundleTicket] | None = None
    """List of tickets that belong to this bundle."""
    overrideprice: bool | None = None
    """If boolean is set to true, the price field is used (even if set to 0)
    to determine the price for this product.
    """
    price: float | None = None
    """Product price, will always be used if larger than 0."""
    productholderid: int | None = None
    """Indicate which contact is the holder of this product.

    Currently only used with bundles.
    """
    productid: int | None = None
    """The id for the product you want to add."""
    properties: list[str] | None = None
    """The property values for the product."""
    voucheramount: float | None = None
    """If this product references a voucher, set the amount to reserve for
    this voucher.
    """
    vouchercode: str | None = None
    """If this product references a voucher, set the code for the voucher that
    will be created. If not set, the code will be generated.
    """
    voucherexpiryts: datetime | None = None
    """If this product references a voucher, set the expiry timestamp for the
    vouchercode that will be created. If not set, the default timestamp
    configured in the voucher will be set.
    """


@dataclasses.dataclass
class ImportOrder(Model):
    """Used to import an order."""

    _has_custom_fields: ClassVar[bool] = True

    orderid: int | None = None
    """Order ID."""
    code: str | None = None
    """Order code.

    Used as a unique identifier in web sales.
    """
    customerid: int | None = None
    """Customer ID."""
    deliveryaddress: Address | None = None
    """Address used when delivering physically."""
    deliveryscenarioid: int | None = None
    """Delivery scenario ID."""
    deliverystatus: int | None = None
    """Delivery status.

    Possible values:

    * ``2601``: Not delivered
    * ``2602``: Delivered
    * ``2603``: Changed after delivery
    """
    expiryhandled: bool | None = None
    """Indicates if the expired order has been handled.

    If set to false when importing, Ticketmatic will send expiry mails if
    configured.
    """
    expiryts: datetime | None = None
    """When the order will expire.

    If this is specified expiryhandled should also be specified.
    """
    ordercosts: list[ImportOrdercost] | None = None
    """Order fees for the order."""
    payments: list[ImportPayment] | None = None
    """Payments in the order."""
    paymentscenarioid: int | None = None
    """Payment scenario ID."""
    products: list[ImportProduct] | None = None
    """Products in the order."""
    rappelhandled: bool | None = None
    """Indicates if the overdue order has been handled.

    If set to false when importing, Ticketmatic will send reminder mails if
    configured.
    """
    rappelts: datetime | None = None
    """When a reminder mail will be sent.

    If this is specified rappelhandled should also be specified.
    """
    saleschannelid: int | None = None
    """Sales channel ID."""
    tickets: list[ImportTicket] | None = None
    """Tickets in the order."""
    createdts: datetime | None = None
    """Created timestamp."""
    lastupdatets: datetime | None = None
    """Last updated timestamp."""
    custom_fields: dict[str, Any] | None = None
    """Custom field values keyed by name (``c_``-prefixed in the API)."""
