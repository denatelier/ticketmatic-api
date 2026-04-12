from __future__ import annotations

import dataclasses
from typing import Any

from ticketmatic.client import Client
from ticketmatic.json_utils import unpack_array
from ticketmatic.models.event import (
    BatchEventOperation,
    Event,
    EventLockTickets,
    EventQuery,
    EventScanTicketsOut,
    EventTicket,
    EventTicketQuery,
    EventUnlockTickets,
    EventUpdateSeatRankForTickets,
)
from ticketmatic.stream import Stream


@dataclasses.dataclass
class EventsList:
    data: list[Event]
    nbrofresults: int

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> EventsList:
        return cls(
            data=unpack_array(Event, data.get("data", [])),
            nbrofresults=int(data.get("nbrofresults", 0)),
        )


def get_list(client: Client, params: EventQuery | dict | None = None) -> EventsList:
    if params is None or isinstance(params, dict):
        params = EventQuery.from_dict(params or {})
    req = client.new_request("GET", "/{accountname}/events")
    req.add_query("context", params.context)
    req.add_query("filter", params.filter)
    req.add_query("lastupdatesince", params.lastupdatesince)
    req.add_query("limit", params.limit)
    req.add_query("offset", params.offset)
    req.add_query("orderby", params.orderby)
    req.add_query("output", params.output)
    req.add_query("searchterm", params.searchterm)
    req.add_query("simplefilter", params.simplefilter)
    return EventsList.from_dict(req.run())


def get(client: Client, id: int) -> Event:
    req = client.new_request("GET", "/{accountname}/events/{id}")
    req.add_parameter("id", id)
    return Event.from_dict(req.run())


def create(client: Client, data: Event | dict) -> Event:
    if isinstance(data, dict):
        data = Event.from_dict(data)
    req = client.new_request("POST", "/{accountname}/events")
    req.set_body(data.to_dict())
    return Event.from_dict(req.run())


def update(client: Client, id: int, data: Event | dict) -> Event:
    if isinstance(data, dict):
        data = Event.from_dict(data)
    req = client.new_request("PUT", "/{accountname}/events/{id}")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Event.from_dict(req.run())


def batch(client: Client, data: BatchEventOperation | dict) -> None:
    if isinstance(data, dict):
        data = BatchEventOperation.from_dict(data)
    req = client.new_request("POST", "/{accountname}/events/batch")
    req.set_body(data.to_dict())
    req.run()


def delete(client: Client, id: int) -> None:
    req = client.new_request("DELETE", "/{accountname}/events/{id}")
    req.add_parameter("id", id)
    req.run()


def get_tickets(client: Client, id: int, params: EventTicketQuery | dict | None = None) -> Stream:
    if params is None or isinstance(params, dict):
        params = EventTicketQuery.from_dict(params or {})
    req = client.new_request("GET", "/{accountname}/events/{id}/tickets")
    req.add_parameter("id", id)
    req.add_query("simplefilter", params.simplefilter)
    return req.stream()


def batch_update_tickets(client: Client, id: int, data: list[EventTicket | dict]) -> None:
    body = []
    for item in data:
        if isinstance(item, dict):
            item = EventTicket.from_dict(item)
        body.append(item.to_dict())
    req = client.new_request("PUT", "/{accountname}/events/{id}/tickets/batch")
    req.add_parameter("id", id)
    req.set_body(body)
    req.run()


def lock_tickets(client: Client, id: int, data: EventLockTickets | dict) -> None:
    if isinstance(data, dict):
        data = EventLockTickets.from_dict(data)
    req = client.new_request("PUT", "/{accountname}/events/{id}/tickets/lock")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    req.run()


def unlock_tickets(client: Client, id: int, data: EventUnlockTickets | dict) -> None:
    if isinstance(data, dict):
        data = EventUnlockTickets.from_dict(data)
    req = client.new_request("PUT", "/{accountname}/events/{id}/tickets/unlock")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    req.run()


def update_seat_rank_for_tickets(client: Client, id: int, data: EventUpdateSeatRankForTickets | dict) -> None:
    if isinstance(data, dict):
        data = EventUpdateSeatRankForTickets.from_dict(data)
    req = client.new_request("PUT", "/{accountname}/events/{id}/tickets/seatrank")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    req.run()


def scan_tickets_out(client: Client, id: int, data: EventScanTicketsOut | dict) -> Any:
    if isinstance(data, dict):
        data = EventScanTicketsOut.from_dict(data)
    req = client.new_request("PUT", "/{accountname}/events/{id}/tickets/scanout")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return req.run()


def translations(client: Client, id: int) -> Any:
    req = client.new_request("GET", "/{accountname}/events/{id}/translate")
    req.add_parameter("id", id)
    return req.run()


def translate(client: Client, id: int, data: dict) -> Any:
    req = client.new_request("PUT", "/{accountname}/events/{id}/translate")
    req.add_parameter("id", id)
    req.set_body(data)
    return req.run()


def purge(client: Client, id: int) -> None:
    req = client.new_request("PUT", "/{accountname}/events/{id}/purge")
    req.add_parameter("id", id)
    req.run()


def save_image(client: Client, id: int, data: bytes) -> Any:
    req = client.new_request("POST", "/{accountname}/events/{id}/image")
    req.add_parameter("id", id)
    req.set_body(data, "jpg")
    return req.run()


def delete_image(client: Client, id: int) -> None:
    req = client.new_request("DELETE", "/{accountname}/events/{id}/image")
    req.add_parameter("id", id)
    req.run()
