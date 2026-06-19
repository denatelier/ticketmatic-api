"""Endpoint functions for settings vouchers."""

from __future__ import annotations

from typing import Any

from ticketmatic.client import Client
from ticketmatic.endpoints.settings._crud import (
    crud_create,
    crud_delete,
    crud_get,
    crud_get_list,
    crud_translate,
    crud_translations,
    crud_update,
    make_list_type,
)
from ticketmatic.models.voucher import AddVoucherCodes, Voucher, VoucherQuery

_URL = "/{accountname}/settings/vouchers"
_ITEM = "/{accountname}/settings/vouchers/{id}"
VouchersList = make_list_type(Voucher)
_FIELDS = ["typeid", "filter", "includearchived", "lastupdatesince"]


def get_list(client: Client, params: VoucherQuery | dict | None = None) -> VouchersList:
    """Get a list of vouchers.

    :param client: Ticketmatic API client.
    :param params: Optional filter/query parameters.
    :returns: A :class:`VouchersList` with matching results.
    """
    return crud_get_list(client, _URL, VoucherQuery, params, VouchersList, _FIELDS)


def get(client: Client, id: int) -> Voucher:
    """Get a single voucher.

    :param client: Ticketmatic API client.
    :param id: Voucher ID.
    :returns: The requested :class:`~ticketmatic.models.voucher.Voucher`.
    """
    return crud_get(client, _ITEM, id, Voucher)


def create(client: Client, data: Voucher | dict) -> Voucher:
    """Create a new voucher.

    :param client: Ticketmatic API client.
    :param data: Voucher data.
    :returns: The newly created
        :class:`~ticketmatic.models.voucher.Voucher`.
    """
    return crud_create(client, _URL, data, Voucher)


def update(client: Client, id: int, data: Voucher | dict) -> Voucher:
    """Modify an existing voucher.

    :param client: Ticketmatic API client.
    :param id: Voucher ID.
    :param data: Updated voucher data.
    :returns: The updated :class:`~ticketmatic.models.voucher.Voucher`.
    """
    return crud_update(client, _ITEM, id, data, Voucher)


def delete(client: Client, id: int) -> None:
    """Remove a voucher.

    Vouchers are archivable: this call will not actually delete the object
    from the database. Instead, it will mark the object as archived, which
    means it will not show up anymore in most places.

    :param client: Ticketmatic API client.
    :param id: Voucher ID.
    """
    crud_delete(client, _ITEM, id)


def translations(client: Client, id: int) -> Any:
    """Fetch translatable fields for a voucher.

    Returns a dictionary with string values in all languages for each
    translatable field.

    :param client: Ticketmatic API client.
    :param id: Voucher ID.
    :returns: Dictionary of translatable field values keyed by language.
    """
    return crud_translations(client, f"{_ITEM}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    """Update translations for a voucher.

    Sets updated translation strings.

    :param client: Ticketmatic API client.
    :param id: Voucher ID.
    :param data: Updated translation strings.
    :returns: Dictionary of updated translatable field values.
    """
    return crud_translate(client, f"{_ITEM}/translate", id, data)


def create_codes(client: Client, id: int, data: AddVoucherCodes | dict) -> None:
    """Create voucher codes.

    Creates individual voucher codes. Codes will be randomly generated
    unless supplied.

    :param client: Ticketmatic API client.
    :param id: Voucher ID.
    :param data: Voucher code creation parameters.
    """
    if isinstance(data, dict):
        data = AddVoucherCodes.from_dict(data)
    req = client.new_request("POST", "/{accountname}/settings/vouchers/{id}/codes")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    req.run()


def deactivate_codes(client: Client, id: int, data: AddVoucherCodes | dict) -> None:
    """Deactivate voucher codes.

    Deactivates individual voucher codes.

    :param client: Ticketmatic API client.
    :param id: Voucher ID.
    :param data: Voucher codes to deactivate.
    """
    if isinstance(data, dict):
        data = AddVoucherCodes.from_dict(data)
    req = client.new_request("DELETE", "/{accountname}/settings/vouchers/{id}/codes")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    req.run()
