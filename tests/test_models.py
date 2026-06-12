"""Unit tests for model serialization round-trips (no API calls needed)."""

from datetime import datetime

from ticketmatic.models.common import Address, BatchResult, Timestamp
from ticketmatic.models.contact import (
    Contact,
    ContactQuery,
)
from ticketmatic.models.event import Event, EventContingent, EventQuery
from ticketmatic.models.order import Order, OrderTicket, Payment
from ticketmatic.models.pricing import (
    PriceType,
    TicketFee,
)
from ticketmatic.models.product import ProductInstancePricetypeValue
from ticketmatic.models.seating import SeatingPlan
from ticketmatic.models.voucher import Voucher


class TestContactRoundTrip:
    def test_basic_fields(self):
        c = Contact.from_dict(
            {"id": 1, "firstname": "John", "lastname": "Doe", "email": "j@test.com"}
        )
        assert c.id == 1
        assert c.firstname == "John"
        d = c.to_dict()
        assert d["id"] == 1
        assert d["firstname"] == "John"

    def test_custom_fields(self):
        c = Contact.from_dict({"id": 1, "c_myfield": "hello", "c_other": 42})
        assert c.custom_fields == {"myfield": "hello", "other": 42}
        d = c.to_dict()
        assert d["c_myfield"] == "hello"
        assert d["c_other"] == 42
        assert "custom_fields" not in d

    def test_nested_addresses(self):
        c = Contact.from_dict(
            {
                "id": 1,
                "addresses": [{"city": "Brussels", "countrycode": "BE"}],
                "phonenumbers": [{"id": 1, "number": "+321234"}],
            }
        )
        assert c.addresses[0].city == "Brussels"
        assert c.phonenumbers[0].number == "+321234"
        d = c.to_dict()
        assert d["addresses"][0]["city"] == "Brussels"

    def test_timestamps(self):
        c = Contact.from_dict({"id": 1, "createdts": "2024-01-15T10:30:00+00:00"})
        assert isinstance(c.createdts, datetime)
        d = c.to_dict()
        assert "2024-01-15" in d["createdts"]

    def test_none_fields_omitted(self):
        c = Contact(id=1, firstname="John")
        d = c.to_dict()
        assert "lastname" not in d
        assert "email" not in d

    def test_optins(self):
        c = Contact.from_dict(
            {
                "id": 1,
                "optins": [
                    {
                        "optinid": 1,
                        "status": 7602,
                        "info": {"method": "api", "remarks": "test"},
                    }
                ],
            }
        )
        assert c.optins[0].optinid == 1
        assert c.optins[0].info.method == "api"

    def test_from_dict_none(self):
        assert Contact.from_dict(None) is None


class TestEventRoundTrip:
    def test_basic(self):
        e = Event.from_dict({"id": 99, "name": "Concert", "currentstatus": 19002})
        assert e.id == 99
        assert e.name == "Concert"

    def test_contingents(self):
        e = Event.from_dict(
            {
                "id": 1,
                "contingents": [{"id": 10, "name": "Main", "amount": 500}],
            }
        )
        assert e.contingents[0].amount == 500
        assert isinstance(e.contingents[0], EventContingent)

    def test_custom_fields(self):
        e = Event.from_dict({"id": 1, "c_category": "jazz"})
        assert e.custom_fields == {"category": "jazz"}

    def test_datetime_fields(self):
        e = Event.from_dict({"id": 1, "startts": "2024-06-15T20:00:00+02:00"})
        assert e.startts is not None
        assert isinstance(e.startts, datetime)


class TestOrderRoundTrip:
    def test_nested_tickets_and_payments(self):
        o = Order.from_dict(
            {
                "orderid": 100,
                "tickets": [{"id": 1, "eventid": 5, "price": 25.50}],
                "payments": [
                    {"id": 1, "amount": 25.50, "paidts": "2024-06-01T10:00:00Z"}
                ],
                "totalamount": 25.50,
                "c_note": "vip",
            }
        )
        assert o.orderid == 100
        assert o.tickets[0].price == 25.50
        assert isinstance(o.tickets[0], OrderTicket)
        assert o.payments[0].amount == 25.50
        assert isinstance(o.payments[0], Payment)
        assert o.custom_fields == {"note": "vip"}

        d = o.to_dict()
        assert d["orderid"] == 100
        assert d["c_note"] == "vip"
        assert d["tickets"][0]["price"] == 25.50


class TestPricingRoundTrip:
    def test_price_type_custom_fields(self):
        pt = PriceType.from_dict({"id": 1, "name": "Normal", "c_color": "red"})
        assert pt.custom_fields == {"color": "red"}
        d = pt.to_dict()
        assert d["c_color"] == "red"

    def test_ticket_fee_rules(self):
        tf = TicketFee.from_dict(
            {
                "id": 1,
                "name": "Fee",
                "rules": {
                    "default": [
                        {"saleschannelid": 1, "status": "fixedfee", "value": 2.50}
                    ],
                    "exceptions": [
                        {
                            "pricetypeid": 5,
                            "saleschannels": [
                                {
                                    "saleschannelid": 1,
                                    "status": "percentage",
                                    "value": 10,
                                }
                            ],
                        }
                    ],
                },
            }
        )
        assert tf.rules.default[0].value == 2.50
        assert tf.rules.exceptions[0].pricetypeid == 5


class TestProductRoundTrip:
    def test_product_instance_pricetype_from_keyword(self):
        """'from' is a Python keyword, mapped to from_."""
        p = ProductInstancePricetypeValue.from_dict({"id": 1, "from": 5})
        assert p.id == 1
        assert p.from_ == 5
        d = p.to_dict()
        assert d["from"] == 5
        assert "from_" not in d


class TestSeatingRoundTrip:
    def test_basic(self):
        sp = SeatingPlan.from_dict(
            {"id": 1, "name": "Main Hall", "useszones": True, "zones": [1, 2]}
        )
        assert sp.useszones is True
        assert sp.zones == [1, 2]


class TestVoucherRoundTrip:
    def test_validity(self):
        v = Voucher.from_dict(
            {
                "id": 1,
                "name": "Gift",
                "validity": {"expiry_monthsaftercreation": 12, "maxusages": 5},
            }
        )
        assert v.validity.expiry_monthsaftercreation == 12
        assert v.validity.maxusages == 5


class TestQueryModels:
    def test_contact_query(self):
        q = ContactQuery.from_dict(
            {"filter": "select id from tm.contact", "limit": 10, "offset": 0}
        )
        assert q.filter == "select id from tm.contact"
        assert q.limit == 10

    def test_event_query_with_nested_filter(self):
        q = EventQuery.from_dict({"simplefilter": {"status": [19001, 19002]}})
        assert q.simplefilter.status == [19001, 19002]


class TestCommonModels:
    def test_timestamp(self):
        ts = Timestamp.from_dict({"systemtime": "2024-01-01T12:00:00Z"})
        assert isinstance(ts.systemtime, datetime)

    def test_batch_result(self):
        br = BatchResult.from_dict(
            {
                "nbrsucceeded": 2,
                "results": [
                    {"id": 1, "succeeded": True},
                    {"id": 2, "succeeded": False, "msg": "error"},
                ],
            }
        )
        assert br.nbrsucceeded == 2
        assert br.results[1].msg == "error"

    def test_address(self):
        a = Address.from_dict({"city": "Ghent", "countrycode": "BE", "zip": "9000"})
        assert a.city == "Ghent"
        assert a.zip == "9000"
