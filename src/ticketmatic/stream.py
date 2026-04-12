from __future__ import annotations

import json
from typing import Any, Iterator

import httpx


class Stream:
    """Iterator over a newline-delimited JSON streaming response.

    Yields parsed JSON objects one per line. Usage::

        stream = request.stream()
        for item in stream:
            print(item)
    """

    def __init__(
        self,
        method: str,
        url: str,
        headers: dict[str, str],
        content: bytes | None,
    ) -> None:
        self._client = httpx.Client(timeout=None)
        self._response = self._client.stream(
            method,
            url,
            headers=headers,
            content=content,
        )
        self._stream = self._response.__enter__()
        self._lines: Iterator[str] = self._stream.iter_lines()

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
        """Close the underlying HTTP connection."""
        self._response.__exit__(None, None, None)
        self._client.close()

    def __enter__(self) -> Stream:
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()

    def __del__(self) -> None:
        self.close()
