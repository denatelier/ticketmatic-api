"""Endpoint functions for sales waiting list requests."""

from __future__ import annotations

import dataclasses
from typing import Any

from ticketmatic.client import Client
from ticketmatic.json_utils import unpack_array
from ticketmatic.models.stream_models import WaitingListRequest, WaitingListRequestQuery


@dataclasses.dataclass
class WaitingListRequestsList:
    """Paged list of :class:`~ticketmatic.models.stream_models.WaitingListRequest`
    results."""

    data: list[WaitingListRequest]
    """Result data."""

    nbrofresults: int
    """Total number of results available without considering limit and offset,
    useful for paging."""

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> WaitingListRequestsList:
        """Construct a :class:`WaitingListRequestsList` from a raw API response dict."""
        return cls(
            data=unpack_array(WaitingListRequest, data.get("data", [])),
            nbrofresults=int(data.get("nbrofresults", 0)),
        )


def get_list(
    client: Client, params: WaitingListRequestQuery | dict | None = None
) -> WaitingListRequestsList:
    """Get a list of waiting list requests.

    :param client: Ticketmatic API client.
    :param params: Optional filter/query parameters.
    :returns: A :class:`WaitingListRequestsList` with matching results.
    """
    if params is None or isinstance(params, dict):
        params = WaitingListRequestQuery.from_dict(params or {})
    req = client.new_request("GET", "/{accountname}/sales/waitinglistrequests")
    req.add_query("filter", params.filter)
    req.add_query("includearchived", params.includearchived)
    req.add_query("lastupdatesince", params.lastupdatesince)
    return WaitingListRequestsList.from_dict(req.run())


def get(client: Client, id: int) -> WaitingListRequest:
    """Get a single waiting list request.

    :param client: Ticketmatic API client.
    :param id: Waiting list request ID.
    :returns: The requested
        :class:`~ticketmatic.models.stream_models.WaitingListRequest`.
    """
    req = client.new_request("GET", "/{accountname}/sales/waitinglistrequests/{id}")
    req.add_parameter("id", id)
    return WaitingListRequest.from_dict(req.run())


def create(client: Client, data: WaitingListRequest | dict) -> WaitingListRequest:
    """Create a new waiting list request.

    :param client: Ticketmatic API client.
    :param data: Waiting list request data.
    :returns: The newly created
        :class:`~ticketmatic.models.stream_models.WaitingListRequest`.
    """
    if isinstance(data, dict):
        data = WaitingListRequest.from_dict(data)
    req = client.new_request("POST", "/{accountname}/sales/waitinglistrequests")
    req.set_body(data.to_dict())
    return WaitingListRequest.from_dict(req.run())


def update(
    client: Client, id: int, data: WaitingListRequest | dict
) -> WaitingListRequest:
    """Modify an existing waiting list request.

    :param client: Ticketmatic API client.
    :param id: Waiting list request ID.
    :param data: Updated waiting list request data.
    :returns: The updated
        :class:`~ticketmatic.models.stream_models.WaitingListRequest`.
    """
    if isinstance(data, dict):
        data = WaitingListRequest.from_dict(data)
    req = client.new_request("PUT", "/{accountname}/sales/waitinglistrequests/{id}")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return WaitingListRequest.from_dict(req.run())


def delete(client: Client, id: int) -> None:
    """Remove a waiting list request.

    Waiting list requests are archivable: this call will not actually delete
    the object from the database. Instead, it will mark the object as
    archived, which means it will not show up anymore in most places.

    :param client: Ticketmatic API client.
    :param id: Waiting list request ID.
    """
    req = client.new_request("DELETE", "/{accountname}/sales/waitinglistrequests/{id}")
    req.add_parameter("id", id)
    req.run()
