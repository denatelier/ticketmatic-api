from __future__ import annotations

import dataclasses
from datetime import datetime
from typing import Any, ClassVar

from ticketmatic.models.base import Model
from ticketmatic.models.common import Address


@dataclasses.dataclass
class Ordercost(Model):
    orderid: int | None = None
    amount: float | None = None
    servicechargedefinitionid: int | None = None


@dataclasses.dataclass
class SetOrderCost(Model):
    amount: float | None = None
    servicechargedefinitionid: int | None = None


@dataclasses.dataclass
class OrderProduct(Model):
    _has_custom_fields: ClassVar[bool] = True

    id: int | None = None
    orderid: int | None = None
    code: str | None = None
    contactid: int | None = None
    price: float | None = None
    productid: int | None = None
    properties: list[str] | None = None
    vouchercodeid: int | None = None
    custom_fields: dict[str, Any] | None = None


@dataclasses.dataclass
class OrderTicket(Model):
    id: int | None = None
    orderid: int | None = None
    barcode: str | None = None
    bundleid: int | None = None
    bundlevariant: str | None = None
    cachedaccesscontrolstatus: int | None = None
    deliveredts: datetime | None = None
    eventid: int | None = None
    price: float | None = None
    pricetypeid: int | None = None
    seatcachedvisualx: float | None = None
    seatcachedvisualy: float | None = None
    seatdescription: str | None = None
    seated_ref: str | None = None
    seatname: str | None = None
    seatzoneid: int | None = None
    servicecharge: float | None = None
    ticketholderid: int | None = None
    ticketname: str | None = None
    tickettypeid: int | None = None
    tickettypename: str | None = None
    tickettypepriceid: int | None = None
    transferredto: int | None = None
    vouchercodeid: int | None = None


@dataclasses.dataclass
class OrderTickettype(Model):
    id: int | None = None
    name: str | None = None
    fulltypename: str | None = None


@dataclasses.dataclass
class Payment(Model):
    id: int | None = None
    orderid: int | None = None
    amount: float | None = None
    paidts: datetime | None = None
    paymentmethodid: int | None = None
    properties: Any | None = None
    refundpaymentid: int | None = None
    vouchercodeid: int | None = None


@dataclasses.dataclass
class OrderFilter(Model):
    createdsince: datetime | None = None
    customerid: int | None = None
    saleschannelid: int | None = None
    status: int | None = None


@dataclasses.dataclass
class Order(Model):
    _has_custom_fields: ClassVar[bool] = True

    orderid: int | None = None
    amountpaid: float | None = None
    calculate_ordercosts: bool | None = None
    code: str | None = None
    customerid: int | None = None
    deferredpaymentproperties: Any | None = None
    deliveryaddress: Address | None = None
    deliveryscenarioid: int | None = None
    deliverystatus: int | None = None
    expiryhandled: bool | None = None
    expiryts: datetime | None = None
    firstname: str | None = None
    hasopenpaymentrequest: bool | None = None
    isauthenticatedcustomer: bool | None = None
    lastname: str | None = None
    lookup: Any | None = None
    nbroftickets: int | None = None
    ordercosts: list[Ordercost] | None = None
    payments: list[Payment] | None = None
    paymentscenarioid: int | None = None
    paymentstatus: int | None = None
    products: list[OrderProduct] | None = None
    promocodes: list[str] | None = None
    queuetokens: list[int] | None = None
    rappelhandled: bool | None = None
    rappelts: datetime | None = None
    saleschannelid: int | None = None
    status: int | None = None
    tickets: list[OrderTicket] | None = None
    totalamount: float | None = None
    webskinid: int | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None
    custom_fields: dict[str, Any] | None = None


@dataclasses.dataclass
class OrderQuery(Model):
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None
    limit: int | None = None
    offset: int | None = None
    orderby: str | None = None
    orderby_asc: bool | None = None
    output: str | None = None
    searchterm: str | None = None
    simplefilter: OrderFilter | None = None


@dataclasses.dataclass
class CreateOrder(Model):
    events: list[int] | None = None
    products: list[int] | None = None
    saleschannelid: int | None = None


@dataclasses.dataclass
class UpdateOrder(Model):
    customerid: int | None = None
    customfields: Any | None = None
    deliveryaddress: Address | None = None
    deliveryscenarioid: int | None = None
    expiryts: str | None = None
    ordercosts: list[SetOrderCost] | None = None
    paymentscenarioid: int | None = None
    rappelts: str | None = None


@dataclasses.dataclass
class OrderIdReservation(Model):
    id: int | None = None


@dataclasses.dataclass
class OrderImportStatus(Model):
    id: int | None = None
    error: str | None = None
    ok: bool | None = None


@dataclasses.dataclass
class SplitOrder(Model):
    customerid: int | None = None
    deliveryscenarioid: int | None = None
    paymentscenarioid: int | None = None
    products: list[int] | None = None
    regenerate_barcodes: bool | None = None
    tickets: list[int] | None = None


@dataclasses.dataclass
class PurgeOrdersRequest(Model):
    contacts: bool | None = None
    createdsince: str | None = None
    events: bool | None = None


@dataclasses.dataclass
class CreateTicket(Model):
    optionbundleid: int | None = None
    ticketid: int | None = None
    tickettypeid: int | None = None
    tickettypepriceid: int | None = None
    vouchercode: str | None = None


@dataclasses.dataclass
class AddTickets(Model):
    onlysinglerow: bool | None = None
    tickets: list[CreateTicket] | None = None


@dataclasses.dataclass
class UpdateTickets(Model):
    operation: str | None = None
    params: Any | None = None
    tickets: list[int] | None = None


@dataclasses.dataclass
class DeleteTickets(Model):
    tickets: list[int] | None = None


@dataclasses.dataclass
class AddPayments(Model):
    amount: float | None = None
    paymentmethodid: int | None = None
    vouchercode: str | None = None
    vouchercodeid: int | None = None


@dataclasses.dataclass
class AddRefunds(Model):
    amount: float | None = None
    paymentid: int | None = None


@dataclasses.dataclass
class CreateProduct(Model):
    productid: int | None = None
    properties: list[str] | None = None


@dataclasses.dataclass
class AddProducts(Model):
    products: list[CreateProduct] | None = None


@dataclasses.dataclass
class UpdateProducts(Model):
    operation: str | None = None
    params: Any | None = None
    products: list[int] | None = None


@dataclasses.dataclass
class DeleteProducts(Model):
    products: list[int] | None = None


@dataclasses.dataclass
class TicketsEmaildeliveryRequest(Model):
    templateid: int | None = None


@dataclasses.dataclass
class TicketsPdfRequest(Model):
    tickets: list[int] | None = None
    vouchercodes: list[int] | None = None


@dataclasses.dataclass
class TicketsprocessedRequest(Model):
    endts: str | None = None
    groupby: str | None = None
    startts: str | None = None


@dataclasses.dataclass
class TicketsprocessedStatistics(Model):
    processed: int | None = None
    soldonline: int | None = None
    ts: datetime | None = None


@dataclasses.dataclass
class Flowinfo(Model):
    contactid: int | None = None
    order: Order | None = None
    reason: str | None = None


@dataclasses.dataclass
class Flowsession(Model):
    orderid: int | None = None
    contactid: int | None = None


@dataclasses.dataclass
class OrderMailTemplate(Model):
    id: int | None = None
    typeid: int | None = None
    name: str | None = None
    body: str | None = None
    subject: str | None = None
    translations: list[str] | None = None
    isarchived: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class OrderMailTemplateQuery(Model):
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None


# --- Batch order operations ---

@dataclasses.dataclass
class BatchOrderUpdateField(Model):
    key: str | None = None
    updatetype: str | None = None
    value: Any | None = None


@dataclasses.dataclass
class BatchOrderParameters(Model):
    updatefields: list[BatchOrderUpdateField] | None = None


@dataclasses.dataclass
class BatchOrderOperation(Model):
    ids: list[int] | None = None
    operation: str | None = None
    parameters: BatchOrderParameters | None = None


# --- Import models ---

@dataclasses.dataclass
class ImportBundleTicket(Model):
    id: int | None = None
    overrideprice: bool | None = None
    price: float | None = None
    seatzoneid: int | None = None
    tickettypeid: int | None = None
    tickettypepriceid: int | None = None


@dataclasses.dataclass
class ImportTicket(Model):
    id: int | None = None
    overrideprice: bool | None = None
    overrideservicecharge: bool | None = None
    price: float | None = None
    seatzoneid: int | None = None
    servicecharge: float | None = None
    ticketholderid: int | None = None
    ticketholdername: str | None = None
    tickettypeid: int | None = None
    tickettypepriceid: int | None = None
    vouchercode: str | None = None
    vouchercodeid: int | None = None


@dataclasses.dataclass
class ImportOrdercost(Model):
    amount: float | None = None
    servicechargedefinitionid: int | None = None


@dataclasses.dataclass
class ImportPayment(Model):
    amount: float | None = None
    paidts: datetime | None = None
    paymentmethodid: int | None = None
    properties: Any | None = None
    vouchercode: str | None = None
    vouchercodeid: int | None = None


@dataclasses.dataclass
class ImportProduct(Model):
    bundletickets: list[ImportBundleTicket] | None = None
    overrideprice: bool | None = None
    price: float | None = None
    productholderid: int | None = None
    productid: int | None = None
    properties: list[str] | None = None
    voucheramount: float | None = None
    vouchercode: str | None = None
    voucherexpiryts: datetime | None = None


@dataclasses.dataclass
class ImportOrder(Model):
    _has_custom_fields: ClassVar[bool] = True

    orderid: int | None = None
    code: str | None = None
    customerid: int | None = None
    deliveryaddress: Address | None = None
    deliveryscenarioid: int | None = None
    deliverystatus: int | None = None
    expiryhandled: bool | None = None
    expiryts: datetime | None = None
    ordercosts: list[ImportOrdercost] | None = None
    payments: list[ImportPayment] | None = None
    paymentscenarioid: int | None = None
    products: list[ImportProduct] | None = None
    rappelhandled: bool | None = None
    rappelts: datetime | None = None
    saleschannelid: int | None = None
    tickets: list[ImportTicket] | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None
    custom_fields: dict[str, Any] | None = None
