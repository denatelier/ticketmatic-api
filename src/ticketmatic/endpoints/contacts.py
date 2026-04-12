from __future__ import annotations

import dataclasses
from typing import Any

from ticketmatic.client import Client
from ticketmatic.json_utils import unpack_array
from ticketmatic.models.contact import (
    BatchContactOperation,
    Contact,
    ContactGetQuery,
    ContactIdReservation,
    ContactImportStatus,
    ContactQuery,
    ContactRemark,
)


@dataclasses.dataclass
class ContactsList:
    data: list[Contact]
    nbrofresults: int

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ContactsList:
        return cls(
            data=unpack_array(Contact, data.get("data", [])),
            nbrofresults=int(data.get("nbrofresults", 0)),
        )


def get_list(client: Client, params: ContactQuery | dict | None = None) -> ContactsList:
    if params is None or isinstance(params, dict):
        params = ContactQuery.from_dict(params or {})
    req = client.new_request("GET", "/{accountname}/contacts")
    req.add_query("filter", params.filter)
    req.add_query("includearchived", params.includearchived)
    req.add_query("lastupdatesince", params.lastupdatesince)
    req.add_query("limit", params.limit)
    req.add_query("offset", params.offset)
    req.add_query("orderby", params.orderby)
    req.add_query("output", params.output)
    req.add_query("searchterm", params.searchterm)
    return ContactsList.from_dict(req.run())


def get(client: Client, id: int, params: ContactGetQuery | dict | None = None) -> Contact:
    if params is None or isinstance(params, dict):
        params = ContactGetQuery.from_dict(params or {})
    req = client.new_request("GET", "/{accountname}/contacts/{id}")
    req.add_parameter("id", id)
    req.add_query("email", params.email)
    return Contact.from_dict(req.run())


def create(client: Client, data: Contact | dict) -> Contact:
    if isinstance(data, dict):
        data = Contact.from_dict(data)
    req = client.new_request("POST", "/{accountname}/contacts")
    req.set_body(data.to_dict())
    return Contact.from_dict(req.run())


def update(client: Client, id: int, data: Contact | dict) -> Contact:
    if isinstance(data, dict):
        data = Contact.from_dict(data)
    req = client.new_request("PUT", "/{accountname}/contacts/{id}")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Contact.from_dict(req.run())


def delete(client: Client, id: int) -> None:
    req = client.new_request("DELETE", "/{accountname}/contacts/{id}")
    req.add_parameter("id", id)
    req.run()


def batch(client: Client, data: BatchContactOperation | dict) -> None:
    if isinstance(data, dict):
        data = BatchContactOperation.from_dict(data)
    req = client.new_request("POST", "/{accountname}/contacts/batch")
    req.set_body(data.to_dict())
    req.run()


def import_contacts(client: Client, data: list[Contact | dict]) -> list[ContactImportStatus]:
    body = []
    for item in data:
        if isinstance(item, dict):
            item = Contact.from_dict(item)
        body.append(item.to_dict())
    req = client.new_request("POST", "/{accountname}/contacts/import")
    req.set_body(body)
    return unpack_array(ContactImportStatus, req.run())


def reserve(client: Client, data: ContactIdReservation | dict) -> ContactIdReservation:
    if isinstance(data, dict):
        data = ContactIdReservation.from_dict(data)
    req = client.new_request("POST", "/{accountname}/contacts/import/reserve")
    req.set_body(data.to_dict())
    return ContactIdReservation.from_dict(req.run())


def get_remark(client: Client, id: int, remark_id: str) -> ContactRemark:
    req = client.new_request("GET", "/{accountname}/contacts/{id}/remarks/{remarkid}")
    req.add_parameter("id", id)
    req.add_parameter("remarkid", remark_id)
    return ContactRemark.from_dict(req.run())


def create_remark(client: Client, id: int, data: ContactRemark | dict) -> ContactRemark:
    if isinstance(data, dict):
        data = ContactRemark.from_dict(data)
    req = client.new_request("POST", "/{accountname}/contacts/{id}/remarks")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return ContactRemark.from_dict(req.run())


def update_remark(client: Client, id: int, remark_id: str, data: ContactRemark | dict) -> ContactRemark:
    if isinstance(data, dict):
        data = ContactRemark.from_dict(data)
    req = client.new_request("PUT", "/{accountname}/contacts/{id}/remarks/{remarkid}")
    req.add_parameter("id", id)
    req.add_parameter("remarkid", remark_id)
    req.set_body(data.to_dict())
    return ContactRemark.from_dict(req.run())


def delete_remark(client: Client, id: int, remark_id: str) -> None:
    req = client.new_request("DELETE", "/{accountname}/contacts/{id}/remarks/{remarkid}")
    req.add_parameter("id", id)
    req.add_parameter("remarkid", remark_id)
    req.run()
