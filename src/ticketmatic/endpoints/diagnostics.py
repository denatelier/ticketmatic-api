"""Diagnostic API calls to help while debugging."""

from __future__ import annotations

from ticketmatic.client import Client
from ticketmatic.models.common import Timestamp


def time(client: Client) -> Timestamp:
    """Get the backend time.

    Returns the current system time, in UTC, using the ISO-8601 format.

    This call does not require an ``Authorization`` header (it is the only
    call that allows this) and can be used to investigate timestamp issues
    when signing API requests.

    :param client: Ticketmatic API client.
    :returns: The current server time as a
        :class:`~ticketmatic.models.common.Timestamp`.
    """
    req = client.new_request("GET", "/{accountname}/diagnostics/time")
    return Timestamp.from_dict(req.run())
