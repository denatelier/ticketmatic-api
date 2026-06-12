from __future__ import annotations

import os

import pytest

from ticketmatic.client import Client


def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line("markers", "integration: requires TM API credentials")


@pytest.fixture
def tm_client() -> Client:
    """Create a Ticketmatic API client from environment variables.

    Required env vars:
        TM_TEST_ACCOUNTCODE  - Account code (short name)
        TM_TEST_ACCESSKEY    - API access key
        TM_TEST_SECRETKEY    - API secret key

    Optional:
        TM_TEST_SERVER       - Override server URL (default: https://qa.ticketmatic.com)
    """
    account_code = os.environ.get("TM_TEST_ACCOUNTCODE", "")
    access_key = os.environ.get("TM_TEST_ACCESSKEY", "")
    secret_key = os.environ.get("TM_TEST_SECRETKEY", "")

    if not all([account_code, access_key, secret_key]):
        pytest.skip(
            "Missing TM_TEST_ACCOUNTCODE, TM_TEST_ACCESSKEY, or TM_TEST_SECRETKEY"
        )

    server = os.environ.get("TM_TEST_SERVER", "https://qa.ticketmatic.com")

    return Client(account_code, access_key, secret_key, server=server)
