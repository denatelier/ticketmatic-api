"""Subscriber management for e-mail marketing integration."""

from __future__ import annotations

from ticketmatic.client import Client
from ticketmatic.json_utils import unpack_array
from ticketmatic.models.stream_models import SubscriberCommunication, SubscriberSync


def sync(client: Client, data: list[SubscriberSync | dict]) -> list[SubscriberSync]:
    """Sync mail-tool changes to Ticketmatic.

    Contacts that are subscribed for e-mail marketing actions are
    automatically synced to the configured e-mail marketing tool. Use this
    method to push subscription changes back from the mail tool into
    Ticketmatic.

    :param client: Ticketmatic API client.
    :param data: List of :class:`~ticketmatic.models.stream_models.SubscriberSync`
        objects (or dicts) describing the changes to sync.
    :returns: List of updated
        :class:`~ticketmatic.models.stream_models.SubscriberSync` objects.
    """
    body = []
    for item in data:
        if isinstance(item, dict):
            item = SubscriberSync.from_dict(item)
        body.append(item.to_dict())
    req = client.new_request("POST", "/{accountname}/subscribers/sync")
    req.set_body(body)
    return unpack_array(SubscriberSync, req.run())


def communications(client: Client) -> list[SubscriberCommunication]:
    """Create a new communication based on a list of subscriber e-mail addresses.

    Creates a new communication entry in Ticketmatic derived from the list
    of subscriber e-mail addresses known to the configured e-mail marketing
    tool.

    :param client: Ticketmatic API client.
    :returns: List of
        :class:`~ticketmatic.models.stream_models.SubscriberCommunication`
        objects.
    """
    req = client.new_request("GET", "/{accountname}/subscribers/communications")
    return unpack_array(SubscriberCommunication, req.run())
