from __future__ import annotations

import dataclasses
from datetime import datetime
from typing import Any

from ticketmatic.models.base import Model


@dataclasses.dataclass
class AccountInfo(Model):
    id: int | None = None
    name: str | None = None
    address: str | None = None
    image: str | None = None
    lat: float | None = None
    logo: str | None = None
    long: float | None = None
    shortname: str | None = None
    url: str | None = None


@dataclasses.dataclass
class AccountParameter(Model):
    key: str | None = None
    value: Any | None = None


@dataclasses.dataclass
class Address(Model):
    id: int | None = None
    typeid: int | None = None
    addressee: str | None = None
    city: str | None = None
    country: str | None = None
    countrycode: str | None = None
    customerid: int | None = None
    state: str | None = None
    street1: str | None = None
    street2: str | None = None
    street3: str | None = None
    type: str | None = None
    zip: str | None = None


@dataclasses.dataclass
class Appoptin(Model):
    ip: str | None = None
    message: str | None = None
    method: str | None = None
    status: bool | None = None
    ts: str | None = None


@dataclasses.dataclass
class BatchResultItem(Model):
    id: int | None = None
    msg: str | None = None
    succeeded: bool | None = None


@dataclasses.dataclass
class BatchResult(Model):
    nbrsucceeded: int | None = None
    results: list[BatchResultItem] | None = None


@dataclasses.dataclass
class KeyValueItem(Model):
    key: str | None = None
    value: str | None = None


@dataclasses.dataclass
class Layout(Model):
    color: str | None = None
    maxImage: bool | None = None


@dataclasses.dataclass
class Timestamp(Model):
    systemtime: datetime | None = None


@dataclasses.dataclass
class Url(Model):
    url: str | None = None


@dataclasses.dataclass
class QueryRequest(Model):
    limit: int | None = None
    offset: int | None = None
    query: str | None = None


@dataclasses.dataclass
class QueryResult(Model):
    nbrofresults: int | None = None
    results: list[Any] | None = None


@dataclasses.dataclass
class LogItem(Model):
    id: int | None = None
    orderid: int | None = None
    typeid: int | None = None
    info: Any | None = None
    lookupinfo: Any | None = None
    model: Any | None = None
    ts: datetime | None = None
    userid: int | None = None
    username: str | None = None


@dataclasses.dataclass
class JobResult(Model):
    id: str | None = None
    name: str | None = None
    progress: int | None = None
    progresstext: str | None = None
    status: int | None = None


@dataclasses.dataclass
class AddItemsResult(Model):
    ids: list[int] | None = None
    # order field is typed as Any to avoid circular import; it's an Order instance
    order: Any | None = None


@dataclasses.dataclass
class ServicemailScheduling(Model):
    days: int | None = None
    relative: str | None = None
    time: str | None = None


@dataclasses.dataclass
class FilterItem(Model):
    id: int | None = None
    operator: str | None = None
