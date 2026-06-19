"""Endpoint functions for settings account parameters."""

from __future__ import annotations

from ticketmatic.client import Client
from ticketmatic.json_utils import unpack_array
from ticketmatic.models.common import AccountParameter


def get_list(client: Client) -> list[AccountParameter]:
    """Get all configured account parameters.

    :param client: Ticketmatic API client.
    :returns: A list of
        :class:`~ticketmatic.models.common.AccountParameter` objects.
    """
    req = client.new_request("GET", "/{accountname}/settings/accountparameters")
    return unpack_array(AccountParameter, req.run())


def get(client: Client, name: str) -> AccountParameter:
    """Get an account parameter.

    :param client: Ticketmatic API client.
    :param name: Account parameter name.
    :returns: The requested
        :class:`~ticketmatic.models.common.AccountParameter`.
    """
    req = client.new_request("GET", "/{accountname}/settings/accountparameters/{name}")
    req.add_parameter("name", name)
    return AccountParameter.from_dict(req.run())


def set(client: Client, name: str, data: AccountParameter | dict) -> AccountParameter:
    """Set an account parameter.

    :param client: Ticketmatic API client.
    :param name: Account parameter name.
    :param data: Account parameter data to set.
    :returns: The updated
        :class:`~ticketmatic.models.common.AccountParameter`.
    """
    if isinstance(data, dict):
        data = AccountParameter.from_dict(data)
    req = client.new_request("PUT", "/{accountname}/settings/accountparameters/{name}")
    req.add_parameter("name", name)
    req.set_body(data.to_dict())
    return AccountParameter.from_dict(req.run())
