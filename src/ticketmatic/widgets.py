from __future__ import annotations

import hashlib
import hmac
from urllib.parse import quote

from ticketmatic.client import Client
from ticketmatic.exceptions import VerifyException


class Widgets:
    """Helper for signing widget URLs and verifying return URLs.

    Note: the access key and secret key for widgets are different from the
    ones used for API calls. You need a separate keypair to sign widgets.
    """

    def __init__(
        self,
        account_code: str,
        access_key: str,
        secret_key: str,
    ) -> None:
        self.account_code = account_code
        self.access_key = access_key
        self.secret_key = secret_key

    def generate_url(self, widget: str, parameters: dict[str, str]) -> str:
        """Build a signed widget URL."""
        signature = self._calculate_signature(parameters)

        url_params = [f"{k}={quote(v, safe='')}" for k, v in parameters.items()]
        url_params.append(f"accesskey={self.access_key}")
        url_params.append(f"signature={signature}")

        return (
            f"{Client.server}/widgets/{self.account_code}/{widget}"
            f"?{'&'.join(url_params)}"
        )

    def verify_return_url(self, parameters: dict[str, str]) -> None:
        """Verify a widget return URL signature.

        Raises :class:`~ticketmatic.exceptions.VerifyException` on failure.
        """
        params = dict(parameters)

        if params.get("accesskey") != self.access_key:
            raise VerifyException("Bad access key")

        del params["accesskey"]

        if "signature" not in params:
            raise VerifyException("Signature missing")

        sig = params.pop("signature")
        expected = self._calculate_signature(params)

        if expected != sig:
            raise VerifyException("Signature mismatch")

    def _calculate_signature(self, params: dict[str, str]) -> str:
        filtered = {k: v for k, v in params.items() if k not in ("l", "ordercode")}
        hash_input = "".join(f"{k}{v}" for k, v in sorted(filtered.items()))

        return hmac.new(
            self.secret_key.encode(),
            (self.access_key + self.account_code + hash_input).encode(),
            hashlib.sha256,
        ).hexdigest()
