"""Unit tests for streaming responses (mocked HTTP, no credentials needed)."""

from __future__ import annotations

import pytest
from pytest_httpx import HTTPXMock

from ticketmatic.client import Client
from ticketmatic.exceptions import ClientException, RateLimitException
from ticketmatic.stream import Stream


@pytest.fixture
def client() -> Client:
    return Client("testaccount", "accesskey", "secretkey")


def test_stream_iterates_ndjson(client: Client, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(text='{"id": 1}\n\n{"id": 2}\n')

    with client.new_request("GET", "/{accountname}/events/1/tickets").stream() as stream:
        items = list(stream)

    assert items == [{"id": 1}, {"id": 2}]


def test_stream_raises_client_exception_on_http_error(client: Client, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        status_code=401,
        json={"code": 401, "message": "Authentication failed"},
    )

    with pytest.raises(ClientException) as exc_info:
        client.new_request("GET", "/{accountname}/events/1/tickets").stream()

    assert exc_info.value.code == 401


def test_stream_raises_rate_limit_exception_on_429(client: Client, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(status_code=429, headers={"retry-after": "120"})

    with pytest.raises(RateLimitException) as exc_info:
        client.new_request("GET", "/{accountname}/events/1/tickets").stream()

    assert exc_info.value.backoff == 120


def test_stream_close_is_idempotent(client: Client, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(text='{"id": 1}\n')

    stream = client.new_request("GET", "/{accountname}/events/1/tickets").stream()
    list(stream)
    stream.close()
    stream.close()  # second close must be a no-op, not an error


def test_stream_del_on_partially_constructed_object_does_not_raise() -> None:
    # Simulates __init__ failing before attributes are set (e.g. connection error)
    stream = Stream.__new__(Stream)
    stream.__del__()
