"""Endpoint functions for settings products and product categories."""

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
from ticketmatic.models.product import (
    Product,
    ProductCategory,
    ProductCategoryQuery,
    ProductQuery,
)

_BASE = "/{accountname}/settings"
_PRODUCTS_URL = f"{_BASE}/products"
_PRODUCT_URL = f"{_BASE}/products/{{id}}"
_CAT_URL = f"{_BASE}/productcategories"
_CAT_ITEM_URL = f"{_BASE}/productcategories/{{id}}"

ProductsList = make_list_type(Product)
ProductCategoriesList = make_list_type(ProductCategory)

_PROD_QUERY_FIELDS = ["typeid", "filter", "includearchived", "lastupdatesince"]
_CAT_QUERY_FIELDS = ["filter", "includearchived", "lastupdatesince"]


# --- Products ---


def get_list(client: Client, params: ProductQuery | dict | None = None) -> ProductsList:
    """Get a list of products.

    :param client: Ticketmatic API client.
    :param params: Optional filter/query parameters.
    :returns: A :class:`ProductsList` with matching results.
    """
    return crud_get_list(
        client, _PRODUCTS_URL, ProductQuery, params, ProductsList, _PROD_QUERY_FIELDS
    )


def get(client: Client, id: int) -> Product:
    """Get a single product.

    :param client: Ticketmatic API client.
    :param id: Product ID.
    :returns: The requested :class:`~ticketmatic.models.product.Product`.
    """
    return crud_get(client, _PRODUCT_URL, id, Product)


def create(client: Client, data: Product | dict) -> Product:
    """Create a new product.

    :param client: Ticketmatic API client.
    :param data: Product data.
    :returns: The newly created
        :class:`~ticketmatic.models.product.Product`.
    """
    return crud_create(client, _PRODUCTS_URL, data, Product)


def update(client: Client, id: int, data: Product | dict) -> Product:
    """Modify an existing product.

    :param client: Ticketmatic API client.
    :param id: Product ID.
    :param data: Updated product data.
    :returns: The updated :class:`~ticketmatic.models.product.Product`.
    """
    return crud_update(client, _PRODUCT_URL, id, data, Product)


def delete(client: Client, id: int) -> None:
    """Remove a product.

    Products are archivable: this call will not actually delete the object
    from the database. Instead, it will mark the object as archived, which
    means it will not show up anymore in most places.

    :param client: Ticketmatic API client.
    :param id: Product ID.
    """
    crud_delete(client, _PRODUCT_URL, id)


def translations(client: Client, id: int) -> Any:
    """Fetch translatable fields for a product.

    Returns a dictionary with string values in all languages for each
    translatable field.

    :param client: Ticketmatic API client.
    :param id: Product ID.
    :returns: Dictionary of translatable field values keyed by language.
    """
    return crud_translations(client, f"{_PRODUCT_URL}/translate", id)


def translate(client: Client, id: int, data: dict) -> Any:
    """Update translations for a product.

    Sets updated translation strings.

    :param client: Ticketmatic API client.
    :param id: Product ID.
    :param data: Updated translation strings.
    :returns: Dictionary of updated translatable field values.
    """
    return crud_translate(client, f"{_PRODUCT_URL}/translate", id, data)


# --- Product Categories ---


def categories_get_list(
    client: Client, params: ProductCategoryQuery | dict | None = None
) -> ProductCategoriesList:
    """Get a list of product categories.

    :param client: Ticketmatic API client.
    :param params: Optional filter/query parameters.
    :returns: A :class:`ProductCategoriesList` with matching results.
    """
    return crud_get_list(
        client,
        _CAT_URL,
        ProductCategoryQuery,
        params,
        ProductCategoriesList,
        _CAT_QUERY_FIELDS,
    )


def categories_get(client: Client, id: int) -> ProductCategory:
    """Get a single product category.

    :param client: Ticketmatic API client.
    :param id: Product category ID.
    :returns: The requested
        :class:`~ticketmatic.models.product.ProductCategory`.
    """
    return crud_get(client, _CAT_ITEM_URL, id, ProductCategory)


def categories_create(client: Client, data: ProductCategory | dict) -> ProductCategory:
    """Create a new product category.

    :param client: Ticketmatic API client.
    :param data: Product category data.
    :returns: The newly created
        :class:`~ticketmatic.models.product.ProductCategory`.
    """
    return crud_create(client, _CAT_URL, data, ProductCategory)


def categories_update(
    client: Client, id: int, data: ProductCategory | dict
) -> ProductCategory:
    """Modify an existing product category.

    :param client: Ticketmatic API client.
    :param id: Product category ID.
    :param data: Updated product category data.
    :returns: The updated
        :class:`~ticketmatic.models.product.ProductCategory`.
    """
    return crud_update(client, _CAT_ITEM_URL, id, data, ProductCategory)


def categories_delete(client: Client, id: int) -> None:
    """Remove a product category.

    Product categories are archivable: this call will not actually delete
    the object from the database. Instead, it will mark the object as
    archived, which means it will not show up anymore in most places.

    :param client: Ticketmatic API client.
    :param id: Product category ID.
    """
    crud_delete(client, _CAT_ITEM_URL, id)


def categories_translations(client: Client, id: int) -> Any:
    """Fetch translatable fields for a product category.

    Returns a dictionary with string values in all languages for each
    translatable field.

    :param client: Ticketmatic API client.
    :param id: Product category ID.
    :returns: Dictionary of translatable field values keyed by language.
    """
    return crud_translations(client, f"{_CAT_ITEM_URL}/translate", id)


def categories_translate(client: Client, id: int, data: dict) -> Any:
    """Update translations for a product category.

    Sets updated translation strings.

    :param client: Ticketmatic API client.
    :param id: Product category ID.
    :param data: Updated translation strings.
    :returns: Dictionary of updated translatable field values.
    """
    return crud_translate(client, f"{_CAT_ITEM_URL}/translate", id, data)
