"""Data models for ticket layouts, ticket sales flows, and web sales skins."""

from __future__ import annotations

import dataclasses
from datetime import datetime
from typing import Any

from ticketmatic.models.base import Model


@dataclasses.dataclass
class TicketLayout(Model):
    """A single ticket layout."""

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new ticket layout.

    **Note:** Ignored when updating an existing ticket layout.
    """
    typeid: int | None = None
    """Type ID.

    **Note:** Ignored when updating an existing ticket layout.
    """
    name: str | None = None
    """Name for the ticket layout."""
    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new ticket layout.

    **Note:** Ignored when updating an existing ticket layout.
    """
    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new ticket layout.

    **Note:** Ignored when updating an existing ticket layout.
    """
    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new ticket layout.

    **Note:** Ignored when updating an existing ticket layout.
    """


@dataclasses.dataclass
class TicketLayoutQuery(Model):
    """Set of parameters used to filter ticket layouts."""

    typeid: int | None = None
    """Only return items with the given typeid."""
    filter: str | None = None
    """Filter the returned items by specifying a query on the public datamodel
    that returns the ids.
    """
    includearchived: bool | None = None
    """If this parameter is true, archived items will be returned as well."""
    lastupdatesince: datetime | None = None
    """All items that were updated since this timestamp will be returned.
    Timestamp should be passed in ``YYYY-MM-DD hh:mm:ss`` format.
    """


@dataclasses.dataclass
class TicketLayoutTemplate(Model):
    """A single ticket layout template."""

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new ticket layout template.

    **Note:** Ignored when updating an existing ticket layout template.
    """
    typeid: int | None = None
    """Type ID.

    **Note:** Ignored when updating an existing ticket layout template.
    """
    name: str | None = None
    """Name for the ticket layout template."""
    css: str | None = None
    """CSS classes for the ticket layout template.

    **Note:** Not set when retrieving a list of ticket layout templates.
    """
    deliveryscenarios: list[int] | None = None
    """Delivery scenarios for which this ticket layout template will be used."""
    htmltemplate: str | None = None
    """HTML template containing the definition for the ticket layout template.

    **Note:** Not set when retrieving a list of ticket layout templates.
    """
    ticketsperpage: int | None = None
    """Number of tickets to be printed per page."""
    translations: list[str] | None = None
    """Translations for the ticket layout template.

    **Note:** Not set when retrieving a list of ticket layout templates.
    """
    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new ticket layout template.

    **Note:** Ignored when updating an existing ticket layout template.
    """
    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new ticket layout template.

    **Note:** Ignored when updating an existing ticket layout template.
    """
    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new ticket layout template.

    **Note:** Ignored when updating an existing ticket layout template.
    """


@dataclasses.dataclass
class TicketLayoutTemplateQuery(Model):
    """Set of parameters used to filter ticket layout templates."""

    typeid: int | None = None
    """Only return items with the given typeid."""
    filter: str | None = None
    """Filter the returned items by specifying a query on the public datamodel
    that returns the ids.
    """
    includearchived: bool | None = None
    """If this parameter is true, archived items will be returned as well."""
    lastupdatesince: datetime | None = None
    """All items that were updated since this timestamp will be returned.
    Timestamp should be passed in ``YYYY-MM-DD hh:mm:ss`` format.
    """


@dataclasses.dataclass
class TicketsalesFlowConfig(Model):
    """Config for a ticket sales flow."""

    from_: datetime | None = None
    """Start timestamp for this config."""
    until: datetime | None = None
    """End timestamp for this config."""
    widget: str | None = None
    """Widget to use in this config."""
    widgetparams: list[str] | None = None
    """Widget parameters for this config."""

    @classmethod
    def from_dict(cls, data: dict | None) -> TicketsalesFlowConfig | None:
        if data is None:
            return None
        from ticketmatic.json_utils import unpack_timestamp

        return cls(
            from_=unpack_timestamp(data.get("from")),
            until=unpack_timestamp(data.get("until")),
            widget=data.get("widget"),
            widgetparams=data.get("widgetparams"),
        )

    def to_dict(self) -> dict[str, Any]:
        from ticketmatic.json_utils import pack_timestamp

        result: dict[str, Any] = {}
        if self.from_ is not None:
            result["from"] = pack_timestamp(self.from_)
        if self.until is not None:
            result["until"] = pack_timestamp(self.until)
        if self.widget is not None:
            result["widget"] = self.widget
        if self.widgetparams is not None:
            result["widgetparams"] = self.widgetparams
        return result


@dataclasses.dataclass
class Ticketsalesflow(Model):
    """A single ticketsalesflow."""

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new ticketsalesflow.

    **Note:** Ignored when updating an existing ticketsalesflow.
    """
    name: str | None = None
    """Name."""
    availabilityfielddefinition: str | None = None
    """Field definition used to define the availability of events for this
    flow.
    """
    code: str | None = None
    """Unique code used for the flow.

    Should only contain lower case letters and digits.
    """
    config: list[TicketsalesFlowConfig] | None = None
    """Config for the flow."""
    description: str | None = None
    """Description."""
    productavailability: list[int] | None = None
    """For flows with supported parameter ``product``: the set of product
    types for which this flow is available.
    """
    supportedparameters: list[str] | None = None
    """Supported parameters for the flow."""
    testmode: bool | None = None
    """Whether or not the flow is in test mode."""
    ticketsalessetupid: int | None = None
    """Ticket sales setup this flow belongs to."""


@dataclasses.dataclass
class TicketsalesflowQuery(Model):
    """Set of parameters used to filter ticketsalesflows."""

    filter: str | None = None
    """Filter the returned items by specifying a query on the public datamodel
    that returns the ids.
    """
    lastupdatesince: datetime | None = None
    """All items that were updated since this timestamp will be returned.
    Timestamp should be passed in ``YYYY-MM-DD hh:mm:ss`` format.
    """


@dataclasses.dataclass
class Ticketsalessetup(Model):
    """A single ticketsalessetup."""

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new ticketsalessetup.

    **Note:** Ignored when updating an existing ticketsalessetup.
    """
    name: str | None = None
    """Name."""
    code: str | None = None
    """Unique code used for the public link to the ticketsalessetup docs."""
    integrated: bool | None = None
    """Whether or not the ticket sales setup is integrated with the website."""
    widgetparams: list[str] | None = None
    """Widget parameters used for all flows in this setup."""


@dataclasses.dataclass
class TicketsalessetupQuery(Model):
    """Set of parameters used to filter ticketsalessetups."""

    filter: str | None = None
    """Filter the returned items by specifying a query on the public datamodel
    that returns the ids.
    """
    lastupdatesince: datetime | None = None
    """All items that were updated since this timestamp will be returned.
    Timestamp should be passed in ``YYYY-MM-DD hh:mm:ss`` format.
    """


# --- Web Sales Skins ---


@dataclasses.dataclass
class WebSalesSkinConfiguration(Model):
    """Configuration settings and parameters for a web sales skin."""

    favicon: str | None = None
    """Asset path to favicon image."""
    googleanalyticsid: str | None = None
    """Deprecated, use Google Tag Manager."""
    googletagmanagerid: str | None = None
    """Google Tag Manager ID. Can be left blank."""
    title: str | None = None
    """Page title."""


@dataclasses.dataclass
class WebSalesSkin(Model):
    """A single web sales skin."""

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new web sales skin.

    **Note:** Ignored when updating an existing web sales skin.
    """
    name: str | None = None
    """Name of the web sales skin."""
    asseturl: str | None = None
    """The URL where the assets are stored for this web skin. This property
    is readonly.

    **Note:** Ignored when creating a new web sales skin.

    **Note:** Ignored when updating an existing web sales skin.

    **Note:** Not set when retrieving a list of web sales skins.
    """
    configuration: WebSalesSkinConfiguration | None = None
    """Skin configuration.

    See the :class:`~ticketmatic.models.ticket.WebSalesSkinConfiguration`
    reference for an overview of all possible options.

    **Note:** Not set when retrieving a list of web sales skins.
    """
    css: str | None = None
    """CSS style rules. Should always include the ``style`` import.

    **Note:** Not set when retrieving a list of web sales skins.
    """
    html: str | None = None
    """HTML template of the skin.

    **Note:** Not set when retrieving a list of web sales skins.
    """
    translations: list[str] | None = None
    """A map of language codes to gettext ``.po`` files.

    **Note:** Not set when retrieving a list of web sales skins.
    """
    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new web sales skin.

    **Note:** Ignored when updating an existing web sales skin.
    """
    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new web sales skin.

    **Note:** Ignored when updating an existing web sales skin.
    """


@dataclasses.dataclass
class WebSalesSkinQuery(Model):
    """Set of parameters used to filter web sales skins."""

    filter: str | None = None
    """Filter the returned items by specifying a query on the public datamodel
    that returns the ids.
    """
    lastupdatesince: datetime | None = None
    """All items that were updated since this timestamp will be returned.
    Timestamp should be passed in ``YYYY-MM-DD hh:mm:ss`` format.
    """
