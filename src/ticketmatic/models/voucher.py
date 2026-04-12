from __future__ import annotations

import dataclasses
from datetime import datetime
from typing import Any

from ticketmatic.models.base import Model


@dataclasses.dataclass
class VoucherValidity(Model):
    expiry_fixeddate: datetime | None = None
    expiry_monthsaftercreation: int | None = None
    maxusages: int | None = None
    maxusagesperevent: int | None = None


@dataclasses.dataclass
class VoucherCode(Model):
    code: str | None = None
    expiryts: datetime | None = None


@dataclasses.dataclass
class Voucher(Model):
    id: int | None = None
    typeid: int | None = None
    name: str | None = None
    codeformatid: int | None = None
    codeprefix: str | None = None
    description: str | None = None
    nbrofcodes: int | None = None
    ordervalidationscript: str | None = None
    paymentmethodid: int | None = None
    validity: VoucherValidity | None = None
    isarchived: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class VoucherQuery(Model):
    typeid: int | None = None
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None


@dataclasses.dataclass
class AddVoucherCodes(Model):
    amount: float | None = None
    codes: list[VoucherCode] | None = None
    count: int | None = None
    update: bool | None = None
