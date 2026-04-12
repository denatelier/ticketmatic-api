from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ticketmatic.request import Request


class Client:
    """Ticketmatic API REST client.

    Usage::

        client = Client("myaccount", "access_key", "secret_key")
    """

    server: str = "https://apps.ticketmatic.com"
    version: str = "1"
    BUILD: str = "1.0.0"

    def __init__(
        self,
        account_code: str,
        access_key: str,
        secret_key: str,
    ) -> None:
        self.account_code = account_code
        self.access_key = access_key
        self.secret_key = secret_key
        self.language: str | None = None

    def new_request(self, method: str, url: str) -> Request:
        from ticketmatic.request import Request

        return Request(self, method, url)

    def set_language(self, lang: str) -> None:
        self.language = lang
