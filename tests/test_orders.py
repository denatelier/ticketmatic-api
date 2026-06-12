import pytest

from ticketmatic.endpoints import events, orders
from ticketmatic.models.order import OrderQuery

pytestmark = pytest.mark.integration


def test_batch(tm_client):
    order = orders.create(tm_client, {"saleschannelid": 1})
    assert order.orderid != 0
    assert order.saleschannelid == 1

    order2 = orders.create(tm_client, {"saleschannelid": 1})
    assert order2.orderid != 0

    orders.batch(
        tm_client,
        {
            "ids": [order.orderid, order2.orderid],
            "operation": "update",
            "parameters": {"updatefields": [{"key": "deliveryscenarioid", "value": 1}]},
        },
    )


def test_get(tm_client):
    result = orders.get_list(tm_client, OrderQuery(output="withlookup"))
    assert len(result.data) > 0

    order = orders.get(tm_client, result.data[0].orderid)
    assert order.orderid == result.data[0].orderid

    result2 = orders.get_list(tm_client, OrderQuery(limit=100))
    assert len(result2.data) == 100


def test_create(tm_client):
    order = orders.create(tm_client, {"saleschannelid": 1})
    assert order.orderid != 0
    assert order.saleschannelid == 1

    updated = orders.update(
        tm_client,
        order.orderid,
        {
            "customerid": 777701,
            "deliveryscenarioid": 2,
            "paymentscenarioid": 3,
        },
    )
    assert updated.orderid == order.orderid
    assert updated.deliveryscenarioid == 2
    assert updated.paymentscenarioid == 3
    assert updated.customerid == 777701

    ttps = events.get(tm_client, 777701)
    assert ttps.id != 0

    ticketsadded = orders.add_tickets(
        tm_client,
        order.orderid,
        {
            "tickets": [
                {
                    "tickettypepriceid": ttps.prices.contingents[0]
                    .pricetypes[0]
                    .tickettypepriceid
                },
                {
                    "tickettypepriceid": ttps.prices.contingents[0]
                    .pricetypes[0]
                    .tickettypepriceid
                },
            ],
        },
    )
    assert len(ticketsadded.order["tickets"]) == 2

    orders.confirm(tm_client, order.orderid)

    ticket_ids = [ticketsadded.order["tickets"][0]["id"]]

    updated2 = orders.update_tickets(
        tm_client,
        order.orderid,
        {
            "operation": "setticketholders",
            "params": {"ticketholderids": [777701]},
            "tickets": ticket_ids,
        },
    )
    assert updated2.tickets[0].ticketholderid == 777701

    deleted = orders.delete_tickets(tm_client, order.orderid, {"tickets": ticket_ids})
    assert len(deleted.tickets) == 1


def test_split(tm_client):
    order = orders.create(tm_client, {"saleschannelid": 1})
    assert order.orderid != 0

    orders.update(
        tm_client,
        order.orderid,
        {
            "customerid": 777701,
            "deliveryscenarioid": 2,
            "paymentscenarioid": 3,
        },
    )

    ttps = events.get(tm_client, 777701)

    ticketsadded = orders.add_tickets(
        tm_client,
        order.orderid,
        {
            "tickets": [
                {
                    "tickettypepriceid": ttps.prices.contingents[0]
                    .pricetypes[0]
                    .tickettypepriceid
                },
                {
                    "tickettypepriceid": ttps.prices.contingents[0]
                    .pricetypes[0]
                    .tickettypepriceid
                },
            ],
        },
    )

    ticket_ids = [ticketsadded.order["tickets"][0]["id"]]

    orders.confirm(tm_client, order.orderid)

    split_order = orders.split(
        tm_client,
        order.orderid,
        {
            "deliveryscenarioid": 3,
            "tickets": ticket_ids,
        },
    )
    assert len(split_order.tickets) == 1
    assert split_order.deliveryscenarioid == 3
    assert split_order.paymentscenarioid == 3
