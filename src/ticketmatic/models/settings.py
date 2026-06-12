from __future__ import annotations

import dataclasses
from datetime import datetime
from typing import Any, ClassVar

from ticketmatic.models.base import Model

# --- Custom Fields ---


@dataclasses.dataclass
class CustomfieldAvailability(Model):
    saleschannels: list[int] | None = None
    script: str | None = None
    usescript: bool | None = None


@dataclasses.dataclass
class CustomField(Model):
    id: int | None = None
    typeid: int | None = None
    availability: CustomfieldAvailability | None = None
    caption: str | None = None
    description: str | None = None
    edittypeid: int | None = None
    fieldtypeid: int | None = None
    key: str | None = None
    manualsort: bool | None = None
    requiredtypeid: int | None = None
    isarchived: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class CustomFieldQuery(Model):
    typeid: int | None = None
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None


@dataclasses.dataclass
class CustomFieldValue(Model):
    id: int | None = None
    typeid: int | None = None
    caption: str | None = None
    sortorder: int | None = None
    isarchived: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class CustomFieldValueQuery(Model):
    typeid: int | None = None
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None


# --- Delivery Scenarios ---


@dataclasses.dataclass
class DeliveryscenarioAvailability(Model):
    saleschannels: list[int] | None = None
    script: str | None = None
    usescript: bool | None = None


@dataclasses.dataclass
class DeliveryScenario(Model):
    _has_custom_fields: ClassVar[bool] = True

    id: int | None = None
    typeid: int | None = None
    name: str | None = None
    allowetickets: int | None = None
    availability: DeliveryscenarioAvailability | None = None
    deliverystatusaftertrigger: int | None = None
    feedescription: str | None = None
    internalremark: str | None = None
    logo: str | None = None
    mailorganization: bool | None = None
    needsaddress: bool | None = None
    ordermailtemplateid_delivery: int | None = None
    ordermailtemplateid_deliverystarted: int | None = None
    shortdescription: str | None = None
    visibility: str | None = None
    isarchived: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None
    custom_fields: dict[str, Any] | None = None


@dataclasses.dataclass
class DeliveryScenarioQuery(Model):
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None


# --- Documents ---


@dataclasses.dataclass
class DocumentOptions(Model):
    nbrperpage: int | None = None


@dataclasses.dataclass
class Document(Model):
    id: int | None = None
    typeid: int | None = None
    name: str | None = None
    css: str | None = None
    description: str | None = None
    enabled: bool | None = None
    htmltemplate: str | None = None
    options: DocumentOptions | None = None
    translations: list[str] | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class DocumentQuery(Model):
    typeid: int | None = None
    filter: str | None = None
    lastupdatesince: datetime | None = None


# --- Dupe Detect ---


@dataclasses.dataclass
class DupeDetectCriteria(Model):
    field: str | None = None
    matcher: str | None = None


@dataclasses.dataclass
class DupeDetectRule(Model):
    id: int | None = None
    name: str | None = None
    criteria: list[DupeDetectCriteria] | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class DupeDetectRuleQuery(Model):
    filter: str | None = None
    lastupdatesince: datetime | None = None


# --- Field Definitions ---


@dataclasses.dataclass
class FieldDefinition(Model):
    id: int | None = None
    typeid: int | None = None
    align: str | None = None
    description: str | None = None
    key: str | None = None
    sqlclause: str | None = None
    uitype: str | None = None
    variablewidth: bool | None = None
    width: int | None = None
    isarchived: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class FieldDefinitionQuery(Model):
    typeid: int | None = None
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None


@dataclasses.dataclass
class FielddefinitionsDataRequest(Model):
    typeid: int | None = None
    fielddefinitions: list[str] | None = None
    ids: list[int] | None = None


@dataclasses.dataclass
class FielddefinitionsDataResult(Model):
    id: int | None = None
    data: Any | None = None


# --- Filter Definitions ---


@dataclasses.dataclass
class FilterDefinition(Model):
    id: int | None = None
    typeid: int | None = None
    checklistquery: str | None = None
    description: str | None = None
    filtertype: int | None = None
    sqlclause: str | None = None
    visible: bool | None = None
    isarchived: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class FilterDefinitionQuery(Model):
    typeid: int | None = None
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None


# --- Opt-Ins ---


@dataclasses.dataclass
class OptInAvailability(Model):
    saleschannelid: int | None = None


@dataclasses.dataclass
class OptIn(Model):
    id: int | None = None
    typeid: int | None = None
    name: str | None = None
    availability: list[OptInAvailability] | None = None
    caption: str | None = None
    description: str | None = None
    nocaption: str | None = None
    yescaption: str | None = None
    isarchived: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class OptInQuery(Model):
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None


# --- Relation Types ---


@dataclasses.dataclass
class RelationType(Model):
    id: int | None = None
    name: str | None = None
    parentid: int | None = None
    isarchived: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class RelationTypeQuery(Model):
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None


# --- Reports ---


@dataclasses.dataclass
class ReportOptions(Model):
    excelpagewidth: int | None = None
    excelscaling: float | None = None
    pdfpagesize: str | None = None
    usesystemfont: bool | None = None


@dataclasses.dataclass
class Report(Model):
    id: int | None = None
    name: str | None = None
    content: Any | None = None
    defaultformat: str | None = None
    description: str | None = None
    emailbcc: str | None = None
    emailcc: str | None = None
    emailrecipients: str | None = None
    emailschedule: bool | None = None
    emailscheduledayofmonth: int | None = None
    emailscheduledayofweek: int | None = None
    emailschedulehourofday: int | None = None
    emailschedulequery: str | None = None
    options: ReportOptions | None = None
    reporttypeid: int | None = None
    subtitles: list[str] | None = None
    translations: list[str] | None = None
    usagetypeid: int | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class ReportQuery(Model):
    filter: str | None = None
    lastupdatesince: datetime | None = None


# --- Sales Channels ---


@dataclasses.dataclass
class SalesChannel(Model):
    id: int | None = None
    typeid: int | None = None
    name: str | None = None
    ordermailtemplateid_confirmation: int | None = None
    ordermailtemplateid_confirmation_sendalways: bool | None = None
    isarchived: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class SalesChannelQuery(Model):
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None


# --- Views ---


@dataclasses.dataclass
class ViewColumn(Model):
    id: int | None = None


@dataclasses.dataclass
class View(Model):
    id: int | None = None
    typeid: int | None = None
    name: str | None = None
    columns: list[ViewColumn] | None = None
    orderby: int | None = None
    orderby_asc: bool | None = None
    isarchived: bool | None = None
    createdts: datetime | None = None
    lastupdatets: datetime | None = None


@dataclasses.dataclass
class ViewQuery(Model):
    typeid: int | None = None
    filter: str | None = None
    includearchived: bool | None = None
    lastupdatesince: datetime | None = None
