"""Helpers to reduce boilerplate in settings CRUD endpoints."""

from __future__ import annotations

import dataclasses
from typing import Any

from ticketmatic.client import Client
from ticketmatic.json_utils import unpack_array


def make_list_type(item_type: type):
    """Dynamically create a ``{name}List`` dataclass for a paged list result.

    :param item_type: The model class of the items in the list.
    :returns: A dataclass with ``data`` and ``nbrofresults`` fields and a
        ``from_dict`` classmethod that deserializes the API response.
    """

    @dataclasses.dataclass
    class _List:
        data: list
        nbrofresults: int

        @classmethod
        def from_dict(cls, data: dict[str, Any]) -> _List:
            return cls(
                data=unpack_array(item_type, data.get("data", [])),
                nbrofresults=int(data.get("nbrofresults", 0)),
            )

    _List.__qualname__ = f"{item_type.__name__}List"
    _List.__name__ = f"{item_type.__name__}List"
    return _List


def crud_get_list(
    client: Client,
    url: str,
    query_model: type,
    params,
    list_type,
    query_fields: list[str],
):
    if params is None or isinstance(params, dict):
        params = query_model.from_dict(params or {})
    req = client.new_request("GET", url)
    for field in query_fields:
        req.add_query(field, getattr(params, field, None))
    return list_type.from_dict(req.run())


def crud_get(client: Client, url: str, id: int, model_type: type):
    req = client.new_request("GET", url)
    req.add_parameter("id", id)
    return model_type.from_dict(req.run())


def crud_create(client: Client, url: str, data, model_type: type):
    if isinstance(data, dict):
        data = model_type.from_dict(data)
    req = client.new_request("POST", url)
    req.set_body(data.to_dict())
    return model_type.from_dict(req.run())


def crud_update(client: Client, url: str, id: int, data, model_type: type):
    if isinstance(data, dict):
        data = model_type.from_dict(data)
    req = client.new_request("PUT", url)
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return model_type.from_dict(req.run())


def crud_delete(client: Client, url: str, id: int):
    req = client.new_request("DELETE", url)
    req.add_parameter("id", id)
    req.run()


def crud_translations(client: Client, url: str, id: int) -> Any:
    req = client.new_request("GET", url)
    req.add_parameter("id", id)
    return req.run()


def crud_translate(client: Client, url: str, id: int, data: dict) -> Any:
    req = client.new_request("PUT", url)
    req.add_parameter("id", id)
    req.set_body(data)
    return req.run()
