from __future__ import annotations

from ticketmatic.client import Client
from ticketmatic.models.common import JobResult


def get(client: Client, id: str) -> JobResult:
    req = client.new_request("GET", "/{accountname}/jobs/{id}")
    req.add_parameter("id", id)
    return JobResult.from_dict(req.run())
