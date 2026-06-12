from __future__ import annotations

import json
from collections.abc import Iterator
from typing import Any

import httpx

from ticketmatic.exceptions import ClientException, RateLimitException


class Stream:
    """Iterator over a newline-delimited JSON streaming response.

    Yields parsed JSON objects one per line. Usage::

        stream = request.stream()
        for item in stream:
            print(item)

    Raises :class:`~ticketmatic.exceptions.ClientException` or
    :class:`~ticketmatic.exceptions.RateLimitException` if the API
    responds with an error status.
    """

    def __init__(
        self,
        http: httpx.Client,
        method: str,
        url: str,
        headers: dict[str, str],
        content: bytes | None,
    ) -> None:
        # Marked False only once fully initialized, so close()/__del__ are
        # safe on partially-constructed instances.
        self._closed = True
        # Streams are long-lived; override the pool's default read timeout.
        self._response = http.stream(
            method,
            url,
            headers=headers,
            content=content,
            timeout=None,
        )
        self._stream = self._response.__enter__()
        self._closed = False

        try:
            self._check_error()
        except BaseException:
            self.close()
            raise

        self._lines: Iterator[str] = self._stream.iter_lines()

    def _check_error(self) -> None:
        if self._stream.status_code == 429:
            backoff = int(self._stream.headers.get("retry-after", "0"))
            raise RateLimitException(backoff)
        if self._stream.status_code != 200:
            self._stream.read()
            raise ClientException(self._stream.status_code, self._stream.text)

    def __iter__(self) -> Stream:
        return self

    def __next__(self) -> Any:
        """Return the next parsed JSON object from the stream."""
        # Skip blank lines
        while True:
            line = next(self._lines)  # raises StopIteration when exhausted
            line = line.strip()
            if line:
                return json.loads(line)

    def close(self) -> None:
        """Close the streaming response. Safe to call repeatedly.

        The shared connection pool is owned by the :class:`Client` and is
        left open.
        """
        if self._closed:
            return
        self._closed = True
        self._response.__exit__(None, None, None)

    def __enter__(self) -> Stream:
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()

    def __del__(self) -> None:
        if not getattr(self, "_closed", True):
            self.close()
