"""Endpoint functions for managing seating plans."""

from __future__ import annotations

from ticketmatic.client import Client
from ticketmatic.endpoints.settings._crud import (
    crud_create,
    crud_delete,
    crud_get,
    crud_get_list,
    crud_update,
    make_list_type,
)
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
    """Get a list of seating plans.

    :param client: Ticketmatic API client.
    :param params: Optional query/filter parameters.
    :returns: A list of
        :class:`~ticketmatic.models.seating.SeatingPlan` objects.
    """
    return crud_get_list(
        client, _URL, SeatingPlanQuery, params, SeatingPlansList, _FIELDS
    )


def get(client: Client, id: int) -> SeatingPlan:
    """Get a single seating plan.

    :param client: Ticketmatic API client.
    :param id: Seating plan ID.
    :returns: The requested
        :class:`~ticketmatic.models.seating.SeatingPlan`.
    """
    return crud_get(client, _ITEM, id, SeatingPlan)


def create(client: Client, data: SeatingPlan | dict) -> SeatingPlan:
    """Create a new seating plan.

    :param client: Ticketmatic API client.
    :param data: Seating plan data.
    :returns: The created
        :class:`~ticketmatic.models.seating.SeatingPlan`.
    """
    return crud_create(client, _URL, data, SeatingPlan)


def update(client: Client, id: int, data: SeatingPlan | dict) -> SeatingPlan:
    """Modify an existing seating plan.

    :param client: Ticketmatic API client.
    :param id: Seating plan ID.
    :param data: Updated seating plan data.
    :returns: The updated
        :class:`~ticketmatic.models.seating.SeatingPlan`.
    """
    return crud_update(client, _ITEM, id, data, SeatingPlan)


def delete(client: Client, id: int) -> None:
    """Remove a seating plan.

    Seating plans are archivable: this call won't actually delete the object
    from the database. Instead, it will mark the object as archived, which
    means it won't show up anymore in most places.

    :param client: Ticketmatic API client.
    :param id: Seating plan ID.
    """
    crud_delete(client, _ITEM, id)


def get_svg(client: Client, id: int) -> str:
    """Get the SVG for a seating plan zone.

    :param client: Ticketmatic API client.
    :param id: Seating plan ID.
    :returns: SVG content as a string.
    """
    req = client.new_request("GET", f"{_ITEM}/svg")
    req.add_parameter("id", id)
    return req.run("svg")


def save_svg(client: Client, id: int, data: str | bytes) -> None:
    """Update the SVG for a seating plan zone.

    :param client: Ticketmatic API client.
    :param id: Seating plan ID.
    :param data: SVG content to save.
    """
    req = client.new_request("POST", f"{_ITEM}/svg")
    req.add_parameter("id", id)
    req.set_body(data, "svg")
    req.run()


def get_lock_templates(client: Client, id: int) -> list[LockTemplate]:
    """Get the lock templates for a seating plan.

    :param client: Ticketmatic API client.
    :param id: Seating plan ID.
    :returns: List of :class:`~ticketmatic.models.seating.LockTemplate` objects.
    """
    req = client.new_request("GET", f"{_ITEM}/locktemplates")
    req.add_parameter("id", id)
    return unpack_array(LockTemplate, req.run())


def save_lock_templates(
    client: Client, id: int, data: list[LockTemplate | dict]
) -> list[LockTemplate]:
    """Save the lock templates for a seating plan.

    :param client: Ticketmatic API client.
    :param id: Seating plan ID.
    :param data: Lock templates to save.
    :returns: Saved list of
        :class:`~ticketmatic.models.seating.LockTemplate` objects.
    """
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
    """Get the seat description templates for a seating plan.

    :param client: Ticketmatic API client.
    :param id: Seating plan ID.
    :returns: List of
        :class:`~ticketmatic.models.seating.SeatDescriptionTemplate` objects.
    """
    req = client.new_request("GET", f"{_ITEM}/seatdescriptiontemplates")
    req.add_parameter("id", id)
    return unpack_array(SeatDescriptionTemplate, req.run())


def save_seat_description_templates(
    client: Client, id: int, data: list[SeatDescriptionTemplate | dict]
) -> list[SeatDescriptionTemplate]:
    """Save the seat description templates for a seating plan.

    :param client: Ticketmatic API client.
    :param id: Seating plan ID.
    :param data: Seat description templates to save.
    :returns: Saved list of
        :class:`~ticketmatic.models.seating.SeatDescriptionTemplate` objects.
    """
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
    """Get the logical plan for a seating plan zone.

    :param client: Ticketmatic API client.
    :param id: Seating plan ID.
    :returns: The :class:`~ticketmatic.models.seating.LogicalPlan`.
    """
    req = client.new_request("GET", f"{_ITEM}/logicalplan")
    req.add_parameter("id", id)
    return LogicalPlan.from_dict(req.run())


def save_logical_plan(client: Client, id: int, data: LogicalPlan | dict) -> LogicalPlan:
    """Update the logical plan for a seating plan zone.

    :param client: Ticketmatic API client.
    :param id: Seating plan ID.
    :param data: Logical plan data.
    :returns: The updated :class:`~ticketmatic.models.seating.LogicalPlan`.
    """
    if isinstance(data, dict):
        data = LogicalPlan.from_dict(data)
    req = client.new_request("POST", f"{_ITEM}/logicalplan")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return LogicalPlan.from_dict(req.run())


def purge(client: Client, id: int) -> None:
    """Purge a seating plan.

    :param client: Ticketmatic API client.
    :param id: Seating plan ID.
    """
    req = client.new_request("PUT", f"{_ITEM}/purge")
    req.add_parameter("id", id)
    req.run()
