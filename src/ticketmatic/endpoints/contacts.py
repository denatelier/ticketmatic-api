"""Contact manipulation operations."""

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
    """Paged list of :class:`~ticketmatic.models.contact.Contact` objects."""

    data: list[Contact]
    """Result data."""
    nbrofresults: int
    """Total number of results available without considering limit and offset,
    useful for paging.
    """

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ContactsList:
        """Construct a :class:`ContactsList` from a raw API response dict."""
        return cls(
            data=unpack_array(Contact, data.get("data", [])),
            nbrofresults=int(data.get("nbrofresults", 0)),
        )


def get_list(client: Client, params: ContactQuery | dict | None = None) -> ContactsList:
    """Get a list of contacts.

    :param client: Ticketmatic API client.
    :param params: Optional query parameters.
    :returns: A :class:`ContactsList` with paged results.
    """
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


def get(
    client: Client, id: int, params: ContactGetQuery | dict | None = None
) -> Contact:
    """Get a single contact.

    To retrieve a contact based on the e-mail address, pass ``0`` as the id
    and supply an ``email`` parameter.

    :param client: Ticketmatic API client.
    :param id: Contact ID (pass ``0`` to look up by e-mail).
    :param params: Optional query parameters (e.g. ``email``).
    :returns: The requested :class:`~ticketmatic.models.contact.Contact`.
    """
    if params is None or isinstance(params, dict):
        params = ContactGetQuery.from_dict(params or {})
    req = client.new_request("GET", "/{accountname}/contacts/{id}")
    req.add_parameter("id", id)
    req.add_query("email", params.email)
    return Contact.from_dict(req.run())


def create(client: Client, data: Contact | dict) -> Contact:
    """Create a new contact.

    :param client: Ticketmatic API client.
    :param data: Contact data to create.
    :returns: The newly created :class:`~ticketmatic.models.contact.Contact`.
    """
    if isinstance(data, dict):
        data = Contact.from_dict(data)
    req = client.new_request("POST", "/{accountname}/contacts")
    req.set_body(data.to_dict())
    return Contact.from_dict(req.run())


def update(client: Client, id: int, data: Contact | dict) -> Contact:
    """Update a contact.

    :param client: Ticketmatic API client.
    :param id: Contact ID.
    :param data: Updated contact data.
    :returns: The updated :class:`~ticketmatic.models.contact.Contact`.
    """
    if isinstance(data, dict):
        data = Contact.from_dict(data)
    req = client.new_request("PUT", "/{accountname}/contacts/{id}")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return Contact.from_dict(req.run())


def delete(client: Client, id: int) -> None:
    """Remove a contact.

    Contacts are archivable: this call will not actually delete the object
    from the database. Instead it will mark the contact as deleted, which
    means it will not show up anymore in most places.

    :param client: Ticketmatic API client.
    :param id: Contact ID.
    """
    req = client.new_request("DELETE", "/{accountname}/contacts/{id}")
    req.add_parameter("id", id)
    req.run()


def batch(client: Client, data: BatchContactOperation | dict) -> None:
    """Apply batch operations to a set of contacts.

    The parameters required are specific to the type of operation. The
    operation will be applied to the contacts with the given IDs (up to
    1000 per call).

    Supported operations include ``addrelationtypes``,
    ``removerelationtypes``, ``delete``, ``subscribe``, ``unsubscribe``,
    ``sendselection``, ``update``, and ``merge``.

    :param client: Ticketmatic API client.
    :param data: Batch operation descriptor.
    """
    if isinstance(data, dict):
        data = BatchContactOperation.from_dict(data)
    req = client.new_request("POST", "/{accountname}/contacts/batch")
    req.set_body(data.to_dict())
    req.run()


def import_contacts(
    client: Client, data: list[Contact | dict]
) -> list[ContactImportStatus]:
    """Import contacts.

    Up to 1000 contacts can be sent per call.

    :param client: Ticketmatic API client.
    :param data: List of contacts to import.
    :returns: List of
        :class:`~ticketmatic.models.contact.ContactImportStatus` results.
    """
    body = []
    for item in data:
        if isinstance(item, dict):
            item = Contact.from_dict(item)
        body.append(item.to_dict())
    req = client.new_request("POST", "/{accountname}/contacts/import")
    req.set_body(body)
    return unpack_array(ContactImportStatus, req.run())


def reserve(client: Client, data: ContactIdReservation | dict) -> ContactIdReservation:
    """Reserve contact IDs.

    Importing contacts with the specified IDs is only possible when those
    IDs fall in the reserved ID range. Use this call to reserve a range of
    contact IDs. Any unused ID lower than or equal to the specified ID will
    be reserved. New contacts will receive IDs higher than the specified ID.

    :param client: Ticketmatic API client.
    :param data: ID reservation request.
    :returns: The resulting
        :class:`~ticketmatic.models.contact.ContactIdReservation`.
    """
    if isinstance(data, dict):
        data = ContactIdReservation.from_dict(data)
    req = client.new_request("POST", "/{accountname}/contacts/import/reserve")
    req.set_body(data.to_dict())
    return ContactIdReservation.from_dict(req.run())


def get_remark(client: Client, id: int, remark_id: str) -> ContactRemark:
    """Get a remark.

    Gets a specific remark for this contact.

    :param client: Ticketmatic API client.
    :param id: Contact ID.
    :param remark_id: Remark ID.
    :returns: The requested :class:`~ticketmatic.models.contact.ContactRemark`.
    """
    req = client.new_request("GET", "/{accountname}/contacts/{id}/remarks/{remarkid}")
    req.add_parameter("id", id)
    req.add_parameter("remarkid", remark_id)
    return ContactRemark.from_dict(req.run())


def create_remark(client: Client, id: int, data: ContactRemark | dict) -> ContactRemark:
    """Create a remark.

    Creates a remark for this contact.

    :param client: Ticketmatic API client.
    :param id: Contact ID.
    :param data: Remark data.
    :returns: The created :class:`~ticketmatic.models.contact.ContactRemark`.
    """
    if isinstance(data, dict):
        data = ContactRemark.from_dict(data)
    req = client.new_request("POST", "/{accountname}/contacts/{id}/remarks")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    return ContactRemark.from_dict(req.run())


def update_remark(
    client: Client, id: int, remark_id: str, data: ContactRemark | dict
) -> ContactRemark:
    """Update a remark.

    Updates a specific remark for this contact.

    :param client: Ticketmatic API client.
    :param id: Contact ID.
    :param remark_id: Remark ID.
    :param data: Updated remark data.
    :returns: The updated :class:`~ticketmatic.models.contact.ContactRemark`.
    """
    if isinstance(data, dict):
        data = ContactRemark.from_dict(data)
    req = client.new_request("PUT", "/{accountname}/contacts/{id}/remarks/{remarkid}")
    req.add_parameter("id", id)
    req.add_parameter("remarkid", remark_id)
    req.set_body(data.to_dict())
    return ContactRemark.from_dict(req.run())


def delete_remark(client: Client, id: int, remark_id: str) -> None:
    """Delete a remark.

    Deletes a specific remark for this contact.

    :param client: Ticketmatic API client.
    :param id: Contact ID.
    :param remark_id: Remark ID.
    """
    req = client.new_request(
        "DELETE", "/{accountname}/contacts/{id}/remarks/{remarkid}"
    )
    req.add_parameter("id", id)
    req.add_parameter("remarkid", remark_id)
    req.run()
