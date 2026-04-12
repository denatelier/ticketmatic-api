from __future__ import annotations

import dataclasses
from datetime import datetime
from typing import Any, ClassVar

from ticketmatic.models.base import Model
from ticketmatic.models.common import KeyValueItem


@dataclasses.dataclass
class ProductVoucherValue(Model):
    amount: float | None = None
    voucherid: int | None = None


@dataclasses.dataclass
class ProductInstancePricetypeValue(Model):
    id: int | None = None
    # 'from' is a Python keyword, stored as-is in the dict
    from_: int | None = None

    @classmethod
    def from_dict(cls, data: dict | None) -> ProductInstancePricetypeValue | None:
        if data is None:
            return None
        return cls(
            id=data.get("id"),
            from_=data.get("from"),
        )

    def to_dict(self) -> dict[str, Any]:
        result: dict[str, Any] = {}
        if self.id is not None:
            result["id"] = self.id
        if self.from_ is not None:
            result["from"] = self.from_
        return result


@dataclasses.dataclass
class ProductInstanceValue(Model):
    max_price: float | None = None
    min_price: float | None = None
    price: float | None = None
    pricetypes: list[ProductInstancePricetypeValue] | None = None
    tickettypeprices: list[int] | None = None
    tickettypes: list[int] | None = None
    voucher: ProductVoucherValue | None = None


@dataclasses.dataclass
class ProductInstanceException(Model):
    properties: list[list[str]] | None = None
    value: ProductInstanceValue | None = None


@dataclasses.dataclass
class ProductInstancevalues(Model):
    default: ProductInstanceValue | None = None
    exceptions: list[ProductInstanceException] | None = None


@dataclasses.dataclass
class ProductProperty(Model):
    name: str | None = None
    description: str | None = None
    key: str | None = None
    values: list[KeyValueItem] | None = None


@dataclasses.dataclass
class Product(Model):
    _has_custom_fields: ClassVar[bool] = True

    id: int | None = None
    typeid: int | None = None
    categoryid: int | None = None
    layoutid: int | None = None
    name: str | None = None
    asksubscribers: bool | None = None
    code: str | None = None
    description: str | None = None
    groupbycustomfield: int | None = None
    image: str | None = None
    instancevalues: ProductInstancevalues | None = None
    maxadditionaltickets: int | None = None
    printtickets: bool | None = None
    properties: list[ProductProperty] | None = None
    queuetoken: int | None = None
    saleendts: datetime | None = None
    saleschannels: list[int] | None = None
    salestartts: datetime | None = None
    salestatusmessagesid: int | None = None
    shortdescription: str | None = None
    translations: list[str] | None = None
    isarchived: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None
    custom_fields: dict[str, Any] | None = None


@dataclasses.dataclass
class ProductQuery(Model):
    typeid: int | None = None
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None


@dataclasses.dataclass
class ProductCategory(Model):
    id: int | None = None
    name: str | None = None
    contactname: str | None = None
    contactnameplural: str | None = None
    nameplural: str | None = None
    isarchived: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class ProductCategoryQuery(Model):
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None
