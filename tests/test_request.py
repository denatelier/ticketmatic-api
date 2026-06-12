"""Unit tests for the request layer (mocked HTTP, no credentials needed)."""

from __future__ import annotations

import hashlib
import hmac
import json
import re

import pytest
from pytest_httpx import HTTPXMock

from ticketmatic.client import Client
from ticketmatic.exceptions import ClientException, RateLimitException


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


def test_auth_header_is_valid_tm_hmac(client: Client, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(json={})

    client.new_request("GET", "/{accountname}/contacts").run()

    sent = httpx_mock.get_request()
    assert sent is not None
    match = re.fullmatch(
        r"TM-HMAC-SHA256 key=accesskey "
        r"ts=(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}) "
        r"sign=([0-9a-f]{64})",
        sent.headers["Authorization"],
    )
    assert match is not None
    ts, sign = match.groups()
    expected = hmac.new(
        b"secretkey",
        f"accesskeytestaccount{ts}".encode(),
        hashlib.sha256,
    ).hexdigest()
    assert sign == expected


def test_accept_language_header_sent_when_language_set(client: Client, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(json={})

    client.set_language("nl")
    client.new_request("GET", "/{accountname}/contacts").run()

    sent = httpx_mock.get_request()
    assert sent is not None
    assert sent.headers["Accept-Language"] == "nl"


def test_none_values_stripped_from_json_body(client: Client, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(json={})

    req = client.new_request("POST", "/{accountname}/contacts")
    req.set_body({"firstname": "John", "lastname": None})
    req.run()

    sent = httpx_mock.get_request()
    assert sent is not None
    assert json.loads(sent.content) == {"firstname": "John"}
    assert sent.headers["Content-Type"] == "application/json"


def test_dict_query_params_are_json_encoded(client: Client, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(json={})

    req = client.new_request("GET", "/{accountname}/orders")
    req.add_query("filter", {"status": ["open"]})
    req.run()

    sent = httpx_mock.get_request()
    assert sent is not None
    assert sent.url.params["filter"] == '{"status": ["open"]}'


def test_json_error_body_maps_to_client_exception(client: Client, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        status_code=404,
        json={
            "code": 404,
            "message": "Contact not found",
            "applicationcode": "CONTACT_NOT_FOUND",
        },
    )

    with pytest.raises(ClientException) as exc_info:
        client.new_request("GET", "/{accountname}/contacts/{id}").run()

    assert exc_info.value.code == 404
    assert str(exc_info.value) == "Contact not found"
    assert exc_info.value.application_code == "CONTACT_NOT_FOUND"


def test_plain_text_error_body_maps_to_client_exception(client: Client, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(status_code=500, text="internal server error")

    with pytest.raises(ClientException) as exc_info:
        client.new_request("GET", "/{accountname}/contacts").run()

    assert exc_info.value.code == 500
    assert str(exc_info.value) == "internal server error"


def test_429_maps_to_rate_limit_exception(client: Client, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(status_code=429, headers={"retry-after": "60"})

    with pytest.raises(RateLimitException) as exc_info:
        client.new_request("GET", "/{accountname}/contacts").run()

    assert exc_info.value.backoff == 60
