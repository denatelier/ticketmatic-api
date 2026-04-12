from __future__ import annotations

import dataclasses
from datetime import datetime
from typing import Any, ClassVar

from ticketmatic.models.base import Model


@dataclasses.dataclass
class PaymentRequest(Model):
    language: str | None = None
    returnurl: str | None = None
    withcustomer: bool | None = None


@dataclasses.dataclass
class PaymentscenarioAvailability(Model):
    saleschannels: list[int] | None = None
    script: str | None = None
    usescript: bool | None = None


@dataclasses.dataclass
class PaymentscenarioExpiryParameters(Model):
    daysaftercreation: int | None = None
    daysafterordercreation: int | None = None
    daysbeforeevent: int | None = None
    deleteonexpiry: bool | None = None


@dataclasses.dataclass
class PaymentscenarioOverdueParameters(Model):
    daysaftercreation: int | None = None
    daysafterordercreation: int | None = None
    daysbeforeevent: int | None = None


@dataclasses.dataclass
class PaymentMethod(Model):
    _has_custom_fields: ClassVar[bool] = True

    id: int | None = None
    name: str | None = None
    config: Any | None = None
    internalremark: str | None = None
    paymentmethodtypeid: int | None = None
    pspid: int | None = None
    isarchived: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None
    custom_fields: dict[str, Any] | None = None


@dataclasses.dataclass
class PaymentMethodQuery(Model):
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None


@dataclasses.dataclass
class PaymentScenario(Model):
    _has_custom_fields: ClassVar[bool] = True

    id: int | None = None
    typeid: int | None = None
    name: str | None = None
    availability: PaymentscenarioAvailability | None = None
    bankaccountbeneficiary: str | None = None
    bankaccountbic: str | None = None
    bankaccountnumber: str | None = None
    expiryparameters: PaymentscenarioExpiryParameters | None = None
    feedescription: str | None = None
    internalremark: str | None = None
    logo: str | None = None
    mailorganization: bool | None = None
    ordermailtemplateid_expiry: int | None = None
    ordermailtemplateid_overdue: int | None = None
    ordermailtemplateid_paymentinstruction: int | None = None
    overdueparameters: PaymentscenarioOverdueParameters | None = None
    paymentmethods: list[int] | None = None
    shortdescription: str | None = None
    visibility: str | None = None
    isarchived: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None
    custom_fields: dict[str, Any] | None = None


@dataclasses.dataclass
class PaymentScenarioQuery(Model):
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None
