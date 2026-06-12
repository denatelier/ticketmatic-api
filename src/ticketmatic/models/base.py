from __future__ import annotations

import dataclasses
from datetime import datetime
from typing import Any, ClassVar, Self, get_type_hints

from ticketmatic.json_utils import pack_timestamp, unpack_timestamp


@dataclasses.dataclass
class Model:
    """Base class for all Ticketmatic API models.

    Provides automatic ``from_dict`` / ``to_dict`` conversion with support for:
    - Nested Model subclasses
    - ``datetime`` fields (ISO-8601 round-trip)
    - ``custom_fields`` with ``c_`` prefix stripping/restoring
    """

    # Subclasses that carry custom fields (c_ prefixed) set this to True.
    _has_custom_fields: ClassVar[bool] = False

    @classmethod
    def from_dict(cls, data: dict[str, Any] | Any | None) -> Self | None:
        if data is None:
            return None

        # httpx returns dicts, but handle raw objects from nested calls too
        if not isinstance(data, dict):
            data = dict(data) if hasattr(data, "__iter__") else data

        hints = get_type_hints(cls)
        kwargs: dict[str, Any] = {}

        for field in dataclasses.fields(cls):
            name = field.name
            if name.startswith("_"):
                continue

            raw = data.get(name)
            if raw is None:
                continue

            hint = hints.get(name)
            kwargs[name] = _coerce(raw, hint)

        # Extract custom fields (c_ prefix)
        if cls._has_custom_fields:
            custom: dict[str, Any] = {}
            for key, value in data.items():
                if key.startswith("c_"):
                    custom[key[2:]] = value
            if custom:
                kwargs["custom_fields"] = custom

        return cls(**kwargs)

    def to_dict(self) -> dict[str, Any]:
        result: dict[str, Any] = {}

        for field in dataclasses.fields(self):
            name = field.name
            if name.startswith("_"):
                continue
            if name == "custom_fields":
                continue

            value = getattr(self, name)
            if value is None:
                continue

            result[name] = _serialize(value)

        # Restore custom fields with c_ prefix
        custom = getattr(self, "custom_fields", None)
        if custom:
            for key, value in custom.items():
                result[f"c_{key}"] = value

        return result


def _coerce(value: Any, hint: Any) -> Any:
    """Coerce a raw JSON value into the expected Python type."""
    import types

    if value is None:
        return None

    # X | None (types.UnionType from PEP 604) -> unwrap to X
    if isinstance(hint, types.UnionType):
        args = hint.__args__
        non_none = [a for a in args if a is not type(None)]
        if len(non_none) == 1:
            return _coerce(value, non_none[0])
        return value

    origin = getattr(hint, "__origin__", None)

    # typing.Optional[X] / typing.Union[X, None]
    import typing

    if origin is typing.Union:
        args = hint.__args__
        non_none = [a for a in args if a is not type(None)]
        if len(non_none) == 1:
            return _coerce(value, non_none[0])
        return value

    # list[X]
    if origin is list:
        inner = hint.__args__[0] if hint.__args__ else None
        if inner and isinstance(inner, type) and issubclass(inner, Model):
            return [inner.from_dict(item) for item in value]
        if inner is datetime:
            return [unpack_timestamp(item) for item in value]
        return value

    # dict[str, X]
    if origin is dict:
        return value

    # datetime
    if hint is datetime:
        return unpack_timestamp(value)

    # Nested Model subclass
    if isinstance(hint, type) and issubclass(hint, Model):
        return hint.from_dict(value)

    return value


def _serialize(value: Any) -> Any:
    """Serialize a Python value back to JSON-compatible form."""
    if isinstance(value, Model):
        return value.to_dict()
    if isinstance(value, datetime):
        return pack_timestamp(value)
    if isinstance(value, list):
        return [_serialize(item) for item in value]
    if isinstance(value, dict):
        return {k: _serialize(v) for k, v in value.items()}
    return value
