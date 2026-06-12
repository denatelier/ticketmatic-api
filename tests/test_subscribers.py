import pytest

from ticketmatic.endpoints import subscribers

pytestmark = pytest.mark.integration


def test_sync(tm_client):
    subscribers.sync(
        tm_client,
        [
            {"email": "subscriber@ticketmatic.com", "subscribed": True},
        ],
    )
