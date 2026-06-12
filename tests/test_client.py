"""Unit tests for Client configuration and connection management."""

from __future__ import annotations

import pytest
from pytest_httpx import HTTPXMock

from ticketmatic.client import Client


def test_server_can_be_set_per_instance(httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(json={})
    httpx_mock.add_response(json={})

    qa = Client("acc", "key", "secret", server="https://qa.example.com")
    prod = Client("acc", "key", "secret")

    qa.new_request("GET", "/{accountname}/contacts").run()
    prod.new_request("GET", "/{accountname}/contacts").run()

    urls = [str(r.url) for r in httpx_mock.get_requests()]
    assert urls[0].startswith("https://qa.example.com/api/1/")
    assert urls[1].startswith("https://apps.ticketmatic.com/api/1/")


def test_class_server_attribute_remains_the_default(httpx_mock: HTTPXMock) -> None:
    # Backward compatibility: Client.server = ... still sets the default
    original = Client.server
    try:
        Client.server = "https://qa.example.com"
        client = Client("acc", "key", "secret")

        httpx_mock.add_response(json={})
        client.new_request("GET", "/{accountname}/contacts").run()

        sent = httpx_mock.get_request()
        assert sent is not None
        assert str(sent.url).startswith("https://qa.example.com/api/1/")
    finally:
        Client.server = original


def test_timeout_is_configurable(httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(json={})

    client = Client("acc", "key", "secret", timeout=5.0)
    client.new_request("GET", "/{accountname}/contacts").run()

    sent = httpx_mock.get_request()
    assert sent is not None
    assert sent.extensions["timeout"]["read"] == 5.0


def test_requests_go_through_shared_pool_closed_by_close() -> None:
    client = Client("acc", "key", "secret")
    client.close()

    with pytest.raises(RuntimeError):
        client.new_request("GET", "/{accountname}/contacts").run()


def test_streams_go_through_shared_pool_closed_by_close() -> None:
    client = Client("acc", "key", "secret")
    client.close()

    with pytest.raises(RuntimeError):
        client.new_request("GET", "/{accountname}/events/1/tickets").stream()


def test_client_is_a_context_manager(httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(json={})

    with Client("acc", "key", "secret") as client:
        client.new_request("GET", "/{accountname}/contacts").run()

    with pytest.raises(RuntimeError):
        client.new_request("GET", "/{accountname}/contacts").run()
