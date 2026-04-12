from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


def unpack_timestamp(value: str | None) -> datetime | None:
    """Parse an ISO-8601 timestamp string into a timezone-aware datetime."""
    if value is None:
        return None
    dt = datetime.fromisoformat(value)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def pack_timestamp(value: datetime | str | None) -> str | None:
    """Serialize a datetime back to an ISO-8601 string."""
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.isoformat()
    return value


def unpack_array(item_type: type, items: list[dict[str, Any]]) -> list:
    """Deserialize a list of dicts into a list of model instances.

    Expects *item_type* to have a ``from_dict`` classmethod.
    """
    return [item_type.from_dict(item) for item in items]
