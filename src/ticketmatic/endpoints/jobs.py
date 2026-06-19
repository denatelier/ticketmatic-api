"""API calls for jobs."""

from __future__ import annotations

from ticketmatic.client import Client
from ticketmatic.models.common import JobResult


def get(client: Client, id: str) -> JobResult:
    """Get job.

    Returns info on a job including the current status.

    :param client: Ticketmatic API client.
    :param id: Job ID.
    :returns: The requested :class:`~ticketmatic.models.common.JobResult`.
    """
    req = client.new_request("GET", "/{accountname}/jobs/{id}")
    req.add_parameter("id", id)
    return JobResult.from_dict(req.run())
