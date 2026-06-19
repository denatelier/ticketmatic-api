"""Python client library for the Ticketmatic API.

This package exposes the public entry points of the library: the
:class:`~ticketmatic.client.Client` used for all API calls, the
:class:`~ticketmatic.widgets.Widgets` helper for signing widget URLs, and the
exception hierarchy. Endpoint functions live under :mod:`ticketmatic.endpoints`
and data models under :mod:`ticketmatic.models`.
"""

from ticketmatic.client import Client
from ticketmatic.exceptions import ClientException, RateLimitException, VerifyException
from ticketmatic.widgets import Widgets

__all__ = [
    "Client",
    "Widgets",
    "ClientException",
    "RateLimitException",
    "VerifyException",
]
