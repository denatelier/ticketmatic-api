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
    return crud_get_list(client, _URL, VoucherQuery, params, VouchersList, _FIELDS)

def get(client: Client, id: int) -> Voucher:
    return crud_get(client, _ITEM, id, Voucher)

def create(client: Client, data: Voucher | dict) -> Voucher:
    return crud_create(client, _URL, data, Voucher)

def update(client: Client, id: int, data: Voucher | dict) -> Voucher:
    return crud_update(client, _ITEM, id, data, Voucher)

def delete(client: Client, id: int) -> None:
    crud_delete(client, _ITEM, id)

def translations(client: Client, id: int) -> Any:
    return crud_translations(client, f"{_ITEM}/translate", id)

def translate(client: Client, id: int, data: dict) -> Any:
    return crud_translate(client, f"{_ITEM}/translate", id, data)

def create_codes(client: Client, id: int, data: AddVoucherCodes | dict) -> None:
    if isinstance(data, dict):
        data = AddVoucherCodes.from_dict(data)
    req = client.new_request("POST", "/{accountname}/settings/vouchers/{id}/codes")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    req.run()

def deactivate_codes(client: Client, id: int, data: AddVoucherCodes | dict) -> None:
    if isinstance(data, dict):
        data = AddVoucherCodes.from_dict(data)
    req = client.new_request("DELETE", "/{accountname}/settings/vouchers/{id}/codes")
    req.add_parameter("id", id)
    req.set_body(data.to_dict())
    req.run()
