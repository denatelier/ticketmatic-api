from __future__ import annotations

from typing import Any

from ticketmatic.client import Client
from ticketmatic.endpoints.settings._crud import *
from ticketmatic.json_utils import unpack_array
from ticketmatic.models.seating import (
    LockTemplate,
    LogicalPlan,
    SeatDescriptionTemplate,
    SeatingPlan,
    SeatingPlanQuery,
)

_URL = "/{accountname}/settings/seatingplans/seatingplans"
_ITEM = "/{accountname}/settings/seatingplans/seatingplans/{id}"
SeatingPlansList = make_list_type(SeatingPlan)
_FIELDS = ["filter", "includearchived", "lastupdatesince"]


def get_list(
    client: Client, params: SeatingPlanQuery | dict | None = None
) -> SeatingPlansList:
    return crud_get_list(
        client, _URL, SeatingPlanQuery, params, SeatingPlansList, _FIELDS
    )


def get(client: Client, id: int) -> SeatingPlan:
    return crud_get(client, _ITEM, id, SeatingPlan)


def create(client: Client, data: SeatingPlan | dict) -> SeatingPlan:
    return crud_create(client, _URL, data, SeatingPlan)


def update(client: Client, id: int, data: SeatingPlan | dict) -> SeatingPlan:
    return crud_update(client, _ITEM, id, data, SeatingPlan)


def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)


def get_svg(client: Client, id: int) -> str:
    req = client.new_request("GET", f"{_ITEM}/svg")
    req.add_parameter("id", id)
    return req.run("svg")


def save_svg(client: Client, id: int, data: str | bytes) -> None:
    req = client.new_request("POST", f"{_ITEM}/svg")
    req.add_parameter("id", id)
    req.set_body(data, "svg")
    req.run()


def get_lock_templates(client: Client, id: int) -> list[LockTemplate]:
    req = client.new_request("GET", f"{_ITEM}/locktemplates")
    req.add_parameter("id", id)
    return unpack_array(LockTemplate, req.run())


def save_lock_templates(
    client: Client, id: int, data: list[LockTemplate | dict]
) -> list[LockTemplate]:
    body = [
        (
            item.to_dict()
            if isinstance(item, LockTemplate)
            else LockTemplate.from_dict(item).to_dict()
        )
        for item in data
    ]
    req = client.new_request("POST", f"{_ITEM}/locktemplates")
    req.add_parameter("id", id)
    req.set_body(body)
    return unpack_array(LockTemplate, req.run())


def get_seat_description_templates(
    client: Client, id: int
) -> list[SeatDescriptionTemplate]:
    req = client.new_request("GET", f"{_ITEM}/seatdescriptiontemplates")
    req.add_parameter("id", id)
    return unpack_array(SeatDescriptionTemplate, req.run())


def save_seat_description_templates(
    client: Client, id: int, data: list[SeatDescriptionTemplate | dict]
) -> list[SeatDescriptionTemplate]:
    body = [
        (
            item.to_dict()
            if isinstance(item, SeatDescriptionTemplate)
            else SeatDescriptionTemplate.from_dict(item).to_dict()
        )
        for item in data
    ]
    req = client.new_request("POST", f"{_ITEM}/seatdescriptiontemplates")
    req.add_parameter("id", id)
    req.set_body(body)
    return unpack_array(SeatDescriptionTemplate, req.run())


def get_logical_plan(client: Client, id: int) -> LogicalPlan:
    req = client.new_request("GET", f"{_ITEM}/logicalplan")
    req.add_parameter("id", id)
    return LogicalPlan.from_dict(req.run())


def save_logical_plan(client: Client, id: int, data: LogicalPlan | dict) -> LogicalPlan:
    if isinstance(data, dict):
        data = LogicalPlan.from_dict(data)
    req = client.new_request("POST", f"{_ITEM}/logicalplan")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return LogicalPlan.from_dict(req.run())


def purge(client: Client, id: int) -> None:
    req = client.new_request("PUT", f"{_ITEM}/purge")
    req.add_parameter("id", id)
    req.run()
