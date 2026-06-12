import pytest

from ticketmatic.exceptions import VerifyException
from ticketmatic.widgets import Widgets


def test_signing():
    w = Widgets(
        "club",
        "142dda885ec6024f934a40c1",
        "abd2e5893bd447dc7331af1db8df42fdc62fc5c8f9f04784",
    )

    url = w.generate_url(
        "addtickets",
        {
            "event": "123",
            "skinid": "25",
            "returnurl": "http://www.ticketmatic.com",
            "l": "fr",
        },
    )

    # Strip the hostname
    start = url.index("/widgets")
    path = url[start:]

    assert path == (
        "/widgets/club/addtickets?"
        "event=123&skinid=25&returnurl=http%3A%2F%2Fwww.ticketmatic.com&l=fr"
        "&accesskey=142dda885ec6024f934a40c1"
        "&signature=ae727e02cea8c27322a24af487af950b4d8d26978e57151bfed7e356dd593c00"
    )


@pytest.fixture
def widgets() -> Widgets:
    return Widgets(
        "club",
        "142dda885ec6024f934a40c1",
        "abd2e5893bd447dc7331af1db8df42fdc62fc5c8f9f04784",
    )


def test_verify_return_url_accepts_valid_signature(widgets: Widgets):
    params = {"event": "123", "orderid": "456"}
    params["accesskey"] = widgets.access_key
    params["signature"] = widgets._calculate_signature(
        {"event": "123", "orderid": "456"}
    )

    widgets.verify_return_url(params)  # must not raise


def test_verify_return_url_rejects_wrong_signature(widgets: Widgets):
    params = {
        "event": "123",
        "accesskey": widgets.access_key,
        "signature": "0" * 64,
    }

    with pytest.raises(VerifyException, match="Signature mismatch"):
        widgets.verify_return_url(params)


def test_verify_return_url_rejects_missing_signature(widgets: Widgets):
    params = {"event": "123", "accesskey": widgets.access_key}

    with pytest.raises(VerifyException, match="Signature missing"):
        widgets.verify_return_url(params)


def test_verify_return_url_rejects_bad_access_key(widgets: Widgets):
    params = {"event": "123", "accesskey": "wrong-key", "signature": "0" * 64}

    with pytest.raises(VerifyException, match="Bad access key"):
        widgets.verify_return_url(params)
