"""Order manipulation operations."""

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
    """Paged list of :class:`~ticketmatic.models.order.Order` objects."""

    data: list[Order]
    """Result data."""
    nbrofresults: int
    """Total number of results available without considering limit and offset,
    useful for paging.
    """

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> OrdersList:
        """Construct an :class:`OrdersList` from a raw API response dict."""
        return cls(
            data=unpack_array(Order, data.get("data", [])),
            nbrofresults=int(data.get("nbrofresults", 0)),
        )


def get_list(client: Client, params: OrderQuery | dict | None = None) -> OrdersList:
    """Get a list of orders.

    :param client: Ticketmatic API client.
    :param params: Optional query parameters.
    :returns: An :class:`OrdersList` with paged results.
    """
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
    """Get a single order.

    :param client: Ticketmatic API client.
    :param id: Order ID.
    :returns: The requested :class:`~ticketmatic.models.order.Order`.
    """
    req = client.new_request("GET", "/{accountname}/orders/{id}")
    req.add_parameter("id", id)
    return Order.from_dict(req.run())


def create(client: Client, data: CreateOrder | dict) -> Order:
    """Create a new order.

    Creates a new empty order. Each order is linked to a sales channel,
    which needs to be supplied when creating.

    **Note:** This method may return a ``429 Rate Limit Exceeded`` status
    when there is too much demand.

    :param client: Ticketmatic API client.
    :param data: Order creation parameters.
    :returns: The newly created :class:`~ticketmatic.models.order.Order`.
    """
    if isinstance(data, dict):
        data = CreateOrder.from_dict(data)
    req = client.new_request("POST", "/{accountname}/orders")
    req.set_body(data.to_dict())
    return Order.from_dict(req.run())


def update(client: Client, id: int, data: UpdateOrder | dict) -> Order:
    """Update an order.

    :param client: Ticketmatic API client.
    :param id: Order ID.
    :param data: Updated order data.
    :returns: The updated :class:`~ticketmatic.models.order.Order`.
    """
    if isinstance(data, dict):
        data = UpdateOrder.from_dict(data)
    req = client.new_request("PUT", "/{accountname}/orders/{id}")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Order.from_dict(req.run())


def delete(client: Client, id: int) -> None:
    """Delete an order.

    :param client: Ticketmatic API client.
    :param id: Order ID.
    """
    req = client.new_request("DELETE", "/{accountname}/orders/{id}")
    req.add_parameter("id", id)
    req.run()


def batch(client: Client, data: BatchOrderOperation | dict) -> None:
    """Apply batch operations to a set of orders.

    The parameters required are specific to the type of operation. The
    operation will be applied to the orders with the given IDs (up to 1000
    per call).

    Supported operations include ``emaildelivery``, ``pdf``, and
    ``update``.

    :param client: Ticketmatic API client.
    :param data: Batch operation descriptor.
    """
    if isinstance(data, dict):
        data = BatchOrderOperation.from_dict(data)
    req = client.new_request("POST", "/{accountname}/orders/batch")
    req.set_body(data.to_dict())
    req.run()


def delete_batch(client: Client, data: list[int]) -> BatchResult:
    """Delete multiple orders.

    :param client: Ticketmatic API client.
    :param data: List of order IDs to delete.
    :returns: A :class:`~ticketmatic.models.common.BatchResult` summary.
    """
    req = client.new_request("DELETE", "/{accountname}/orders")
    req.set_body(data)
    return BatchResult.from_dict(req.run())


def confirm(client: Client, id: int) -> Order:
    """Confirm an order.

    Marks the order as confirmed.

    :param client: Ticketmatic API client.
    :param id: Order ID.
    :returns: The confirmed :class:`~ticketmatic.models.order.Order`.
    """
    req = client.new_request("POST", "/{accountname}/orders/{id}")
    req.add_parameter("id", id)
    return Order.from_dict(req.run())


def split(client: Client, id: int, data: SplitOrder | dict) -> Order:
    """Split tickets and/or products from an order into a new one.

    :param client: Ticketmatic API client.
    :param id: Source order ID.
    :param data: Split parameters specifying which items to move.
    :returns: The newly created :class:`~ticketmatic.models.order.Order`.
    """
    if isinstance(data, dict):
        data = SplitOrder.from_dict(data)
    req = client.new_request("POST", "/{accountname}/orders/{id}/split")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Order.from_dict(req.run())


def add_tickets(client: Client, id: int, data: AddTickets | dict) -> AddItemsResult:
    """Add tickets to an order.

    When adding tickets, this is limited to 50 tickets per call.

    **Note:** This method may return a ``429 Rate Limit Exceeded`` status
    when there is too much demand.

    :param client: Ticketmatic API client.
    :param id: Order ID.
    :param data: Tickets to add.
    :returns: An :class:`~ticketmatic.models.common.AddItemsResult`.
    """
    if isinstance(data, dict):
        data = AddTickets.from_dict(data)
    req = client.new_request("POST", "/{accountname}/orders/{id}/tickets")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return AddItemsResult.from_dict(req.run())


def update_tickets(client: Client, id: int, data: UpdateTickets | dict) -> Order:
    """Modify tickets in an order.

    Individual tickets can be updated. Per call you can specify any number
    of ticket IDs and one operation (e.g. set ticket holders, update price
    type, add to bundles, remove from bundles).

    :param client: Ticketmatic API client.
    :param id: Order ID.
    :param data: Ticket update parameters.
    :returns: The updated :class:`~ticketmatic.models.order.Order`.
    """
    if isinstance(data, dict):
        data = UpdateTickets.from_dict(data)
    req = client.new_request("PUT", "/{accountname}/orders/{id}/tickets")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Order.from_dict(req.run())


def delete_tickets(client: Client, id: int, data: DeleteTickets | dict) -> Order:
    """Remove tickets from an order.

    :param client: Ticketmatic API client.
    :param id: Order ID.
    :param data: Specifies which tickets to remove.
    :returns: The updated :class:`~ticketmatic.models.order.Order`.
    """
    if isinstance(data, dict):
        data = DeleteTickets.from_dict(data)
    req = client.new_request("DELETE", "/{accountname}/orders/{id}/tickets")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Order.from_dict(req.run())


def add_products(client: Client, id: int, data: AddProducts | dict) -> AddItemsResult:
    """Add products to an order.

    :param client: Ticketmatic API client.
    :param id: Order ID.
    :param data: Products to add.
    :returns: An :class:`~ticketmatic.models.common.AddItemsResult`.
    """
    if isinstance(data, dict):
        data = AddProducts.from_dict(data)
    req = client.new_request("POST", "/{accountname}/orders/{id}/products")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return AddItemsResult.from_dict(req.run())


def update_products(client: Client, id: int, data: UpdateProducts | dict) -> Order:
    """Modify products in an order.

    Individual products can be updated. Per call you can specify any number
    of product IDs and one operation (e.g. set product holders).

    :param client: Ticketmatic API client.
    :param id: Order ID.
    :param data: Product update parameters.
    :returns: The updated :class:`~ticketmatic.models.order.Order`.
    """
    if isinstance(data, dict):
        data = UpdateProducts.from_dict(data)
    req = client.new_request("PUT", "/{accountname}/orders/{id}/products")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Order.from_dict(req.run())


def delete_products(client: Client, id: int, data: DeleteProducts | dict) -> Order:
    """Remove products from an order.

    :param client: Ticketmatic API client.
    :param id: Order ID.
    :param data: Specifies which products to remove.
    :returns: The updated :class:`~ticketmatic.models.order.Order`.
    """
    if isinstance(data, dict):
        data = DeleteProducts.from_dict(data)
    req = client.new_request("DELETE", "/{accountname}/orders/{id}/products")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Order.from_dict(req.run())


def add_payments(client: Client, id: int, data: AddPayments | dict) -> Order:
    """Add payments to an order.

    :param client: Ticketmatic API client.
    :param id: Order ID.
    :param data: Payment details to add.
    :returns: The updated :class:`~ticketmatic.models.order.Order`.
    """
    if isinstance(data, dict):
        data = AddPayments.from_dict(data)
    req = client.new_request("POST", "/{accountname}/orders/{id}/payments")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Order.from_dict(req.run())


def add_refunds(client: Client, id: int, data: AddRefunds | dict) -> Order:
    """Add a refund for a payment on an order.

    :param client: Ticketmatic API client.
    :param id: Order ID.
    :param data: Refund details.
    :returns: The updated :class:`~ticketmatic.models.order.Order`.
    """
    if isinstance(data, dict):
        data = AddRefunds.from_dict(data)
    req = client.new_request("POST", "/{accountname}/orders/{id}/refunds")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Order.from_dict(req.run())


def get_logs(client: Client, id: int) -> list[LogItem]:
    """Get the log history for an order.

    :param client: Ticketmatic API client.
    :param id: Order ID.
    :returns: List of :class:`~ticketmatic.models.common.LogItem` entries.
    """
    req = client.new_request("GET", "/{accountname}/orders/{id}/logs")
    req.add_parameter("id", id)
    return unpack_array(LogItem, req.run())


def post_tickets_pdf(client: Client, id: int, data: TicketsPdfRequest | dict) -> Url:
    """Export tickets to PDF (deprecated).

    **Deprecated:** Use :func:`post_pdf` (``/{id}/pdf``) instead.

    :param client: Ticketmatic API client.
    :param id: Order ID.
    :param data: PDF request parameters.
    :returns: A :class:`~ticketmatic.models.common.Url` for the PDF.
    """
    if isinstance(data, dict):
        data = TicketsPdfRequest.from_dict(data)
    req = client.new_request("POST", "/{accountname}/orders/{id}/tickets/pdf")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Url.from_dict(req.run())


def post_pdf(client: Client, id: int, data: TicketsPdfRequest | dict) -> Url:
    """Export tickets and/or voucher codes to PDF.

    :param client: Ticketmatic API client.
    :param id: Order ID.
    :param data: PDF request parameters.
    :returns: A :class:`~ticketmatic.models.common.Url` for the PDF.
    """
    if isinstance(data, dict):
        data = TicketsPdfRequest.from_dict(data)
    req = client.new_request("POST", "/{accountname}/orders/{id}/pdf")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Url.from_dict(req.run())


def post_tickets_email_delivery(
    client: Client, id: int, data: TicketsEmaildeliveryRequest | dict
) -> Order:
    """Send the delivery e-mail for the order.

    :param client: Ticketmatic API client.
    :param id: Order ID.
    :param data: E-mail delivery request parameters.
    :returns: The updated :class:`~ticketmatic.models.order.Order`.
    """
    if isinstance(data, dict):
        data = TicketsEmaildeliveryRequest.from_dict(data)
    req = client.new_request("POST", "/{accountname}/orders/{id}/tickets/emaildelivery")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Order.from_dict(req.run())


def post_tickets_email_payment_instruction(client: Client, id: int) -> Order:
    """Send the payment instruction e-mail.

    Send the payment instruction e-mail for the order that is linked to
    the payment scenario. Will only be sent if saldo <> 0 and
    paymentinstruction contains a valid payment instruction template.

    :param client: Ticketmatic API client.
    :param id: Order ID.
    :returns: The updated :class:`~ticketmatic.models.order.Order`.
    """
    req = client.new_request(
        "POST", "/{accountname}/orders/{id}/tickets/emailpaymentinstruction"
    )
    req.add_parameter("id", id)
    return Order.from_dict(req.run())


def post_payment_request(client: Client, id: int, data: PaymentRequest | dict) -> Url:
    """Create a payment request for an online payment for the order.

    :param client: Ticketmatic API client.
    :param id: Order ID.
    :param data: Payment request parameters.
    :returns: A :class:`~ticketmatic.models.common.Url` for the payment
        page.
    """
    if isinstance(data, dict):
        data = PaymentRequest.from_dict(data)
    req = client.new_request("POST", "/{accountname}/orders/{id}/paymentrequest")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Url.from_dict(req.run())


def cancel_payment_request(client: Client, id: int) -> None:
    """Cancel the outstanding payment request for the order.

    A payment request can only be cancelled when its status is open.

    :param client: Ticketmatic API client.
    :param id: Order ID.
    """
    req = client.new_request("DELETE", "/{accountname}/orders/{id}/paymentrequest")
    req.add_parameter("id", id)
    req.run()


def get_document(client: Client, id: int, document_id: str, language: str) -> Url:
    """Get the PDF for a document for the order.

    :param client: Ticketmatic API client.
    :param id: Order ID.
    :param document_id: Document ID.
    :param language: Language code for the document.
    :returns: A :class:`~ticketmatic.models.common.Url` for the document
        PDF.
    """
    req = client.new_request(
        "GET", "/{accountname}/orders/{id}/documents/{documentid}/{language}"
    )
    req.add_parameter("id", id)
    req.add_parameter("documentid", document_id)
    req.add_parameter("language", language)
    return Url.from_dict(req.run())


def import_orders(
    client: Client, data: list[ImportOrder | dict]
) -> list[OrderImportStatus]:
    """Import historic orders.

    Up to 100 orders can be sent per call. Many of the usual consistency
    checks are relaxed while importing orders. It is recommended that you
    only import orders that will not be changed anymore in the future.

    :param client: Ticketmatic API client.
    :param data: List of orders to import.
    :returns: List of
        :class:`~ticketmatic.models.order.OrderImportStatus` results.
    """
    body = []
    for item in data:
        if isinstance(item, dict):
            item = ImportOrder.from_dict(item)
        body.append(item.to_dict())
    req = client.new_request("POST", "/{accountname}/orders/import")
    req.set_body(body)
    return unpack_array(OrderImportStatus, req.run())


def reserve(client: Client, data: OrderIdReservation | dict) -> OrderIdReservation:
    """Reserve order IDs.

    Importing orders with specified IDs is only possible when those IDs
    fall in the reserved ID range. Use this call to reserve a range of
    order IDs. Any unused ID lower than or equal to the specified ID will
    be reserved. New orders will receive IDs higher than the specified ID.

    :param client: Ticketmatic API client.
    :param data: ID reservation request.
    :returns: The resulting
        :class:`~ticketmatic.models.order.OrderIdReservation`.
    """
    if isinstance(data, dict):
        data = OrderIdReservation.from_dict(data)
    req = client.new_request("POST", "/{accountname}/orders/import/reserve")
    req.set_body(data.to_dict())
    return OrderIdReservation.from_dict(req.run())


def purge(client: Client, params: PurgeOrdersRequest | dict | None = None) -> Any:
    """Purge all orders.

    This is only possible for test or staging accounts.

    :param client: Ticketmatic API client.
    :param params: Optional purge filter parameters.
    :returns: The raw API response.
    """
    if params is None or isinstance(params, dict):
        params = PurgeOrdersRequest.from_dict(params or {})
    req = client.new_request("POST", "/{accountname}/orders/purge")
    req.add_query("contacts", params.contacts)
    req.add_query("createdsince", params.createdsince)
    req.add_query("events", params.events)
    return req.run()
