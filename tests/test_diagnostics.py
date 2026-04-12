import time

import pytest

from ticketmatic.endpoints import diagnostics

pytestmark = pytest.mark.integration


def test_get_time(tm_client):
    result = diagnostics.time(tm_client)
    assert result.systemtime.timestamp() > time.time() - 3600
