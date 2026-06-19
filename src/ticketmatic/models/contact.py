"""Data models for contacts, contact settings, and batch contact operations."""

from __future__ import annotations

import dataclasses
from datetime import datetime
from typing import Any, ClassVar

from ticketmatic.models.base import Model
from ticketmatic.models.common import Address, Appoptin


@dataclasses.dataclass
class ContactOptInInfo(Model):
    """Additional info when this opt in is set."""

    ip: str | None = None
    """The ip address from which the opt in is set."""

    method: str | None = None
    """The method by which the status is set."""

    remarks: str | None = None
    """Explanation of why the status was set."""

    userid: int | None = None
    """ID of the user that has set this opt in."""


@dataclasses.dataclass
class ContactOptIn(Model):
    """A single contact opt-in."""

    id: int | None = None
    """Unique ID."""

    info: ContactOptInInfo | None = None
    """Info on the actual opt in."""

    optinid: int | None = None
    """ID of the optin."""

    status: int | None = None
    """Status of the opt-in.

    Possible values are ``Unknown`` (7601), ``Opted In`` (7602) and
    ``Opted Out`` (7603).
    """

    createdts: datetime | None = None
    """Created timestamp."""

    lastupdatets: datetime | None = None
    """Last updated timestamp."""


@dataclasses.dataclass
class ContactRelationship(Model):
    """Contact relationships."""

    id: int | None = None
    """Contact relationship ID."""

    typeid: int | None = None
    """The type of the relationship."""

    childcontactid: int | None = None
    """The contact ID of the child."""

    parentcontactid: int | None = None
    """The contact ID of the parent."""


@dataclasses.dataclass
class Phonenumber(Model):
    """A phone number belonging to a contact."""

    id: int | None = None
    """Phone number ID."""

    typeid: int | None = None
    """Phone number type ID."""

    customerid: int | None = None
    """Contact this address belongs to."""

    number: str | None = None
    """Phone number."""

    type: str | None = None
    """Phone number type (based on ``typeid``, returned as a convenience)."""


@dataclasses.dataclass
class Contact(Model):
    """A single contact."""

    _has_custom_fields: ClassVar[bool] = True

    id: int | None = None
    """Contact ID.

    **Note:** Ignored when creating a new contact.

    **Note:** Ignored when updating an existing contact.
    """

    addresses: list[Address] | None = None
    """Addresses."""

    appnotifications: list[int] | None = None
    """App notifications."""

    apponboardingstatus: int | None = None
    """App onboardingstatus."""

    appoptin: Appoptin | None = None
    """App optin."""

    appphone: str | None = None
    """App phone."""

    apptoken: str | None = None
    """App token."""

    birthdate: datetime | None = None
    """Birth date."""

    company: str | None = None
    """Company."""

    customertitleid: int | None = None
    """Customer title ID (also determines the gender of the contact)."""

    email: str | None = None
    """E-mail address."""

    firstname: str | None = None
    """First name."""

    image: str | None = None
    """Image url."""

    languagecode: str | None = None
    """Language (ISO 639-1 code)."""

    lastname: str | None = None
    """Last name."""

    lookup: Any | None = None
    """Related objects."""

    middlename: str | None = None
    """Middle name."""

    optins: list[ContactOptIn] | None = None
    """A list of opt ins."""

    organizationfunction: str | None = None
    """Job function."""

    phonenumbers: list[Phonenumber] | None = None
    """Phone numbers."""

    relationships: list[ContactRelationship] | None = None
    """A list of contact relationships."""

    relationtypes: list[int] | None = None
    """Relation type IDs."""

    sendmail: bool | None = None
    """Whether to send mail to this contact."""

    sex: str | None = None
    """Sex."""

    status: str | None = None
    """Contact status.

    Possible values:

    * **deleted**: Contact has been deleted.
    * **incomplete**: Contact misses crucial account information.
    * **(blank)**: Normal contact.

    **Note:** Ignored when creating a new contact.

    **Note:** Ignored when updating an existing contact.
    """

    subscribed: bool | None = None
    """Whether or not this contact is subscribed in the e-mail marketing integration.

    **Note:** Ignored when creating a new contact.

    **Note:** Ignored when updating an existing contact.
    """

    vatnumber: str | None = None
    """VAT Number (for organizations)."""

    isdeleted: bool | None = None
    """Whether or not this contact has been deleted.

    **Note:** Ignored when creating a new contact.

    **Note:** Ignored when updating an existing contact.
    """

    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new contact.

    **Note:** Ignored when updating an existing contact.
    """

    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new contact.

    **Note:** Ignored when updating an existing contact.
    """

    custom_fields: dict[str, Any] | None = None
    """Custom field values keyed by name (``c_``-prefixed in the API)."""


@dataclasses.dataclass
class ContactQuery(Model):
    """Filter parameters to fetch a list of contacts."""

    filter: str | None = None
    """A SQL query that returns contact IDs.

    Can be used to do arbitrary filtering. See the database documentation
    for contact for more information.
    """

    includearchived: bool | None = None
    """If this parameter is true, archived items will be returned as well."""

    lastupdatesince: datetime | None = None
    """Only include contacts that have been updated since the given timestamp."""

    limit: int | None = None
    """Limit results to at most the given amount of contacts."""

    offset: int | None = None
    """Skip the first X contacts."""

    orderby: str | None = None
    """Order by the given field.

    Supported values: ``name``, ``lastupdatets``, ``createdts``.
    """

    output: str | None = None
    """Output format.

    Possible values:

    * **ids**: Only fill the ID field.
    * **minimal**: A minimal set of order fields.
    * **default**: Return all order fields (also used when the output
      parameter is omitted).
    """

    searchterm: str | None = None
    """A text filter string.

    Matches against the contact name and contact details.
    """


@dataclasses.dataclass
class ContactGetQuery(Model):
    """Optional alternative methods to retrieve a contact."""

    email: str | None = None
    """Contact e-mail address."""


@dataclasses.dataclass
class ContactIdReservation(Model):
    """Contact ID reservation."""

    id: int | None = None
    """Maximum ID to reserve."""


@dataclasses.dataclass
class ContactImportStatus(Model):
    """Import status per contact."""

    id: int | None = None
    """Contact ID."""

    error: str | None = None
    """Error message, if failed."""

    ok: bool | None = None
    """Whether the import succeeded."""


@dataclasses.dataclass
class ContactRemark(Model):
    """Remarks belonging to a contact."""

    id: int | None = None
    """Remark ID."""

    content: str | None = None
    """The message."""

    pinned: bool | None = None
    """Is this relevant for sales?"""


@dataclasses.dataclass
class ContactTitle(Model):
    """A single contact title."""

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new contact title.

    **Note:** Ignored when updating an existing contact title.
    """

    name: str | None = None
    """Title name."""

    isinternal: bool | None = None
    """Restricts this title from showing up on the websales pages."""

    languagecode: str | None = None
    """Language for this title."""

    sex: str | None = None
    """Gender associated with this title."""

    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new contact title.

    **Note:** Ignored when updating an existing contact title.
    """

    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new contact title.

    **Note:** Ignored when updating an existing contact title.
    """

    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new contact title.

    **Note:** Ignored when updating an existing contact title.
    """


@dataclasses.dataclass
class ContactTitleQuery(Model):
    """Set of parameters used to filter contact titles."""

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
class ContactAddressType(Model):
    """A single contact address type."""

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new contact address type.

    **Note:** Ignored when updating an existing contact address type.
    """

    name: str | None = None
    """Name of the address type."""

    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new contact address type.

    **Note:** Ignored when updating an existing contact address type.
    """

    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new contact address type.

    **Note:** Ignored when updating an existing contact address type.
    """

    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new contact address type.

    **Note:** Ignored when updating an existing contact address type.
    """


@dataclasses.dataclass
class ContactAddressTypeQuery(Model):
    """Set of parameters used to filter contact address types."""

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
class ContactField(Model):
    """Contact field is a list of fields that are asked upon registration."""

    id: int | None = None
    """ID of this ContactField."""

    name: str | None = None
    """Name of this contactfield."""

    caption: str | None = None
    """Caption of this contactfield."""


@dataclasses.dataclass
class PhoneNumberType(Model):
    """A single phone number type."""

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new phone number type.

    **Note:** Ignored when updating an existing phone number type.
    """

    name: str | None = None
    """Name of the phone number type."""

    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new phone number type.

    **Note:** Ignored when updating an existing phone number type.
    """

    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new phone number type.

    **Note:** Ignored when updating an existing phone number type.
    """

    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new phone number type.

    **Note:** Ignored when updating an existing phone number type.
    """


@dataclasses.dataclass
class PhoneNumberTypeQuery(Model):
    """Set of parameters used to filter phone number types."""

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
class ContactBatchUpdate(Model):
    """Set of fields that can be used for contact batch update."""

    _has_custom_fields: ClassVar[bool] = True

    customertitleid: int | None = None
    """Customer title ID (also determines the gender of the contact)."""

    languagecode: str | None = None
    """Language (ISO 639-1 code)."""

    custom_fields: dict[str, Any] | None = None
    """Custom field values keyed by name (``c_``-prefixed in the API)."""


@dataclasses.dataclass
class BatchContactUpdateField(Model):
    """Field to update on contact."""

    key: str | None = None
    """The name of the field, can either be a custom field or one of the
    following fixed fields (``customertitleid``, ``languagecode``).
    """

    updatetype: str | None = None
    """The type of update that needs to be done on the field.

    Can either be ``set`` (default), ``add`` or ``remove`` when used in
    combination with multi value fields.
    """

    value: Any | None = None
    """The value of the field."""


@dataclasses.dataclass
class BatchContactParameters(Model):
    """Parameters for batch operations performed on contacts."""

    name: str | None = None
    """Selection name, used for operation ``sendselection``."""

    fields: ContactBatchUpdate | None = None
    """[DEPRECATED] Use updatefields instead."""

    ids: list[int] | None = None
    """Relation type IDs, used for operations ``addrelationtypes`` and
    ``removerelationtypes``.
    """

    primary: int | None = None
    """Primary contact to merge into."""

    updatefields: list[BatchContactUpdateField] | None = None
    """Set of fields to update, used for operation ``update``.

    Custom fields are also supported.
    """


@dataclasses.dataclass
class BatchContactOperation(Model):
    """Batch operations performed on contacts."""

    ids: list[int] | None = None
    """Restrict operation to supplied IDs, if these ids are not specified
    **all** contacts are updated.
    """

    operation: str | None = None
    """Operation to perform.

    Possible values are: ``addrelationtypes``, ``removerelationtypes``,
    ``delete``, ``subscribe``, ``unsubscribe`` and ``update``.
    """

    parameters: BatchContactParameters | None = None
    """Operation-specific parameters."""
