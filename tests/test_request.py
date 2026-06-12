"""Unit tests for the request layer (mocked HTTP, no credentials needed)."""

from __future__ import annotations

import pytest
from pytest_httpx import HTTPXMock

from ticketmatic.client import Client


@pytest.fixture
def client() -> Client:
    return Client("testaccount", "accesskey", "secretkey")


def test_bool_query_params_serialize_as_lowercase_json(client: Client, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(json={"data": [], "nbrofresults": 0})

    req = client.new_request("GET", "/{accountname}/contacts")
    req.add_query("includearchived", True)
    req.run()

    sent = httpx_mock.get_request()
    assert sent is not None
    url = str(sent.url)
    assert "includearchived=true" in url
    assert "includearchived=True" not in url


def test_false_query_params_serialize_as_lowercase_json(client: Client, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(json={})

    req = client.new_request("GET", "/{accountname}/contacts")
    req.add_query("includearchived", False)
    req.run()

    sent = httpx_mock.get_request()
    assert sent is not None
    assert "includearchived=false" in str(sent.url)


def test_path_parameters_are_url_escaped(client: Client, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(json={})

    req = client.new_request("GET", "/{accountname}/contacts/{id}/remarks/{remarkid}")
    req.add_parameter("id", 123)
    req.add_parameter("remarkid", "a/b c")
    req.run()

    sent = httpx_mock.get_request()
    assert sent is not None
    assert "/contacts/123/remarks/a%2Fb%20c" in sent.url.raw_path.decode()
