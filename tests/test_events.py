import pytest

from ticketmatic import ClientException
from ticketmatic.endpoints import events
from ticketmatic.models.event import EventQuery

pytestmark = pytest.mark.integration


def test_batch(tm_client):
    event = events.create(
        tm_client,
        {
            "contingents": [{"amount": 100}],
            "locationid": 1,
            "name": "Example",
        },
    )
    assert event.name == "Example"
    assert event.contingents[0].amount == 100
    assert event.locationid == 1

    event2 = events.create(
        tm_client,
        {
            "contingents": [{"amount": 100}],
            "locationid": 1,
            "name": "Example2",
        },
    )
    assert event2.name == "Example2"

    events.batch(
        tm_client,
        {
            "ids": [event.id, event2.id],
            "operation": "update",
            "parameters": {"updatefields": [{"key": "locationid", "value": 2}]},
        },
    )


def test_create(tm_client):
    event = events.create(
        tm_client,
        {
            "contingents": [{"amount": 100}],
            "name": "Example",
        },
    )
    assert event.name == "Example"
    assert event.contingents[0].amount == 100


def test_get(tm_client):
    result = events.get_list(tm_client, EventQuery(output="withlookup"))
    assert len(result.data) > 0

    event = events.get(tm_client, result.data[0].id)
    assert event.id == result.data[0].id


def test_get_conditions(tm_client):
    req = events.get(tm_client, 777717)
    assert req.id == 777717
    assert (
        req.prices.contingents[0].pricetypes[0].saleschannels[0].conditions[0].type
        == "orderticketlimit"
    )


def test_get_draft(tm_client):
    event = events.create(tm_client, {"name": "Draft"})
    assert event.name == "Draft"

    result = events.get_list(
        tm_client,
        EventQuery(
            filter="select id from tm.event where nameen='Draft'",
            simplefilter={"status": [19001, 19002, 19003]},
        ),
    )
    assert len(result.data) > 0

    events.delete(tm_client, event.id)


def test_get_tickets(tm_client):
    result = events.get_list(tm_client)
    assert len(result.data) > 0

    with events.get_tickets(tm_client, result.data[0].id) as stream:
        list(stream)
    # Stream may be empty for some events, just verify it doesn't error


def test_delete_fixed_bundle_event(tm_client):
    with pytest.raises(ClientException) as exc_info:
        events.delete(tm_client, 777704)
    assert exc_info.value.code == 400


def test_lock_unlock_tickets(tm_client):
    result = events.get_list(
        tm_client,
        EventQuery(
            filter="select id from tm.event "
            "where seatingplanid is not null and id < 777800",
            limit=1,
            orderby="name",
            output="ids",
        ),
    )
    assert len(result.data) > 0

    with events.get_tickets(tm_client, result.data[0].id) as stream:
        tickets = list(stream)
    assert len(tickets) > 0

    events.lock_tickets(
        tm_client,
        result.data[0].id,
        {
            "locktypeid": 1,
            "ticketids": [tickets[0]["id"], tickets[1]["id"]],
        },
    )

    events.unlock_tickets(
        tm_client,
        result.data[0].id,
        {
            "ticketids": [tickets[0]["id"], tickets[1]["id"]],
        },
    )


def test_update_seat_rank_for_tickets(tm_client):
    result = events.get_list(
        tm_client,
        EventQuery(
            filter="select id from tm.event "
            "where seatingplanid is not null and id < 777800",
            limit=1,
            orderby="name",
            output="ids",
        ),
    )
    assert len(result.data) > 0

    with events.get_tickets(tm_client, result.data[0].id) as stream:
        tickets = list(stream)
    assert len(tickets) > 0

    events.update_seat_rank_for_tickets(
        tm_client,
        result.data[0].id,
        {
            "seatrankid": 3,
            "ticketids": [tickets[0]["id"], tickets[1]["id"]],
        },
    )
