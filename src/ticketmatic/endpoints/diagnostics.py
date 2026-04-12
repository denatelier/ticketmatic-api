from __future__ import annotations

from ticketmatic.client import Client
from ticketmatic.models.common import Timestamp


def time(client: Client) -> Timestamp:
    req = client.new_request("GET", "/{accountname}/diagnostics/time")
    return Timestamp.from_dict(req.run())
