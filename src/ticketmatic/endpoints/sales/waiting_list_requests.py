from __future__ import annotations

import dataclasses
from typing import Any

from ticketmatic.client import Client
from ticketmatic.json_utils import unpack_array
from ticketmatic.models.stream_models import WaitingListRequest, WaitingListRequestQuery


@dataclasses.dataclass
class WaitingListRequestsList:
    data: list[WaitingListRequest]
    nbrofresults: int

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> WaitingListRequestsList:
        return cls(
            data=unpack_array(WaitingListRequest, data.get("data", [])),
            nbrofresults=int(data.get("nbrofresults", 0)),
        )


def get_list(client: Client, params: WaitingListRequestQuery | dict | None = None) -> WaitingListRequestsList:
    if params is None or isinstance(params, dict):
        params = WaitingListRequestQuery.from_dict(params or {})
    req = client.new_request("GET", "/{accountname}/sales/waitinglistrequests")
    req.add_query("filter", params.filter)
    req.add_query("includearchived", params.includearchived)
    req.add_query("lastupdatesince", params.lastupdatesince)
    return WaitingListRequestsList.from_dict(req.run())


def get(client: Client, id: int) -> WaitingListRequest:
    req = client.new_request("GET", "/{accountname}/sales/waitinglistrequests/{id}")
    req.add_parameter("id", id)
    return WaitingListRequest.from_dict(req.run())


def create(client: Client, data: WaitingListRequest | dict) -> WaitingListRequest:
    if isinstance(data, dict):
        data = WaitingListRequest.from_dict(data)
    req = client.new_request("POST", "/{accountname}/sales/waitinglistrequests")
    req.set_body(data.to_dict())
    return WaitingListRequest.from_dict(req.run())


def update(client: Client, id: int, data: WaitingListRequest | dict) -> WaitingListRequest:
    if isinstance(data, dict):
        data = WaitingListRequest.from_dict(data)
    req = client.new_request("PUT", "/{accountname}/sales/waitinglistrequests/{id}")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return WaitingListRequest.from_dict(req.run())


def delete(client: Client, id: int) -> None:
    req = client.new_request("DELETE", "/{accountname}/sales/waitinglistrequests/{id}")
    req.add_parameter("id", id)
    req.run()
