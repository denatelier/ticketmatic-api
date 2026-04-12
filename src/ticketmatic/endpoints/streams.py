from __future__ import annotations

from typing import Any

from ticketmatic.client import Client
from ticketmatic.models.stream_models import EventstreamRequest, EventstreamResult


def eventstream(client: Client, params: EventstreamRequest | dict | None = None) -> EventstreamResult:
    if params is None or isinstance(params, dict):
        params = EventstreamRequest.from_dict(params or {})
    req = client.new_request("GET", "/{accountname}/eventstream")
    req.add_query("id", params.id)
    req.add_query("eventtypes", params.eventtypes)
    req.add_query("ts", params.ts)
    return EventstreamResult.from_dict(req.run())
