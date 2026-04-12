from __future__ import annotations

import dataclasses
from datetime import datetime
from typing import Any, ClassVar

from ticketmatic.models.base import Model
from ticketmatic.models.common import Address, Appoptin


@dataclasses.dataclass
class ContactOptInInfo(Model):
    ip: str | None = None
    method: str | None = None
    remarks: str | None = None
    userid: int | None = None


@dataclasses.dataclass
class ContactOptIn(Model):
    id: int | None = None
    info: ContactOptInInfo | None = None
    optinid: int | None = None
    status: int | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class ContactRelationship(Model):
    id: int | None = None
    typeid: int | None = None
    childcontactid: int | None = None
    parentcontactid: int | None = None


@dataclasses.dataclass
class Phonenumber(Model):
    id: int | None = None
    typeid: int | None = None
    customerid: int | None = None
    number: str | None = None
    type: str | None = None


@dataclasses.dataclass
class Contact(Model):
    _has_custom_fields: ClassVar[bool] = True

    id: int | None = None
    addresses: list[Address] | None = None
    appnotifications: list[int] | None = None
    apponboardingstatus: int | None = None
    appoptin: Appoptin | None = None
    appphone: str | None = None
    apptoken: str | None = None
    birthdate: datetime | None = None
    company: str | None = None
    customertitleid: int | None = None
    email: str | None = None
    firstname: str | None = None
    image: str | None = None
    languagecode: str | None = None
    lastname: str | None = None
    lookup: Any | None = None
    middlename: str | None = None
    optins: list[ContactOptIn] | None = None
    organizationfunction: str | None = None
    phonenumbers: list[Phonenumber] | None = None
    relationships: list[ContactRelationship] | None = None
    relationtypes: list[int] | None = None
    sendmail: bool | None = None
    sex: str | None = None
    status: str | None = None
    subscribed: bool | None = None
    vatnumber: str | None = None
    isdeleted: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None
    custom_fields: dict[str, Any] | None = None


@dataclasses.dataclass
class ContactQuery(Model):
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None
    limit: int | None = None
    offset: int | None = None
    orderby: str | None = None
    output: str | None = None
    searchterm: str | None = None


@dataclasses.dataclass
class ContactGetQuery(Model):
    email: str | None = None


@dataclasses.dataclass
class ContactIdReservation(Model):
    id: int | None = None


@dataclasses.dataclass
class ContactImportStatus(Model):
    id: int | None = None
    error: str | None = None
    ok: bool | None = None


@dataclasses.dataclass
class ContactRemark(Model):
    id: int | None = None
    content: str | None = None
    pinned: bool | None = None


@dataclasses.dataclass
class ContactTitle(Model):
    id: int | None = None
    name: str | None = None
    isinternal: bool | None = None
    languagecode: str | None = None
    sex: str | None = None
    isarchived: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class ContactTitleQuery(Model):
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None


@dataclasses.dataclass
class ContactAddressType(Model):
    id: int | None = None
    name: str | None = None
    isarchived: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class ContactAddressTypeQuery(Model):
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None


@dataclasses.dataclass
class ContactField(Model):
    id: int | None = None
    name: str | None = None
    caption: str | None = None


@dataclasses.dataclass
class PhoneNumberType(Model):
    id: int | None = None
    name: str | None = None
    isarchived: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class PhoneNumberTypeQuery(Model):
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None


@dataclasses.dataclass
class ContactBatchUpdate(Model):
    _has_custom_fields: ClassVar[bool] = True

    customertitleid: int | None = None
    languagecode: str | None = None
    custom_fields: dict[str, Any] | None = None


@dataclasses.dataclass
class BatchContactUpdateField(Model):
    key: str | None = None
    updatetype: str | None = None
    value: Any | None = None


@dataclasses.dataclass
class BatchContactParameters(Model):
    name: str | None = None
    fields: ContactBatchUpdate | None = None
    ids: list[int] | None = None
    primary: int | None = None
    updatefields: list[BatchContactUpdateField] | None = None


@dataclasses.dataclass
class BatchContactOperation(Model):
    ids: list[int] | None = None
    operation: str | None = None
    parameters: BatchContactParameters | None = None
