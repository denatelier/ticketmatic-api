Core concepts
=============

The library has a small, consistent shape. Once you understand these four
ideas, every endpoint behaves the same way.

Client, endpoints, models
-------------------------

A call always flows through three layers:

#. A :class:`~ticketmatic.client.Client` holds your credentials and connection.
#. An **endpoint function** builds and runs one request.
#. A **model** wraps the response.

Endpoints are **module-level functions, not methods**. Each takes the client as
its first argument. Import the module you need and call its functions:

.. code-block:: python

   from ticketmatic.endpoints import contacts, events, orders

   events.get_list(client)
   contacts.get(client, 12345)
   orders.create(client, {"saleschannelid": 1})

Endpoint modules mirror the API structure — for example settings live under
:mod:`ticketmatic.endpoints.settings` (``from ticketmatic.endpoints.settings
import products``).

Dicts or models
---------------

Functions that take input accept **either a plain dict or a model object**.
Dicts are convenient for quick calls; model objects give you IDE
autocompletion and type checking. These two calls are equivalent:

.. code-block:: python

   from ticketmatic.models.contact import Contact

   contacts.create(client, {"firstname": "John", "lastname": "Doe"})
   contacts.create(client, Contact(firstname="John", lastname="Doe"))

Models are :class:`~ticketmatic.models.base.Model` dataclasses with
``from_dict`` / ``to_dict`` conversion. Two things worth knowing:

- **Fields set to** ``None`` **are omitted** from what is sent, matching the
  API's sparse semantics — only the fields you set are transmitted.
- **Timestamps** are exposed as ``datetime`` objects and serialized back to
  ISO-8601 automatically.

List results
------------

Endpoints that return a collection wrap it in a small list object exposing
``data`` (the items) and ``nbrofresults`` (the total available, ignoring
``limit``/``offset``):

.. code-block:: python

   result = events.get_list(client)
   print(result.nbrofresults, "events total")
   for event in result.data:
       print(event.id, event.name)

Query objects (for example
:class:`~ticketmatic.models.event.EventQuery`) carry the supported filter,
paging and search parameters:

.. code-block:: python

   from ticketmatic.models.event import EventQuery

   page = events.get_list(client, EventQuery(searchterm="concert", limit=20))

Custom fields
-------------

Many objects support account-defined **custom fields**. On the wire these use a
``c_`` prefix; the library collects them into a ``custom_fields`` dict and
restores the prefix on the way out:

.. code-block:: python

   contact = contacts.get(client, 12345)
   contact.custom_fields            # {"my_field": "value", ...}

   contacts.update(client, 12345, {"custom_fields": {"my_field": "new value"}})
