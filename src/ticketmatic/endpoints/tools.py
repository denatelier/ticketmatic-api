"""Miscellaneous tools for retrieving information from the account."""

from __future__ import annotations

from typing import Any

from ticketmatic.client import Client
from ticketmatic.json_utils import unpack_array
from ticketmatic.models.common import AccountInfo, QueryRequest, QueryResult
from ticketmatic.models.order import TicketsprocessedRequest, TicketsprocessedStatistics


def account(client: Client) -> AccountInfo:
    """Get account information.

    Get information of the current account, including account ID and full
    name.

    :param client: Ticketmatic API client.
    :returns: The current account as an
        :class:`~ticketmatic.models.common.AccountInfo`.
    """
    req = client.new_request("GET", "/{accountname}/tools/account")
    return AccountInfo.from_dict(req.run())


def accounts(client: Client) -> list[AccountInfo]:
    """Get authorized accounts.

    Gets an overview of all authorized accounts for this API key.

    **Note:** This method is not specific to an account. Use a separate API
    client with an empty string (``""``) as the account shortname.

    :param client: Ticketmatic API client.
    :returns: List of :class:`~ticketmatic.models.common.AccountInfo` objects.
    """
    req = client.new_request("GET", "/{accountname}/tools/accounts")
    return unpack_array(AccountInfo, req.run())


def queries(client: Client, data: QueryRequest | dict) -> QueryResult:
    """Execute a query on the public data model.

    Use this method to execute random (read-only) queries on the public data
    model. Not intended for long-running queries or large result sets; an
    exception is returned if the query executes too long or uses too much
    memory.

    :param client: Ticketmatic API client.
    :param data: Query parameters as a
        :class:`~ticketmatic.models.common.QueryRequest` or dict.
    :returns: The query result as a
        :class:`~ticketmatic.models.common.QueryResult`.
    """
    if isinstance(data, dict):
        data = QueryRequest.from_dict(data)
    req = client.new_request("POST", "/{accountname}/tools/queries")
    req.set_body(data.to_dict())
    return QueryResult.from_dict(req.run())


def export(client: Client, data: QueryRequest | dict) -> Any:
    """Export a query on the public data model.

    Executes a query against the public data model and exports the results
    as a stream of JSON lines (each line is a JSON object representing one
    row of the query result).

    :param client: Ticketmatic API client.
    :param data: Query parameters as a
        :class:`~ticketmatic.models.common.QueryRequest` or dict.
    :returns: A raw stream of the query results.
    """
    if isinstance(data, dict):
        data = QueryRequest.from_dict(data)
    req = client.new_request("POST", "/{accountname}/tools/export")
    req.set_body(data.to_dict())
    return req.run()


def tickets_processed_statistics(
    client: Client, data: TicketsprocessedRequest | dict
) -> list[TicketsprocessedStatistics]:
    """Get statistics on the tickets processed during a certain period.

    Retrieves the statistics on the number of tickets processed and sold
    online during a given period. Results can be grouped by day or month
    and are often used as the basis for invoicing or reporting.

    :param client: Ticketmatic API client.
    :param data: Request parameters as a
        :class:`~ticketmatic.models.order.TicketsprocessedRequest` or dict.
    :returns: List of
        :class:`~ticketmatic.models.order.TicketsprocessedStatistics` objects.
    """
    if isinstance(data, dict):
        data = TicketsprocessedRequest.from_dict(data)
    req = client.new_request("POST", "/{accountname}/tools/ticketsprocessedstatistics")
    req.set_body(data.to_dict())
    return unpack_array(TicketsprocessedStatistics, req.run())
