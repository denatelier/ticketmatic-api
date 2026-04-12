from __future__ import annotations

import dataclasses
from typing import Any

from ticketmatic.client import Client
from ticketmatic.json_utils import unpack_array
from ticketmatic.models.common import AddItemsResult, BatchResult, LogItem, Url
from ticketmatic.models.order import (
    AddPayments,
    AddProducts,
    AddRefunds,
    AddTickets,
    BatchOrderOperation,
    CreateOrder,
    DeleteProducts,
    DeleteTickets,
    ImportOrder,
    Order,
    OrderIdReservation,
    OrderImportStatus,
    OrderQuery,
    PurgeOrdersRequest,
    SplitOrder,
    TicketsEmaildeliveryRequest,
    TicketsPdfRequest,
    UpdateOrder,
    UpdateProducts,
    UpdateTickets,
)
from ticketmatic.models.payment import PaymentRequest


@dataclasses.dataclass
class OrdersList:
    data: list[Order]
    nbrofresults: int

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> OrdersList:
        return cls(
            data=unpack_array(Order, data.get("data", [])),
            nbrofresults=int(data.get("nbrofresults", 0)),
        )


def get_list(client: Client, params: OrderQuery | dict | None = None) -> OrdersList:
    if params is None or isinstance(params, dict):
        params = OrderQuery.from_dict(params or {})
    req = client.new_request("GET", "/{accountname}/orders")
    req.add_query("filter", params.filter)
    req.add_query("includearchived", params.includearchived)
    req.add_query("lastupdatesince", params.lastupdatesince)
    req.add_query("limit", params.limit)
    req.add_query("offset", params.offset)
    req.add_query("orderby", params.orderby)
    req.add_query("orderby_asc", params.orderby_asc)
    req.add_query("output", params.output)
    req.add_query("searchterm", params.searchterm)
    req.add_query("simplefilter", params.simplefilter)
    return OrdersList.from_dict(req.run())


def get(client: Client, id: int) -> Order:
    req = client.new_request("GET", "/{accountname}/orders/{id}")
    req.add_parameter("id", id)
    return Order.from_dict(req.run())


def create(client: Client, data: CreateOrder | dict) -> Order:
    if isinstance(data, dict):
        data = CreateOrder.from_dict(data)
    req = client.new_request("POST", "/{accountname}/orders")
    req.set_body(data.to_dict())
    return Order.from_dict(req.run())


def update(client: Client, id: int, data: UpdateOrder | dict) -> Order:
    if isinstance(data, dict):
        data = UpdateOrder.from_dict(data)
    req = client.new_request("PUT", "/{accountname}/orders/{id}")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Order.from_dict(req.run())


def delete(client: Client, id: int) -> None:
    req = client.new_request("DELETE", "/{accountname}/orders/{id}")
    req.add_parameter("id", id)
    req.run()


def batch(client: Client, data: BatchOrderOperation | dict) -> None:
    if isinstance(data, dict):
        data = BatchOrderOperation.from_dict(data)
    req = client.new_request("POST", "/{accountname}/orders/batch")
    req.set_body(data.to_dict())
    req.run()


def delete_batch(client: Client, data: list[int]) -> BatchResult:
    req = client.new_request("DELETE", "/{accountname}/orders")
    req.set_body(data)
    return BatchResult.from_dict(req.run())


def confirm(client: Client, id: int) -> Order:
    req = client.new_request("POST", "/{accountname}/orders/{id}")
    req.add_parameter("id", id)
    return Order.from_dict(req.run())


def split(client: Client, id: int, data: SplitOrder | dict) -> Order:
    if isinstance(data, dict):
        data = SplitOrder.from_dict(data)
    req = client.new_request("POST", "/{accountname}/orders/{id}/split")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Order.from_dict(req.run())


def add_tickets(client: Client, id: int, data: AddTickets | dict) -> AddItemsResult:
    if isinstance(data, dict):
        data = AddTickets.from_dict(data)
    req = client.new_request("POST", "/{accountname}/orders/{id}/tickets")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return AddItemsResult.from_dict(req.run())


def update_tickets(client: Client, id: int, data: UpdateTickets | dict) -> Order:
    if isinstance(data, dict):
        data = UpdateTickets.from_dict(data)
    req = client.new_request("PUT", "/{accountname}/orders/{id}/tickets")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Order.from_dict(req.run())


def delete_tickets(client: Client, id: int, data: DeleteTickets | dict) -> Order:
    if isinstance(data, dict):
        data = DeleteTickets.from_dict(data)
    req = client.new_request("DELETE", "/{accountname}/orders/{id}/tickets")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Order.from_dict(req.run())


def add_products(client: Client, id: int, data: AddProducts | dict) -> AddItemsResult:
    if isinstance(data, dict):
        data = AddProducts.from_dict(data)
    req = client.new_request("POST", "/{accountname}/orders/{id}/products")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return AddItemsResult.from_dict(req.run())


def update_products(client: Client, id: int, data: UpdateProducts | dict) -> Order:
    if isinstance(data, dict):
        data = UpdateProducts.from_dict(data)
    req = client.new_request("PUT", "/{accountname}/orders/{id}/products")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Order.from_dict(req.run())


def delete_products(client: Client, id: int, data: DeleteProducts | dict) -> Order:
    if isinstance(data, dict):
        data = DeleteProducts.from_dict(data)
    req = client.new_request("DELETE", "/{accountname}/orders/{id}/products")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Order.from_dict(req.run())


def add_payments(client: Client, id: int, data: AddPayments | dict) -> Order:
    if isinstance(data, dict):
        data = AddPayments.from_dict(data)
    req = client.new_request("POST", "/{accountname}/orders/{id}/payments")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Order.from_dict(req.run())


def add_refunds(client: Client, id: int, data: AddRefunds | dict) -> Order:
    if isinstance(data, dict):
        data = AddRefunds.from_dict(data)
    req = client.new_request("POST", "/{accountname}/orders/{id}/refunds")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Order.from_dict(req.run())


def get_logs(client: Client, id: int) -> list[LogItem]:
    req = client.new_request("GET", "/{accountname}/orders/{id}/logs")
    req.add_parameter("id", id)
    return unpack_array(LogItem, req.run())


def post_tickets_pdf(client: Client, id: int, data: TicketsPdfRequest | dict) -> Url:
    if isinstance(data, dict):
        data = TicketsPdfRequest.from_dict(data)
    req = client.new_request("POST", "/{accountname}/orders/{id}/tickets/pdf")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Url.from_dict(req.run())


def post_pdf(client: Client, id: int, data: TicketsPdfRequest | dict) -> Url:
    if isinstance(data, dict):
        data = TicketsPdfRequest.from_dict(data)
    req = client.new_request("POST", "/{accountname}/orders/{id}/pdf")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Url.from_dict(req.run())


def post_tickets_email_delivery(client: Client, id: int, data: TicketsEmaildeliveryRequest | dict) -> Order:
    if isinstance(data, dict):
        data = TicketsEmaildeliveryRequest.from_dict(data)
    req = client.new_request("POST", "/{accountname}/orders/{id}/tickets/emaildelivery")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Order.from_dict(req.run())


def post_tickets_email_payment_instruction(client: Client, id: int) -> Order:
    req = client.new_request("POST", "/{accountname}/orders/{id}/tickets/emailpaymentinstruction")
    req.add_parameter("id", id)
    return Order.from_dict(req.run())


def post_payment_request(client: Client, id: int, data: PaymentRequest | dict) -> Url:
    if isinstance(data, dict):
        data = PaymentRequest.from_dict(data)
    req = client.new_request("POST", "/{accountname}/orders/{id}/paymentrequest")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Url.from_dict(req.run())


def cancel_payment_request(client: Client, id: int) -> None:
    req = client.new_request("DELETE", "/{accountname}/orders/{id}/paymentrequest")
    req.add_parameter("id", id)
    req.run()


def get_document(client: Client, id: int, document_id: str, language: str) -> Url:
    req = client.new_request("GET", "/{accountname}/orders/{id}/documents/{documentid}/{language}")
    req.add_parameter("id", id)
    req.add_parameter("documentid", document_id)
    req.add_parameter("language", language)
    return Url.from_dict(req.run())


def import_orders(client: Client, data: list[ImportOrder | dict]) -> list[OrderImportStatus]:
    body = []
    for item in data:
        if isinstance(item, dict):
            item = ImportOrder.from_dict(item)
        body.append(item.to_dict())
    req = client.new_request("POST", "/{accountname}/orders/import")
    req.set_body(body)
    return unpack_array(OrderImportStatus, req.run())


def reserve(client: Client, data: OrderIdReservation | dict) -> OrderIdReservation:
    if isinstance(data, dict):
        data = OrderIdReservation.from_dict(data)
    req = client.new_request("POST", "/{accountname}/orders/import/reserve")
    req.set_body(data.to_dict())
    return OrderIdReservation.from_dict(req.run())


def purge(client: Client, params: PurgeOrdersRequest | dict | None = None) -> Any:
    if params is None or isinstance(params, dict):
        params = PurgeOrdersRequest.from_dict(params or {})
    req = client.new_request("POST", "/{accountname}/orders/purge")
    req.add_query("contacts", params.contacts)
    req.add_query("createdsince", params.createdsince)
    req.add_query("events", params.events)
    return req.run()
