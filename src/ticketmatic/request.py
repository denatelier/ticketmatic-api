"""Construction, signing and execution of a single Ticketmatic API request."""

from __future__ import annotations

import hashlib
import hmac
import json
from datetime import UTC, datetime
from typing import Any
from urllib.parse import quote

import httpx

from ticketmatic.client import Client
from ticketmatic.exceptions import ClientException, RateLimitException
from ticketmatic.stream import Stream


class Request:
    """Builds and executes a single Ticketmatic API request."""

    def __init__(self, client: Client, method: str, url: str) -> None:
        self._client = client
        self._method = method
        self._url = url
        self._parameters: dict[str, str] = {}
        self._query: dict[str, Any] = {}
        self._body: Any = None
        self._body_content_type: str = "json"

    def add_parameter(self, key: str, value: Any) -> None:
        """Set a URL path parameter (e.g. ``{id}``)."""
        self._parameters[key] = str(value)

    def add_query(self, key: str, value: Any) -> None:
        """Add a query-string parameter. ``None`` values are silently skipped."""
        if value is not None:
            self._query[key] = value

    def set_body(self, obj: Any, content_type: str = "json") -> None:
        self._body = obj
        self._body_content_type = content_type

    # ------------------------------------------------------------------
    # Execution
    # ------------------------------------------------------------------

    def run(self, content_type: str = "json") -> Any:
        """Execute the request and return the parsed response."""
        url, headers, content = self._prepare()

        response = self._client._http.request(
            self._method,
            url,
            headers=headers,
            content=content,
        )
        self._check_error(response)

        if content_type == "json":
            return response.json()
        return response.text

    def stream(self) -> Stream:
        """Execute the request and return a streaming iterator."""
        url, headers, content = self._prepare()
        return Stream(self._client._http, self._method, url, headers, content)

    # ------------------------------------------------------------------
    # Internals
    # ------------------------------------------------------------------

    def _prepare(self) -> tuple[str, dict[str, str], bytes | None]:
        """Return ``(url, headers, body_bytes)`` ready for httpx."""
        headers: dict[str, str] = {
            "User-Agent": f"ticketmatic/python ({Client.BUILD})",
            "Authorization": self._generate_auth_header(),
        }

        if self._client.language:
            headers["Accept-Language"] = self._client.language

        content: bytes | None = None
        if self._body is not None:
            if self._body_content_type == "json":
                # Strip None values from the body dict before encoding
                if isinstance(self._body, dict):
                    body = {k: v for k, v in self._body.items() if v is not None}
                elif isinstance(self._body, list):
                    body = self._body
                else:
                    body = self._body
                content = json.dumps(body).encode()
                headers["Content-Type"] = "application/json"
            elif self._body_content_type == "svg":
                content = (
                    self._body if isinstance(self._body, bytes) else self._body.encode()
                )
                headers["Content-Type"] = "image/svg+xml"
            elif self._body_content_type == "jpg":
                content = (
                    self._body if isinstance(self._body, bytes) else self._body.encode()
                )
                headers["Content-Type"] = "image/jpeg"

        url = self._generate_url()
        return url, headers, content

    def _generate_url(self) -> str:
        url = f"{self._client.server}/api/{self._client.version}{self._url}"

        # Substitute path parameters
        for key, value in self._parameters.items():
            url = url.replace(f"{{{key}}}", quote(value, safe=""))
        url = url.replace("{accountname}", quote(self._client.account_code, safe=""))

        # Append query string
        if self._query:
            parts: list[str] = []
            for key, value in self._query.items():
                if isinstance(value, bool):
                    parts.append(f"{key}={'true' if value else 'false'}")
                elif isinstance(value, (dict, list)):
                    parts.append(f"{key}={quote(json.dumps(value))}")
                else:
                    parts.append(f"{key}={quote(str(value))}")
            url += "?" + "&".join(parts)

        return url

    def _generate_auth_header(self) -> str:
        """Build a TM-HMAC-SHA256 Authorization header."""
        account_code = self._client.account_code
        access_key = self._client.access_key
        secret_key = self._client.secret_key

        ts = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%S")

        signature = hmac.new(
            secret_key.encode(),
            (access_key + account_code + ts).encode(),
            hashlib.sha256,
        ).hexdigest()

        return f"TM-HMAC-SHA256 key={access_key} ts={ts} sign={signature}"

    @staticmethod
    def _check_error(response: httpx.Response) -> None:
        if response.status_code == 429:
            backoff = int(response.headers.get("retry-after", "0"))
            raise RateLimitException(backoff)
        if response.status_code != 200:
            raise ClientException(response.status_code, response.text)
