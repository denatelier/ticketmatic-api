import pytest

from ticketmatic.endpoints import tools

pytestmark = pytest.mark.integration


def test_info(tm_client):
    info = tools.account(tm_client)
    assert info.id == 998


def test_queries(tm_client):
    result = tools.queries(tm_client, {
        "limit": 2,
        "query": "SELECT * FROM tm.paymentscenario",
    })
    assert result.nbrofresults > 1
    assert len(result.results) == 2
