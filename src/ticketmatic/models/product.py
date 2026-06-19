"""Data models for products and product categories."""

from __future__ import annotations

import dataclasses
from datetime import datetime
from typing import Any, ClassVar

from ticketmatic.models.base import Model
from ticketmatic.models.common import KeyValueItem


@dataclasses.dataclass
class ProductVoucherValue(Model):
    """Product voucher value."""

    amount: float | None = None
    """Amount (only used for vouchers of type Payment)."""

    voucherid: int | None = None
    """Voucher ID."""


@dataclasses.dataclass
class ProductInstancePricetypeValue(Model):
    """Product instance price type value."""

    id: int | None = None
    """Price type ID."""

    # 'from' is a Python keyword, stored as-is in the dict
    from_: int | None = None
    """Minimum amount from which the price type will be applied."""

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
    """Product instance value, used with products.

    It configures the price and the content of a product.
    """

    max_price: float | None = None
    """Maximum price for a variable payment voucher."""

    min_price: float | None = None
    """Minimum price for a variable payment voucher."""

    price: float | None = None
    """Price."""

    pricetypes: list[ProductInstancePricetypeValue] | None = None
    """Set of price type values (used in option bundle products)."""

    tickettypeprices: list[int] | None = None
    """Set of ticket type prices (used in fixed bundle products)."""

    tickettypes: list[int] | None = None
    """Set of ticket types (used in option bundle products)."""

    voucher: ProductVoucherValue | None = None
    """Voucher."""


@dataclasses.dataclass
class ProductInstanceException(Model):
    """Product instance value exception."""

    properties: list[list[str]] | None = None
    """Properties for which this exception is valid."""

    value: ProductInstanceValue | None = None
    """Value for this exception."""


@dataclasses.dataclass
class ProductInstancevalues(Model):
    """Product instance values."""

    default: ProductInstanceValue | None = None
    """Default value.

    This is used whenever no listed exception matches the selected variant
    of a product.
    """

    exceptions: list[ProductInstanceException] | None = None
    """Exceptions on the default values.

    Each exception lists the property values to match and the value lists
    the price (and optionally) other content (such as a voucher ID and the
    amount for a payment voucher).
    """


@dataclasses.dataclass
class ProductProperty(Model):
    """Product property."""

    name: str | None = None
    """Name."""

    description: str | None = None
    """Description."""

    key: str | None = None
    """Key."""

    values: list[KeyValueItem] | None = None
    """Values."""


@dataclasses.dataclass
class Product(Model):
    """A single product."""

    _has_custom_fields: ClassVar[bool] = True

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new product.

    **Note:** Ignored when updating an existing product.
    """

    typeid: int | None = None
    """Type ID.

    **Note:** Ignored when updating an existing product.
    """

    categoryid: int | None = None
    """Category for the product.

    Categories can be managed in account parameters and indicate the labels
    for a single and multiple product and also what labels to use for the
    holders of the product. If not set, the UI will fall back to default
    labels.
    """

    layoutid: int | None = None
    """Optional layout for the product.

    If not specified, there will be no ticket generated for the product.
    """

    name: str | None = None
    """Name for the product."""

    asksubscribers: bool | None = None
    """If true, subscriber info is requested for each bundle in web sales."""

    code: str | None = None
    """Unique 12-digit code for the product."""

    description: str | None = None
    """Description for the product."""

    groupbycustomfield: int | None = None
    """The custom field used to group the option bundle in the UI.

    Used in web sales and the back office.

    **Note:** Not set when retrieving a list of products.
    """

    image: str | None = None
    """Reference to product image.

    **Note:** Ignored when creating a new product.

    **Note:** Ignored when updating an existing product.

    **Note:** Not set when retrieving a list of products.
    """

    instancevalues: ProductInstancevalues | None = None
    """Instance values controlling the price and content of the product.

    All products should have a default instance value and a set of
    exceptions (if any). If no specific exception is found for the selected
    product, the default instance value is used.
    """

    maxadditionaltickets: int | None = None
    """Maximum number of individual tickets per event purchasable alongside
    this bundle.

    **Note:** Not set when retrieving a list of products.
    """

    printtickets: bool | None = None
    """If true, tickets for items that belong to the product will be printed
    when printing the product.
    """

    properties: list[ProductProperty] | None = None
    """Definition of possible properties for the product.

    A product can have one or more properties. Properties can be used to
    introduce variants of a product (for example, sizes of a t-shirt).
    """

    queuetoken: int | None = None
    """Queue ID.

    See rate limiting for more info.

    **Note:** Not set when retrieving a list of products.
    """

    saleendts: datetime | None = None
    """End of sales."""

    saleschannels: list[int] | None = None
    """Sales channels for which sales are active.

    **Note:** Not set when retrieving a list of products.
    """

    salestartts: datetime | None = None
    """Start of sales."""

    salestatusmessagesid: int | None = None
    """Sale status messages in use for this product."""

    shortdescription: str | None = None
    """Short description for the product."""

    translations: list[str] | None = None
    """Translations for the product properties.

    **Note:** Not set when retrieving a list of products.
    """

    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new product.

    **Note:** Ignored when updating an existing product.
    """

    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new product.

    **Note:** Ignored when updating an existing product.
    """

    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new product.

    **Note:** Ignored when updating an existing product.
    """

    custom_fields: dict[str, Any] | None = None
    """Custom field values keyed by name (``c_``-prefixed in the API)."""


@dataclasses.dataclass
class ProductQuery(Model):
    """Set of parameters used to filter products."""

    typeid: int | None = None
    """Only return items with the given type ID."""

    filter: str | None = None
    """Filter the returned items by specifying a query on the public data
    model that returns the IDs.
    """

    includearchived: bool | None = None
    """If this parameter is true, archived items will be returned as well."""

    lastupdatesince: datetime | None = None
    """All items updated since this timestamp will be returned.

    Timestamp should be passed in ``YYYY-MM-DD hh:mm:ss`` format.
    """


@dataclasses.dataclass
class ProductCategory(Model):
    """A single product category."""

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new product category.

    **Note:** Ignored when updating an existing product category.
    """

    name: str | None = None
    """Name for the product category."""

    contactname: str | None = None
    """Name for the holder/owner of this product."""

    contactnameplural: str | None = None
    """Name for the holder/owner of this product in plural."""

    nameplural: str | None = None
    """Name for the product category in plural."""

    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new product category.

    **Note:** Ignored when updating an existing product category.
    """

    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new product category.

    **Note:** Ignored when updating an existing product category.
    """

    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new product category.

    **Note:** Ignored when updating an existing product category.
    """


@dataclasses.dataclass
class ProductCategoryQuery(Model):
    """Set of parameters used to filter product categories."""

    filter: str | None = None
    """Filter the returned items by specifying a query on the public data
    model that returns the IDs.
    """

    includearchived: bool | None = None
    """If this parameter is true, archived items will be returned as well."""

    lastupdatesince: datetime | None = None
    """All items updated since this timestamp will be returned.

    Timestamp should be passed in ``YYYY-MM-DD hh:mm:ss`` format.
    """
