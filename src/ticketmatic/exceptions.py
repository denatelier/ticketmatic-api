from __future__ import annotations

import json
from typing import Any


class TicketmaticError(Exception):
    """Base exception for all Ticketmatic API errors."""


class ClientException(TicketmaticError):
    """Raised when the API returns a non-success HTTP status."""

    def __init__(self, code: int, body: str) -> None:
        self.application_code: str | None = None
        self.application_data: Any = None

        try:
            obj = json.loads(body)
            if isinstance(obj, dict) and "code" in obj and "message" in obj:
                self.application_code = obj.get("applicationcode")
                self.application_data = obj.get("applicationdata")
                super().__init__(obj["message"])
                self.code = obj["code"]
                return
        except (json.JSONDecodeError, TypeError):
            pass

        super().__init__(body)
        self.code = code


class RateLimitException(TicketmaticError):
    """Raised when the API returns HTTP 429."""

    def __init__(self, backoff: int) -> None:
        self.backoff = backoff
        super().__init__("Rate Limit Exceeded")


class VerifyException(TicketmaticError):
    """Raised when widget return URL verification fails."""

    def __init__(self, message: str) -> None:
        super().__init__(f"Failed to verify return URL: {message}")
