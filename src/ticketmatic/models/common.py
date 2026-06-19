"""Common data models shared across the Ticketmatic API."""

from __future__ import annotations

import dataclasses
from datetime import datetime
from typing import Any

from ticketmatic.models.base import Model


@dataclasses.dataclass
class AccountInfo(Model):
    """Account information."""

    id: int | None = None
    """Account ID."""

    name: str | None = None
    """Account name."""

    address: str | None = None
    """Account address."""

    image: str | None = None
    """Link to the account image."""

    lat: float | None = None
    """Latitude."""

    logo: str | None = None
    """Link to the account logo."""

    long: float | None = None
    """Longitude."""

    shortname: str | None = None
    """Account short name."""

    url: str | None = None
    """Account website."""


@dataclasses.dataclass
class AccountParameter(Model):
    """An account parameter defines general behavior of your account."""

    key: str | None = None
    """The name of the account parameter."""

    value: Any | None = None
    """Value."""


@dataclasses.dataclass
class Address(Model):
    """Address, used for physical deliveries and contact details."""

    id: int | None = None
    """Address ID.

    **Note:** Only available when used for a contact address.
    """

    typeid: int | None = None
    """Address type ID.

    **Note:** Only available when used for a contact address.
    """

    addressee: str | None = None
    """Addressee.

    **Note:** Only available when used as an order delivery address.
    """

    city: str | None = None
    """City."""

    country: str | None = None
    """Country name (based on ``typeid``, returned as a convenience).

    **Note:** Only available when used for a contact address.
    """

    countrycode: str | None = None
    """ISO 3166-1 alpha-2 country code."""

    customerid: int | None = None
    """Contact this address belongs to.

    **Note:** Only available when used for a contact address.
    """

    state: str | None = None
    """State."""

    street1: str | None = None
    """Street field 1 (typically the street name)."""

    street2: str | None = None
    """Street field 2 (typically the number)."""

    street3: str | None = None
    """Street field 3 (sometimes used for box numbers or suffixes)."""

    type: str | None = None
    """Address type (based on ``typeid``, returned as a convenience).

    **Note:** Only available when used for a contact address.
    """

    zip: str | None = None
    """Zip code."""


@dataclasses.dataclass
class Appoptin(Model):
    """App opt-in."""

    ip: str | None = None
    """IP address."""

    message: str | None = None
    """The message shown for the opt-in."""

    method: str | None = None
    """Method used for opt-in."""

    status: bool | None = None
    """The status of the opt-in."""

    ts: str | None = None
    """Created timestamp."""


@dataclasses.dataclass
class BatchResultItem(Model):
    """Result of a batch operation for a specific item."""

    id: int | None = None
    """The ID of the item."""

    msg: str | None = None
    """Extra info."""

    succeeded: bool | None = None
    """Indicates if the operation succeeded for this item."""


@dataclasses.dataclass
class BatchResult(Model):
    """Result of a batch operation."""

    nbrsucceeded: int | None = None
    """The number of items for which the batch operation succeeded."""

    results: list[BatchResultItem] | None = None
    """Detailed results for the batch operation."""


@dataclasses.dataclass
class KeyValueItem(Model):
    """Key-value item."""

    key: str | None = None
    """Key."""

    value: str | None = None
    """Value."""


@dataclasses.dataclass
class Layout(Model):
    """Layout parameters."""

    color: str | None = None
    """Main color for the event."""

    maxImage: bool | None = None
    """Use image in max format."""


@dataclasses.dataclass
class Timestamp(Model):
    """A timestamp returned by the diagnostic ``/time`` call."""

    systemtime: datetime | None = None
    """Current system time."""


@dataclasses.dataclass
class Url(Model):
    """A URL wrapper."""

    url: str | None = None
    """URL."""


@dataclasses.dataclass
class QueryRequest(Model):
    """Required data for creating a query on the public data model."""

    limit: int | None = None
    """Optional limit for the result (default: 100)."""

    offset: int | None = None
    """Optional offset for the result (default: 0)."""

    query: str | None = None
    """Actual query to execute."""


@dataclasses.dataclass
class QueryResult(Model):
    """Result of a query on the public data model."""

    nbrofresults: int | None = None
    """The number of rows in the result."""

    results: list[Any] | None = None
    """The actual resulting rows."""


@dataclasses.dataclass
class LogItem(Model):
    """Log item returned when requesting the log history of an order."""

    id: int | None = None
    """ID of the log item."""

    orderid: int | None = None
    """Order ID."""

    typeid: int | None = None
    """Log item type."""

    info: Any | None = None
    """Info."""

    lookupinfo: Any | None = None
    """Lookup info."""

    model: Any | None = None
    """Model."""

    ts: datetime | None = None
    """Log item timestamp."""

    userid: int | None = None
    """User ID."""

    username: str | None = None
    """User name."""


@dataclasses.dataclass
class JobResult(Model):
    """Info on a job."""

    id: str | None = None
    """ID of the job."""

    name: str | None = None
    """Job name."""

    progress: int | None = None
    """Job progress (percentage)."""

    progresstext: str | None = None
    """Current progress of the job as string."""

    status: int | None = None
    """Status for the job."""


@dataclasses.dataclass
class AddItemsResult(Model):
    """Result when adding tickets or products to an order."""

    ids: list[int] | None = None
    """IDs of the items that were added."""

    # order field is typed as Any to avoid circular import; it's an Order instance
    order: Any | None = None
    """The modified order."""


@dataclasses.dataclass
class ServicemailScheduling(Model):
    """Scheduling used for planning of service mails."""

    days: int | None = None
    """Amount of days before/after the event to send the mail."""

    relative: str | None = None
    """Send the mail before or after the event."""

    time: str | None = None
    """The time (HH:MM) at which to send the mail."""


@dataclasses.dataclass
class FilterItem(Model):
    """Element of a filter."""

    id: int | None = None
    """Filter ID indicating which filter is used in this operator."""

    operator: str | None = None
    """Operator type."""
