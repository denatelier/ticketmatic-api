"""Data models for payment methods, payment scenarios, and related types."""

from __future__ import annotations

import dataclasses
from datetime import datetime
from typing import Any, ClassVar

from ticketmatic.models.base import Model


@dataclasses.dataclass
class PaymentRequest(Model):
    """Info for requesting an immediate payment in an order."""

    language: str | None = None
    """The language to be used during the payment processing."""

    returnurl: str | None = None
    """The returnurl that will be called after the payment request was done."""

    withcustomer: bool | None = None
    """Create (or use an existing) customer with the PSP.

    The order needs a linked contact.
    """


@dataclasses.dataclass
class PaymentscenarioAvailability(Model):
    """Configures in what sales channels a payment scenario is available.

    It can also further refine the availability based on a script written in
    JavaScript.
    """

    saleschannels: list[int] | None = None
    """The payment scenario will be available for these sales channels.

    If this is empty the payment scenario will not be available.
    """

    script: str | None = None
    """A JavaScript that needs to return a boolean.

    It has the current order and sales channel available.
    """

    usescript: bool | None = None
    """Indicates if the script will be used."""


@dataclasses.dataclass
class PaymentscenarioExpiryParameters(Model):
    """Expiry parameters for a deferred-payment payment scenario.

    Determines the moment in time when an order expires. It is calculated as
    ``MIN(<order creation date> + daysafterordercreation, <date of first event
    in order> - daysbeforeevent)``. If ``deleteonexpiry`` is set to ``true``,
    the order will be deleted.
    """

    daysaftercreation: int | None = None
    """The amount of days after the payment scenario was set that the order
    becomes overdue.
    """

    daysafterordercreation: int | None = None
    """DEPRECATED, use ``daysaftercreation``.

    The amount of days after an order has been created that the order becomes
    overdue.
    """

    daysbeforeevent: int | None = None
    """DEPRECATED, use ``daysaftercreation``.

    The number of days before an event that an order becomes overdue.
    """

    deleteonexpiry: bool | None = None
    """Indicates whether the order will be deleted when it expires."""


@dataclasses.dataclass
class PaymentscenarioOverdueParameters(Model):
    """Overdue parameters for a deferred-payment payment scenario.

    Determines the moment in time when an order becomes overdue. It is
    calculated as ``MIN(<order creation date> + daysafterordercreation,
    <date of first event in order> - daysbeforeevent)``.
    """

    daysaftercreation: int | None = None
    """The amount of days after the payment scenario was set that the order
    becomes overdue.
    """

    daysafterordercreation: int | None = None
    """DEPRECATED, use ``daysaftercreation``.

    The amount of days after an order has been created that the order becomes
    overdue.
    """

    daysbeforeevent: int | None = None
    """DEPRECATED, use ``daysaftercreation``.

    The number of days before an event that an order becomes overdue.
    """


@dataclasses.dataclass
class PaymentMethod(Model):
    """A single payment method."""

    _has_custom_fields: ClassVar[bool] = True

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new payment method.

    **Note:** Ignored when updating an existing payment method.
    """

    name: str | None = None
    """Name of the payment method."""

    config: Any | None = None
    """Specific configuration for the payment method; content depends on the
    payment method type.

    **Note:** Not set when retrieving a list of payment methods.
    """

    internalremark: str | None = None
    """Internal remark, will not be shown to customers."""

    paymentmethodtypeid: int | None = None
    """Type of the payment method."""

    pspid: int | None = None
    """Payment Service Provider this payment method is linked to."""

    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new payment method.

    **Note:** Ignored when updating an existing payment method.
    """

    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new payment method.

    **Note:** Ignored when updating an existing payment method.
    """

    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new payment method.

    **Note:** Ignored when updating an existing payment method.
    """

    custom_fields: dict[str, Any] | None = None
    """Custom field values keyed by name (``c_``-prefixed in the API)."""


@dataclasses.dataclass
class PaymentMethodQuery(Model):
    """Set of parameters used to filter payment methods."""

    filter: str | None = None
    """Filter the returned items by specifying a query on the public data model
    that returns the ids.
    """

    includearchived: bool | None = None
    """If this parameter is true, archived items will be returned as well."""

    lastupdatesince: datetime | None = None
    """All items that were updated since this timestamp will be returned.

    Timestamp should be passed in ``YYYY-MM-DD hh:mm:ss`` format.
    """


@dataclasses.dataclass
class PaymentScenario(Model):
    """A single payment scenario."""

    _has_custom_fields: ClassVar[bool] = True

    id: int | None = None
    """Unique ID.

    **Note:** Ignored when creating a new payment scenario.

    **Note:** Ignored when updating an existing payment scenario.
    """

    typeid: int | None = None
    """Type for the payment scenario.

    Can be ``Immediate payment`` (2701), ``Mollie bank transfer`` (2702),
    ``Regular bank transfer`` (2703), ``Deferred online payment`` (2704), or
    ``Deferred other`` (2705).
    """

    name: str | None = None
    """Name of the payment scenario."""

    availability: PaymentscenarioAvailability | None = None
    """Rules that define in what conditions this payment scenario is available.

    **Note:** Not set when retrieving a list of payment scenarios.
    """

    bankaccountbeneficiary: str | None = None
    """Beneficiary for the bank account number.

    Only used for type 2703 (Regular bank transfer).
    """

    bankaccountbic: str | None = None
    """BIC code for the bank account number.

    Only used for type 2703 (Regular bank transfer).
    """

    bankaccountnumber: str | None = None
    """Bank account number to be used.

    Only used for type 2703 (Regular bank transfer).
    """

    expiryparameters: PaymentscenarioExpiryParameters | None = None
    """Rules that define when an order becomes expired.

    Not used for type 2701.

    **Note:** Not set when retrieving a list of payment scenarios.
    """

    feedescription: str | None = None
    """A very short description of the fee that is applicable."""

    internalremark: str | None = None
    """An internal remark, which is never shown to customers.

    Can be used to distinguish identically named payment scenarios.
    """

    logo: str | None = None
    """Logo URL."""

    mailorganization: bool | None = None
    """Send mail to organization if known."""

    ordermailtemplateid_expiry: int | None = None
    """Link to the order mail template sent when the order is expired.

    Can be 0 to indicate that no mail should be sent. Not used for type 2701.
    """

    ordermailtemplateid_overdue: int | None = None
    """Link to the order mail template sent when the order is overdue.

    Can be 0 to indicate that no mail should be sent. Not used for type 2701.
    """

    ordermailtemplateid_paymentinstruction: int | None = None
    """Link to the order mail template sent as payment instruction.

    Can be 0 to indicate that no mail should be sent. Not used for type 2701.
    """

    overdueparameters: PaymentscenarioOverdueParameters | None = None
    """Rules that define when an order becomes overdue.

    Not used for type 2701.

    **Note:** Not set when retrieving a list of payment scenarios.
    """

    paymentmethods: list[int] | None = None
    """Set of payment methods that are linked to this payment scenario.

    Depending on the type, this field has different usage.
    """

    shortdescription: str | None = None
    """Short description of the payment scenario, will be shown to customers."""

    visibility: str | None = None
    """Parameter that sets the visibility of this scenario.

    Can be either ``FULL`` or ``API``.
    """

    isarchived: bool | None = None
    """Whether or not this item is archived.

    **Note:** Ignored when creating a new payment scenario.

    **Note:** Ignored when updating an existing payment scenario.
    """

    createdts: datetime | None = None
    """Created timestamp.

    **Note:** Ignored when creating a new payment scenario.

    **Note:** Ignored when updating an existing payment scenario.
    """

    lastupdatets: datetime | None = None
    """Last updated timestamp.

    **Note:** Ignored when creating a new payment scenario.

    **Note:** Ignored when updating an existing payment scenario.
    """

    custom_fields: dict[str, Any] | None = None
    """Custom field values keyed by name (``c_``-prefixed in the API)."""


@dataclasses.dataclass
class PaymentScenarioQuery(Model):
    """Set of parameters used to filter payment scenarios."""

    filter: str | None = None
    """Filter the returned items by specifying a query on the public data model
    that returns the ids.
    """

    includearchived: bool | None = None
    """If this parameter is true, archived items will be returned as well."""

    lastupdatesince: datetime | None = None
    """All items that were updated since this timestamp will be returned.

    Timestamp should be passed in ``YYYY-MM-DD hh:mm:ss`` format.
    """
