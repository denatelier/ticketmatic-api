from ticketmatic.widgets import Widgets


def test_signing():
    w = Widgets("club", "142dda885ec6024f934a40c1", "abd2e5893bd447dc7331af1db8df42fdc62fc5c8f9f04784")

    url = w.generate_url("addtickets", {
        "event": "123",
        "skinid": "25",
        "returnurl": "http://www.ticketmatic.com",
        "l": "fr",
    })

    # Strip the hostname
    start = url.index("/widgets")
    path = url[start:]

    assert path == (
        "/widgets/club/addtickets?"
        "event=123&skinid=25&returnurl=http%3A%2F%2Fwww.ticketmatic.com&l=fr"
        "&accesskey=142dda885ec6024f934a40c1"
        "&signature=ae727e02cea8c27322a24af487af950b4d8d26978e57151bfed7e356dd593c00"
    )
