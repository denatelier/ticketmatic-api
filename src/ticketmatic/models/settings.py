"""Data models for Ticketmatic settings (custom fields, views, reports, etc.)."""

from __future__ import annotations

import dataclasses
from datetime import datetime
from typing import Any, ClassVar

from ticketmatic.models.base import Model

# --- Custom Fields ---


@dataclasses.dataclass
class CustomfieldAvailability(Model):
    """Configures in what sales channels a custom field is available during checkout.

    Availability can be further refined with an optional JavaScript script.
    """

    saleschannels: list[int] | None = None
    """Sales channels for which this custom field is available.

    If empty, the custom field will not be available.
    """

    script: str | None = None
    """JavaScript that must return a boolean, with the current order available."""

    usescript: bool | None = None
    """Indicates if the script will be used."""


@dataclasses.dataclass
class CustomField(Model):
    """A single custom field."""

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new custom field.

    **Note:** Ignored when updating an existing custom field.
    """

    typeid: int | None = None
    """Type ID.

    **Note:** Ignored when updating an existing custom field.
    """

    availability: CustomfieldAvailability | None = None
    """Rules that define when this custom field is available when edit type is
    ``checkout``.
    """

    caption: str | None = None
    """Human-readable name for the custom field."""

    description: str | None = None
    """Human-readable description for the custom field.

    Will be visible for end-users when edit type ``checkout`` is used.
    """

    edittypeid: int | None = None
    """Type of editing allowed for the custom field (links to system type 22xxx)."""

    fieldtypeid: int | None = None
    """Type of the custom field (links to system type 12xxx)."""

    key: str | None = None
    """Identifier for the custom field.

    Should contain only alphanumeric characters and no whitespace; max length is
    30 characters. The custom field will be available in the API and the public
    data model as ``c_<key>``.
    """

    manualsort: bool | None = None
    """Indicates whether the field is manually sortable."""

    requiredtypeid: int | None = None
    """Indicates where the custom field is required (links to system type 30xxx)."""

    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new custom field.

    **Note:** Ignored when updating an existing custom field.
    """

    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new custom field.

    **Note:** Ignored when updating an existing custom field.
    """

    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new custom field.

    **Note:** Ignored when updating an existing custom field.
    """


@dataclasses.dataclass
class CustomFieldQuery(Model):
    """Set of parameters used to filter custom fields."""

    typeid: int | None = None
    """Only return items with the given typeid."""

    filter: str | None = None
    """Filter the returned items by specifying a query on the public datamodel
    that returns the ids.
    """

    includearchived: bool | None = None
    """If this parameter is true, archived items will be returned as well."""

    lastupdatesince: datetime | None = None
    """All items updated since this timestamp will be returned.

    Timestamp should be passed in ``YYYY-MM-DD hh:mm:ss`` format.
    """


@dataclasses.dataclass
class CustomFieldValue(Model):
    """A single custom field value."""

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new custom field value.

    **Note:** Ignored when updating an existing custom field value.
    """

    typeid: int | None = None
    """Type ID.

    **Note:** Ignored when updating an existing custom field value.
    """

    caption: str | None = None
    """Human-readable name for the value."""

    sortorder: int | None = None
    """Indicates the manual sort order."""

    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new custom field value.

    **Note:** Ignored when updating an existing custom field value.
    """

    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new custom field value.

    **Note:** Ignored when updating an existing custom field value.
    """

    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new custom field value.

    **Note:** Ignored when updating an existing custom field value.
    """


@dataclasses.dataclass
class CustomFieldValueQuery(Model):
    """Set of parameters used to filter custom field values."""

    typeid: int | None = None
    """Only return items with the given typeid."""

    filter: str | None = None
    """Filter the returned items by specifying a query on the public datamodel
    that returns the ids.
    """

    includearchived: bool | None = None
    """If this parameter is true, archived items will be returned as well."""

    lastupdatesince: datetime | None = None
    """All items updated since this timestamp will be returned.

    Timestamp should be passed in ``YYYY-MM-DD hh:mm:ss`` format.
    """


# --- Delivery Scenarios ---


@dataclasses.dataclass
class DeliveryscenarioAvailability(Model):
    """Defines when a delivery scenario is available.

    Availability requires a set of sales channels (required) and may be further
    restricted by an optional JavaScript script.
    """

    saleschannels: list[int] | None = None
    """An array of sales channel IDs for which this delivery scenario can be used."""

    script: str | None = None
    """Script used to determine availability of the delivery scenario."""

    usescript: bool | None = None
    """Whether to use a script to further refine the set of sales channels."""


@dataclasses.dataclass
class DeliveryScenario(Model):
    """A single delivery scenario."""

    _has_custom_fields: ClassVar[bool] = True

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new delivery scenario.

    **Note:** Ignored when updating an existing delivery scenario.
    """

    typeid: int | None = None
    """The type of this delivery scenario, defines when this delivery scenario is
    triggered.
    """

    name: str | None = None
    """Name of the delivery scenario."""

    allowetickets: int | None = None
    """Indicates whether e-tickets are allowed with this delivery scenario."""

    availability: DeliveryscenarioAvailability | None = None
    """Rules that define when this scenario is available.

    **Note:** Not set when retrieving a list of delivery scenarios.
    """

    deliverystatusaftertrigger: int | None = None
    """The delivery status the order will transition to when the trigger occurs."""

    feedescription: str | None = None
    """A very short description of the fee that is applicable."""

    internalremark: str | None = None
    """An internal description field; will not be shown to customers."""

    logo: str | None = None
    """Logo URL."""

    mailorganization: bool | None = None
    """Whether to send mail to the organization if known."""

    needsaddress: bool | None = None
    """Indicates that a physical address is required."""

    ordermailtemplateid_delivery: int | None = None
    """ID of the order mail template sent when changing to delivery state
    ``delivered``. Can be 0 to indicate that no mail should be sent.
    """

    ordermailtemplateid_deliverystarted: int | None = None
    """ID of the order mail template sent when changing to delivery state
    ``delivery started``. Can be 0 to indicate that no mail should be sent.
    """

    shortdescription: str | None = None
    """A short description of the delivery scenario; will be shown to customers."""

    visibility: str | None = None
    """Visibility of this scenario; can be either ``FULL`` or ``API``."""

    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new delivery scenario.

    **Note:** Ignored when updating an existing delivery scenario.
    """

    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new delivery scenario.

    **Note:** Ignored when updating an existing delivery scenario.
    """

    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new delivery scenario.

    **Note:** Ignored when updating an existing delivery scenario.
    """

    custom_fields: dict[str, Any] | None = None
    """Custom field values keyed by name (``c_``-prefixed in the API)."""


@dataclasses.dataclass
class DeliveryScenarioQuery(Model):
    """Set of parameters used to filter delivery scenarios."""

    filter: str | None = None
    """Filter the returned items by specifying a query on the public datamodel
    that returns the ids.
    """

    includearchived: bool | None = None
    """If this parameter is true, archived items will be returned as well."""

    lastupdatesince: datetime | None = None
    """All items updated since this timestamp will be returned.

    Timestamp should be passed in ``YYYY-MM-DD hh:mm:ss`` format.
    """


# --- Documents ---


@dataclasses.dataclass
class DocumentOptions(Model):
    """Options for the document generation."""

    nbrperpage: int | None = None
    """Amount of documents per page."""


@dataclasses.dataclass
class Document(Model):
    """A single document."""

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new document.

    **Note:** Ignored when updating an existing document.
    """

    typeid: int | None = None
    """Type ID.

    **Note:** Ignored when updating an existing document.
    """

    name: str | None = None
    """Name of the document."""

    css: str | None = None
    """CSS content for the document template.

    **Note:** Not set when retrieving a list of documents.
    """

    description: str | None = None
    """Description of the document."""

    enabled: bool | None = None
    """Whether the document template is enabled."""

    htmltemplate: str | None = None
    """HTML content for the document template.

    **Note:** Not set when retrieving a list of documents.
    """

    options: DocumentOptions | None = None
    """Key-value options for the document (e.g. ``nbrperpage``).

    **Note:** Not set when retrieving a list of documents.
    """

    translations: list[str] | None = None
    """Translations for the document template.

    **Note:** Not set when retrieving a list of documents.
    """

    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new document.

    **Note:** Ignored when updating an existing document.
    """

    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new document.

    **Note:** Ignored when updating an existing document.
    """


@dataclasses.dataclass
class DocumentQuery(Model):
    """Set of parameters used to filter documents."""

    typeid: int | None = None
    """Only return items with the given typeid."""

    filter: str | None = None
    """Filter the returned items by specifying a query on the public datamodel
    that returns the ids.
    """

    lastupdatesince: datetime | None = None
    """All items updated since this timestamp will be returned.

    Timestamp should be passed in ``YYYY-MM-DD hh:mm:ss`` format.
    """


# --- Dupe Detect ---


@dataclasses.dataclass
class DupeDetectCriteria(Model):
    """Dupe detect criteria define how contact fields are matched."""

    field: str | None = None
    """The field on which to match."""

    matcher: str | None = None
    """Matcher used for the specified field."""


@dataclasses.dataclass
class DupeDetectRule(Model):
    """A single dupe detect rule."""

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new dupe detect rule.

    **Note:** Ignored when updating an existing dupe detect rule.
    """

    name: str | None = None
    """Rule name."""

    criteria: list[DupeDetectCriteria] | None = None
    """Criteria for matching; any contact that matches all criteria is listed as
    a match.
    """

    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new dupe detect rule.

    **Note:** Ignored when updating an existing dupe detect rule.
    """

    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new dupe detect rule.

    **Note:** Ignored when updating an existing dupe detect rule.
    """


@dataclasses.dataclass
class DupeDetectRuleQuery(Model):
    """Set of parameters used to filter dupe detect rules."""

    filter: str | None = None
    """Filter the returned items by specifying a query on the public datamodel
    that returns the ids.
    """

    lastupdatesince: datetime | None = None
    """All items updated since this timestamp will be returned.

    Timestamp should be passed in ``YYYY-MM-DD hh:mm:ss`` format.
    """


# --- Field Definitions ---


@dataclasses.dataclass
class FieldDefinition(Model):
    """A single field definition."""

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new field definition.

    **Note:** Ignored when updating an existing field definition.
    """

    typeid: int | None = None
    """Type ID.

    **Note:** Ignored when updating an existing field definition.
    """

    align: str | None = None
    """Alignment when used in a view; values can be ``left``, ``right``, or
    ``center``.
    """

    description: str | None = None
    """Human-readable name for the field definition."""

    key: str | None = None
    """Key for the field definition; should only consist of lowercase alphanumeric
    characters.
    """

    sqlclause: str | None = None
    """The SQL clause that retrieves the information element from the database."""

    uitype: str | None = None
    """Decides how the field will be rendered when used in a view."""

    variablewidth: bool | None = None
    """Indicates whether the column width can be adapted when stretching a view
    across the full available width.
    """

    width: int | None = None
    """Width of the field definition when used in a view."""

    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new field definition.

    **Note:** Ignored when updating an existing field definition.
    """

    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new field definition.

    **Note:** Ignored when updating an existing field definition.
    """

    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new field definition.

    **Note:** Ignored when updating an existing field definition.
    """


@dataclasses.dataclass
class FieldDefinitionQuery(Model):
    """Set of parameters used to filter field definitions."""

    typeid: int | None = None
    """Only return items with the given typeid."""

    filter: str | None = None
    """Filter the returned items by specifying a query on the public datamodel
    that returns the ids.
    """

    includearchived: bool | None = None
    """If this parameter is true, archived items will be returned as well."""

    lastupdatesince: datetime | None = None
    """All items updated since this timestamp will be returned.

    Timestamp should be passed in ``YYYY-MM-DD hh:mm:ss`` format.
    """


@dataclasses.dataclass
class FielddefinitionsDataRequest(Model):
    """Info for requesting field definition data for one or more items."""

    typeid: int | None = None
    """Type ID."""

    fielddefinitions: list[str] | None = None
    """Keys for field definitions to retrieve."""

    ids: list[int] | None = None
    """Item IDs."""


@dataclasses.dataclass
class FielddefinitionsDataResult(Model):
    """Data for field definitions for an item."""

    id: int | None = None
    """Item ID."""

    data: Any | None = None
    """Field definition data for the item."""


# --- Filter Definitions ---


@dataclasses.dataclass
class FilterDefinition(Model):
    """A single filter definition."""

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new filter definition.

    **Note:** Ignored when updating an existing filter definition.
    """

    typeid: int | None = None
    """Type ID.

    **Note:** Ignored when updating an existing filter definition.
    """

    checklistquery: str | None = None
    """SQL clause to retrieve the list of available values for checklist-type
    filters.
    """

    description: str | None = None
    """Name for the filter."""

    filtertype: int | None = None
    """The type of filter definition; defines the UI and resulting parameters
    used when a user selects the filter.
    """

    sqlclause: str | None = None
    """The SQL clause that defines how the filter will work."""

    visible: bool | None = None
    """Whether the filter is enabled (visible)."""

    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new filter definition.

    **Note:** Ignored when updating an existing filter definition.
    """

    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new filter definition.

    **Note:** Ignored when updating an existing filter definition.
    """

    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new filter definition.

    **Note:** Ignored when updating an existing filter definition.
    """


@dataclasses.dataclass
class FilterDefinitionQuery(Model):
    """Set of parameters used to filter filter definitions."""

    typeid: int | None = None
    """Only return items with the given typeid."""

    filter: str | None = None
    """Filter the returned items by specifying a query on the public datamodel
    that returns the ids.
    """

    includearchived: bool | None = None
    """If this parameter is true, archived items will be returned as well."""

    lastupdatesince: datetime | None = None
    """All items updated since this timestamp will be returned.

    Timestamp should be passed in ``YYYY-MM-DD hh:mm:ss`` format.
    """


# --- Opt-Ins ---


@dataclasses.dataclass
class OptInAvailability(Model):
    """Defines the sales channel in which an opt-in is available."""

    saleschannelid: int | None = None
    """Sales channel ID."""


@dataclasses.dataclass
class OptIn(Model):
    """A single opt-in."""

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new opt in.

    **Note:** Ignored when updating an existing opt in.
    """

    typeid: int | None = None
    """Type of the opt-in; can be ``Mandatory`` (40001) or ``Optional`` (40002)."""

    name: str | None = None
    """Name."""

    availability: list[OptInAvailability] | None = None
    """Sales channels where this opt-in is available."""

    caption: str | None = None
    """Caption for the checkbox; required when typeid is ``Optional`` (40002)."""

    description: str | None = None
    """Description."""

    nocaption: str | None = None
    """Caption for the no radio button; required when typeid is
    ``Mandatory`` (40001).
    """

    yescaption: str | None = None
    """Caption for the yes radio button; required when typeid is
    ``Mandatory`` (40001).
    """

    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new opt in.

    **Note:** Ignored when updating an existing opt in.
    """

    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new opt in.

    **Note:** Ignored when updating an existing opt in.
    """

    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new opt in.

    **Note:** Ignored when updating an existing opt in.
    """


@dataclasses.dataclass
class OptInQuery(Model):
    """Set of parameters used to filter opt ins."""

    filter: str | None = None
    """Filter the returned items by specifying a query on the public datamodel
    that returns the ids.
    """

    includearchived: bool | None = None
    """If this parameter is true, archived items will be returned as well."""

    lastupdatesince: datetime | None = None
    """All items updated since this timestamp will be returned.

    Timestamp should be passed in ``YYYY-MM-DD hh:mm:ss`` format.
    """


# --- Relation Types ---


@dataclasses.dataclass
class RelationType(Model):
    """A single relation type."""

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new relation type.

    **Note:** Ignored when updating an existing relation type.
    """

    name: str | None = None
    """Name of the relation type."""

    parentid: int | None = None
    """ID of the parent relation type."""

    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new relation type.

    **Note:** Ignored when updating an existing relation type.
    """

    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new relation type.

    **Note:** Ignored when updating an existing relation type.
    """

    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new relation type.

    **Note:** Ignored when updating an existing relation type.
    """


@dataclasses.dataclass
class RelationTypeQuery(Model):
    """Set of parameters used to filter relation types."""

    filter: str | None = None
    """Filter the returned items by specifying a query on the public datamodel
    that returns the ids.
    """

    includearchived: bool | None = None
    """If this parameter is true, archived items will be returned as well."""

    lastupdatesince: datetime | None = None
    """All items updated since this timestamp will be returned.

    Timestamp should be passed in ``YYYY-MM-DD hh:mm:ss`` format.
    """


# --- Reports ---


@dataclasses.dataclass
class ReportOptions(Model):
    """Report options controlling output format and layout."""

    excelpagewidth: int | None = None
    """The page size for the report when exported as Excel."""

    excelscaling: float | None = None
    """Excel-specific option for scaling the width."""

    pdfpagesize: str | None = None
    """The page size for the report (e.g. A4 landscape, Letter landscape)."""

    usesystemfont: bool | None = None
    """Indicates if a system font should be used."""


@dataclasses.dataclass
class Report(Model):
    """A single report."""

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new report.

    **Note:** Ignored when updating an existing report.
    """

    name: str | None = None
    """Name of the report."""

    content: Any | None = None
    """The actual report definition.

    **Note:** Not set when retrieving a list of reports.
    """

    defaultformat: str | None = None
    """Default output format; possible values are ``pdf`` or ``excel``."""

    description: str | None = None
    """Description of the report."""

    emailbcc: str | None = None
    """List of email recipients to receive the report in BCC, separated by
    semicolons.
    """

    emailcc: str | None = None
    """List of email recipients to receive the report in CC, separated by
    semicolons.
    """

    emailrecipients: str | None = None
    """List of email recipients to receive the report, separated by semicolons."""

    emailschedule: bool | None = None
    """Indicates if this report is scheduled to be sent by email at a certain
    interval.
    """

    emailscheduledayofmonth: int | None = None
    """Day of the month on which the report will be sent."""

    emailscheduledayofweek: int | None = None
    """Day of the week on which the report will be sent (1 = Monday, 7 = Sunday)."""

    emailschedulehourofday: int | None = None
    """Hour of the day at which the report will be sent."""

    emailschedulequery: str | None = None
    """Report will only be sent if this query returns at least one result."""

    options: ReportOptions | None = None
    """Key-value options for output (e.g. ``pdfpagesize``, ``excelpagewidth``).

    **Note:** Not set when retrieving a list of reports.
    """

    reporttypeid: int | None = None
    """The report type defines the UI and parameters used when generating the
    report.
    """

    subtitles: list[str] | None = None
    """A list of subtitles for the report.

    **Note:** Not set when retrieving a list of reports.
    """

    translations: list[str] | None = None
    """A map of language codes to gettext ``.po`` files.

    **Note:** Not set when retrieving a list of reports.
    """

    usagetypeid: int | None = None
    """Indicates where the report is used: 17001 (Sales), 17002 (External sales),
    17003 (Hidden).
    """

    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new report.

    **Note:** Ignored when updating an existing report.
    """

    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new report.

    **Note:** Ignored when updating an existing report.
    """


@dataclasses.dataclass
class ReportQuery(Model):
    """Set of parameters used to filter reports."""

    filter: str | None = None
    """Filter the returned items by specifying a query on the public datamodel
    that returns the ids.
    """

    lastupdatesince: datetime | None = None
    """All items updated since this timestamp will be returned.

    Timestamp should be passed in ``YYYY-MM-DD hh:mm:ss`` format.
    """


# --- Sales Channels ---


@dataclasses.dataclass
class SalesChannel(Model):
    """A single sales channel."""

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new sales channel.

    **Note:** Ignored when updating an existing sales channel.
    """

    typeid: int | None = None
    """The type of this sales channel, defines where this sales channel will be
    used.
    """

    name: str | None = None
    """Name of the sales channel."""

    ordermailtemplateid_confirmation: int | None = None
    """ID of the order mail template used for sending confirmations. Can be 0 to
    indicate that no mail should be sent.
    """

    ordermailtemplateid_confirmation_sendalways: bool | None = None
    """Always send the confirmation, regardless of the payment method
    configuration.
    """

    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new sales channel.

    **Note:** Ignored when updating an existing sales channel.
    """

    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new sales channel.

    **Note:** Ignored when updating an existing sales channel.
    """

    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new sales channel.

    **Note:** Ignored when updating an existing sales channel.
    """


@dataclasses.dataclass
class SalesChannelQuery(Model):
    """Set of parameters used to filter sales channels."""

    filter: str | None = None
    """Filter the returned items by specifying a query on the public datamodel
    that returns the ids.
    """

    includearchived: bool | None = None
    """If this parameter is true, archived items will be returned as well."""

    lastupdatesince: datetime | None = None
    """All items updated since this timestamp will be returned.

    Timestamp should be passed in ``YYYY-MM-DD hh:mm:ss`` format.
    """


# --- Views ---


@dataclasses.dataclass
class ViewColumn(Model):
    """A view column referencing a field definition."""

    id: int | None = None
    """ID of the field definition for this column."""


@dataclasses.dataclass
class View(Model):
    """A single view."""

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new view.

    **Note:** Ignored when updating an existing view.
    """

    typeid: int | None = None
    """Type ID.

    **Note:** Ignored when updating an existing view.
    """

    name: str | None = None
    """Name of the view."""

    columns: list[ViewColumn] | None = None
    """List of field definitions that are part of this view."""

    orderby: int | None = None
    """The field definition to order results on."""

    orderby_asc: bool | None = None
    """Indicates whether results should be ordered ascending or descending."""

    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new view.

    **Note:** Ignored when updating an existing view.
    """

    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new view.

    **Note:** Ignored when updating an existing view.
    """

    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new view.

    **Note:** Ignored when updating an existing view.
    """


@dataclasses.dataclass
class ViewQuery(Model):
    """Set of parameters used to filter views."""

    typeid: int | None = None
    """Only return items with the given typeid."""

    filter: str | None = None
    """Filter the returned items by specifying a query on the public datamodel
    that returns the ids.
    """

    includearchived: bool | None = None
    """If this parameter is true, archived items will be returned as well."""

    lastupdatesince: datetime | None = None
    """All items updated since this timestamp will be returned.

    Timestamp should be passed in ``YYYY-MM-DD hh:mm:ss`` format.
    """
