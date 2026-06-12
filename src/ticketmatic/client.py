from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

if TYPE_CHECKING:
    from ticketmatic.request import Request


class Client:
    """Ticketmatic API REST client.

    Usage::

        client = Client("myaccount", "access_key", "secret_key")

    Optional keyword arguments::

        client = Client(
            "myaccount",
            "access_key",
            "secret_key",
            server="https://qa.ticketmatic.com",  # default: Client.server
            timeout=10.0,                          # seconds, default: 30.0
        )

    Each client holds a pooled HTTP connection. Call :meth:`close` when done,
    or use the client as a context manager::

        with Client("myaccount", "access_key", "secret_key") as client:
            ...
    """

    server: str = "https://apps.ticketmatic.com"
    version: str = "1"
    BUILD: str = "1.0.0"

    def __init__(
        self,
        account_code: str,
        access_key: str,
        secret_key: str,
        *,
        server: str | None = None,
        timeout: float = 30.0,
    ) -> None:
        self.account_code = account_code
        self.access_key = access_key
        self.secret_key = secret_key
        self.language: str | None = None
        if server is not None:
            self.server = server
        self.timeout = timeout
        self._http = httpx.Client(timeout=timeout)

    def new_request(self, method: str, url: str) -> Request:
        from ticketmatic.request import Request

        return Request(self, method, url)

    def set_language(self, lang: str) -> None:
        self.language = lang

    def close(self) -> None:
        """Close the underlying HTTP connection pool."""
        self._http.close()

    def __enter__(self) -> Client:
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()
