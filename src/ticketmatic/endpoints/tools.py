from __future__ import annotations

from typing import Any

from ticketmatic.client import Client
from ticketmatic.json_utils import unpack_array
from ticketmatic.models.common import AccountInfo, QueryRequest, QueryResult
from ticketmatic.models.order import TicketsprocessedRequest, TicketsprocessedStatistics


def account(client: Client) -> AccountInfo:
    req = client.new_request("GET", "/{accountname}/tools/account")
    return AccountInfo.from_dict(req.run())


def accounts(client: Client) -> list[AccountInfo]:
    req = client.new_request("GET", "/{accountname}/tools/accounts")
    return unpack_array(AccountInfo, req.run())


def queries(client: Client, data: QueryRequest | dict) -> QueryResult:
    if isinstance(data, dict):
        data = QueryRequest.from_dict(data)
    req = client.new_request("POST", "/{accountname}/tools/queries")
    req.set_body(data.to_dict())
    return QueryResult.from_dict(req.run())


def export(client: Client, data: QueryRequest | dict) -> Any:
    if isinstance(data, dict):
        data = QueryRequest.from_dict(data)
    req = client.new_request("POST", "/{accountname}/tools/export")
    req.set_body(data.to_dict())
    return req.run()


def tickets_processed_statistics(client: Client, data: TicketsprocessedRequest | dict) -> list[TicketsprocessedStatistics]:
    if isinstance(data, dict):
        data = TicketsprocessedRequest.from_dict(data)
    req = client.new_request("POST", "/{accountname}/tools/ticketsprocessedstatistics")
    req.set_body(data.to_dict())
    return unpack_array(TicketsprocessedStatistics, req.run())
