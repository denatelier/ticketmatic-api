from __future__ import annotations

from typing import Any

from ticketmatic.client import Client
from ticketmatic.json_utils import unpack_array
from ticketmatic.models.stream_models import SubscriberCommunication, SubscriberSync


def sync(client: Client, data: list[SubscriberSync | dict]) -> list[SubscriberSync]:
    body = []
    for item in data:
        if isinstance(item, dict):
            item = SubscriberSync.from_dict(item)
        body.append(item.to_dict())
    req = client.new_request("POST", "/{accountname}/subscribers/sync")
    req.set_body(body)
    return unpack_array(SubscriberSync, req.run())


def communications(client: Client) -> list[SubscriberCommunication]:
    req = client.new_request("GET", "/{accountname}/subscribers/communications")
    return unpack_array(SubscriberCommunication, req.run())
