"""The Ticketmatic API client and its HTTP connection handling."""

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
        """Create a new :class:`~ticketmatic.request.Request` bound to this client.

        :param method: HTTP method (``GET``, ``POST``, ``PUT``, ``DELETE``).
        :param url: API path, with placeholders such as ``{accountname}`` and
            ``{id}`` that are filled in when the request is executed.
        :returns: A request ready to have parameters, query values and a body
            added before being run.
        """
        from ticketmatic.request import Request

        return Request(self, method, url)

    def set_language(self, lang: str) -> None:
        """Set the language for translated content returned by the API.

        :param lang: A language code (for example ``"en"`` or ``"nl"``) sent as
            the ``Accept-Language`` header on subsequent requests.
        """
        self.language = lang

    def close(self) -> None:
        """Close the underlying HTTP connection pool."""
        self._http.close()

    def __enter__(self) -> Client:
        """Enter the runtime context and return the client itself."""
        return self

    def __exit__(self, *exc: object) -> None:
        """Exit the runtime context, closing the connection pool."""
        self.close()
