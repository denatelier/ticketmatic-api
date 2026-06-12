"""Integration tests for all settings endpoints."""

import pytest

from ticketmatic import ClientException
from ticketmatic.endpoints.settings import account_parameters, products, vouchers
from ticketmatic.endpoints.settings.communication import documents
from ticketmatic.endpoints.settings.events import event_locations
from ticketmatic.endpoints.settings.pricing import (
    price_types,
    ticket_fees,
    order_fee_definitions,
)
from ticketmatic.endpoints.settings.seating_plans import seating_plans
from ticketmatic.endpoints.settings.system import (
    contact_address_types,
    contact_fields,
    contact_titles,
    field_definitions,
    optins,
    phone_number_types,
    relation_types,
    reports,
    views,
)
from ticketmatic.endpoints.settings.ticket_sales import order_fees, payment_scenarios

pytestmark = pytest.mark.integration


# --- Account Parameters ---


class TestAccountParameters:
    def test_get(self, tm_client):
        result = account_parameters.get_list(tm_client)
        assert len(result) > 0

        param = account_parameters.get(tm_client, "accountname")
        assert param.key == "accountname"
        assert param.value == "qa"


# --- Documents ---


class TestDocuments:
    def test_get(self, tm_client):
        result = documents.get_list(tm_client, {"typeid": 10002})
        assert len(result.data) > 0


# --- Event Locations ---


class TestEventLocations:
    def test_bad_filter(self, tm_client):
        with pytest.raises(ClientException) as exc_info:
            event_locations.get_list(tm_client, {"filter": "INVALID QUERY"})
        assert exc_info.value.code == 400


# --- Price Types ---


class TestPriceTypes:
    def test_get(self, tm_client):
        result = price_types.get_list(tm_client)
        assert len(result.data) > 0

    def test_create_delete(self, tm_client):
        initial = price_types.get_list(tm_client)

        created = price_types.create(tm_client, {"name": "test", "typeid": 2301})
        assert created.id != 0
        assert created.name == "test"
        assert created.createdts is not None

        after_create = price_types.get_list(tm_client)
        assert len(after_create.data) > len(initial.data)

        price_types.delete(tm_client, created.id)

        after_delete = price_types.get_list(tm_client)
        assert len(after_delete.data) == len(initial.data)

    def test_translations(self, tm_client):
        tm_client.set_language("en")
        result = price_types.get_list(tm_client)
        assert len(result.data) > 0

        en_name = result.data[0].name

        tm_client.set_language("nl")
        result_nl = price_types.get_list(tm_client)
        nl_name = result_nl.data[0].name

        # Reset language
        tm_client.language = None

    def test_bad_filter(self, tm_client):
        with pytest.raises(ClientException) as exc_info:
            price_types.get_list(tm_client, {"filter": "INVALID QUERY"})
        assert exc_info.value.code == 400


# --- Ticket Fees ---


class TestTicketFees:
    def test_create(self, tm_client):
        fee = ticket_fees.create(
            tm_client,
            {
                "name": "Fee",
                "rules": {
                    "default": [
                        {"saleschannelid": 1, "status": "fixedfee", "value": 1.5},
                        {"saleschannelid": 2, "status": "percentage", "value": 4},
                    ],
                    "exceptions": [
                        {
                            "pricetypeid": 29,
                            "saleschannels": [
                                {
                                    "saleschannelid": 1,
                                    "status": "fixedfee",
                                    "value": 2.5,
                                },
                            ],
                        }
                    ],
                },
            },
        )
        assert fee.id != 0
        assert fee.name == "Fee"


# --- Seating Plans ---


class TestSeatingPlans:
    def test_create_single_zone(self, tm_client):
        sp = seating_plans.create(tm_client, {"name": "testplan", "status": "draft"})
        assert sp.name == "testplan"
        assert sp.status == "draft"
        assert sp.useszones is False

    def test_create_multi_zone(self, tm_client):
        sp = seating_plans.create(
            tm_client,
            {
                "name": "testplan-multi",
                "status": "draft",
                "useszones": True,
                "zones": [1, 2],
            },
        )
        assert sp.name == "testplan-multi"
        assert sp.useszones is True
        assert sp.zones == [1, 2]

    def test_get(self, tm_client):
        result = seating_plans.get_list(tm_client)
        assert len(result.data) > 0

        sp = seating_plans.get(tm_client, result.data[0].id)
        assert sp.id == result.data[0].id


# --- System: Contact Address Types ---


class TestContactAddressTypes:
    def test_get(self, tm_client):
        result = contact_address_types.get_list(tm_client)
        assert len(result.data) > 0


# --- System: Contact Fields ---


class TestContactFields:
    def test_get(self, tm_client):
        result = contact_fields.get_list(tm_client)
        assert len(result.data) > 0

        field = contact_fields.get(tm_client, result.data[0].id)
        assert field.id > 0


# --- System: Contact Titles ---


class TestContactTitles:
    def test_get(self, tm_client):
        result = contact_titles.get_list(tm_client)
        assert len(result.data) > 0


# --- System: Field Definitions ---


class TestFieldDefinitions:
    def test_get(self, tm_client):
        result = field_definitions.get_list(tm_client, {"typeid": 10004})
        assert len(result.data) > 0


# --- System: Opt-ins ---


class TestOptins:
    def test_get(self, tm_client):
        result = optins.get_list(tm_client)
        assert len(result.data) > 0

    def test_create(self, tm_client):
        created = optins.create(
            tm_client,
            {
                "typeid": 40001,
                "name": "Newsletter",
                "availability": [{"saleschannelid": 1}],
                "caption": "Please subscribe",
                "yescaption": "Yes",
                "nocaption": "No",
            },
        )
        assert created.id != 0
        assert created.typeid == 40001
        assert created.name == "Newsletter"


# --- System: Phone Number Types ---


class TestPhoneNumberTypes:
    def test_get(self, tm_client):
        result = phone_number_types.get_list(tm_client)
        assert len(result.data) > 0


# --- System: Relation Types ---


class TestRelationTypes:
    def test_get(self, tm_client):
        result = relation_types.get_list(tm_client)
        assert len(result.data) > 0


# --- System: Reports ---


class TestReports:
    def test_get(self, tm_client):
        result = reports.get_list(tm_client)
        assert len(result.data) > 0


# --- System: Views ---


class TestViews:
    def test_get(self, tm_client):
        result = views.get_list(tm_client, {"typeid": 10004})
        assert len(result.data) > 0


# --- Ticket Sales: Order Fees ---


class TestOrderFees:
    def test_create_and_delete(self, tm_client):
        fee1 = order_fees.create(
            tm_client,
            {
                "typeid": 2401,
                "name": "Fixed fee",
                "rule": {
                    "auto": [
                        {
                            "saleschannelids": [1],
                            "status": "fixedfee",
                            "value": 5,
                        }
                    ],
                },
            },
        )
        assert fee1.id != 0
        assert fee1.name == "Fixed fee"

        fee2 = order_fees.create(
            tm_client,
            {
                "typeid": 2402,
                "name": "Script fee",
                "rule": {
                    "script": "return 1;",
                    "context": [
                        {"key": "test", "query": "SELECT 1", "cacheable": True}
                    ],
                },
            },
        )
        assert fee2.id != 0

        result = order_fees.get_list(tm_client)
        assert len(result.data) > 1

        order_fees.delete(tm_client, fee1.id)
        order_fees.delete(tm_client, fee2.id)


# --- Ticket Sales: Payment Scenarios ---


class TestPaymentScenarios:
    def test_create(self, tm_client):
        ps = payment_scenarios.create(
            tm_client,
            {
                "typeid": 2705,
                "name": "Payment scenario test",
                "availability": {"saleschannels": [1, 2]},
                "paymentmethods": [1],
                "expiryparameters": {
                    "daysaftercreation": 5,
                    "deleteonexpiry": True,
                },
            },
        )
        assert ps.id != 0
        assert ps.typeid == 2705
        assert ps.name == "Payment scenario test"

    def test_get(self, tm_client):
        ps = payment_scenarios.get(tm_client, 13)
        assert ps.name == "PayPal"


# --- Vouchers ---


class TestVouchers:
    def test_validity(self, tm_client):
        v = vouchers.create(
            tm_client,
            {
                "name": "test",
                "typeid": 24001,
                "validity": {
                    "expiry_monthsaftercreation": 12,
                    "maxusages": 5,
                },
            },
        )
        assert v.validity.expiry_monthsaftercreation == 12
        assert v.validity.maxusages == 5
