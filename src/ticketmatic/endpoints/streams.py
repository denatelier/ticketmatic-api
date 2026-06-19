"""Event stream to poll events in the account."""

from __future__ import annotations

from ticketmatic.client import Client
from ticketmatic.models.stream_models import EventstreamRequest, EventstreamResult


def eventstream(
    client: Client, params: EventstreamRequest | dict | None = None
) -> EventstreamResult:
    """Poll the event stream.

    Poll the account event stream to retrieve events that have occurred.

    :param client: Ticketmatic API client.
    :param params: Optional query parameters as an
        :class:`~ticketmatic.models.stream_models.EventstreamRequest` or dict.
    :returns: The poll result as an
        :class:`~ticketmatic.models.stream_models.EventstreamResult`.
    """
    if params is None or isinstance(params, dict):
        params = EventstreamRequest.from_dict(params or {})
    req = client.new_request("GET", "/{accountname}/eventstream")
    req.add_query("id", params.id)
    req.add_query("eventtypes", params.eventtypes)
    req.add_query("ts", params.ts)
    return EventstreamResult.from_dict(req.run())
