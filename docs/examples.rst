Examples
========

This page walks through a complete order — from finding an event to delivering
a ticket — and then collects a few standalone recipes. Every snippet uses the
real endpoint functions and model fields; the specific IDs and values are
placeholders for your account's data.

All examples assume a configured ``client`` (see
:ref:`credentials-from-the-environment`):

.. code-block:: python

   import os
   from ticketmatic import Client

   client = Client(
       os.environ["TM_ACCOUNTCODE"],
       os.environ["TM_ACCESSKEY"],
       os.environ["TM_SECRETKEY"],
   )

Selling a ticket, end to end
----------------------------

The flow below creates an order, adds a ticket, registers a payment, confirms
the order and produces a ticket PDF. The exact business rules (which payment
method, whether confirmation precedes payment) depend on your account's sales
channel and payment scenario configuration, so treat the sequence as a
template.

1. Find an event
~~~~~~~~~~~~~~~~~

Search the event list and pick one:

.. code-block:: python

   from ticketmatic.endpoints import events
   from ticketmatic.models.event import EventQuery

   results = events.get_list(client, EventQuery(searchterm="concert", limit=10))
   event = results.data[0]
   print(f"Selling for {event.id}: {event.name}")

2. Check availability
~~~~~~~~~~~~~~~~~~~~~~

Fetch the full event to inspect its contingents and live availability. Each
availability entry is keyed by ``tickettypeid`` (the contingent):

.. code-block:: python

   event = events.get(client, event.id)

   for avail in event.availability or []:
       print(f"contingent {avail.tickettypeid}: {avail.free} of {avail.total} free")

   # Pick a contingent that still has tickets.
   tickettypeid = next(a.tickettypeid for a in event.availability if a.free > 0)

3. Find or create the customer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Look the customer up by email, and create them if they are new:

.. code-block:: python

   from ticketmatic.endpoints import contacts
   from ticketmatic.models.contact import ContactQuery

   found = contacts.get_list(client, ContactQuery(searchterm="john@example.com"))
   if found.data:
       contact = found.data[0]
   else:
       contact = contacts.create(client, {
           "firstname": "John",
           "lastname": "Doe",
           "email": "john@example.com",
       })

4. Create the order
~~~~~~~~~~~~~~~~~~~~

Create an order on a sales channel and attach the customer:

.. code-block:: python

   from ticketmatic.endpoints import orders

   order = orders.create(client, {"saleschannelid": 1})
   order = orders.update(client, order.orderid, {"customerid": contact.id})
   print("order", order.orderid)

5. Add tickets
~~~~~~~~~~~~~~

Add one or more tickets from the chosen contingent.
:func:`~ticketmatic.endpoints.orders.add_tickets` returns an
:class:`~ticketmatic.models.common.AddItemsResult` whose ``ids`` are the new
ticket IDs:

.. code-block:: python

   result = orders.add_tickets(client, order.orderid, {
       "tickets": [
           {"tickettypeid": tickettypeid},
           {"tickettypeid": tickettypeid},
       ],
   })
   ticket_ids = result.ids
   print("added tickets", ticket_ids)

6. Register a payment
~~~~~~~~~~~~~~~~~~~~~~

Re-read the order to get the amount due, then add a payment:

.. code-block:: python

   order = orders.get(client, order.orderid)

   orders.add_payments(client, order.orderid, {
       "amount": order.totalamount,
       "paymentmethodid": 3,      # one of your account's payment methods
   })

7. Confirm the order
~~~~~~~~~~~~~~~~~~~~~

:func:`~ticketmatic.endpoints.orders.confirm` turns the unconfirmed order into
a firm sale:

.. code-block:: python

   order = orders.confirm(client, order.orderid)
   print("status", order.status)

8. Deliver the tickets
~~~~~~~~~~~~~~~~~~~~~~~

Generate a ticket PDF. The call returns a
:class:`~ticketmatic.models.common.Url` pointing at the rendered document:

.. code-block:: python

   pdf = orders.post_tickets_pdf(client, order.orderid, {"tickets": ticket_ids})
   print("ticket PDF:", pdf.url)


Recipes
-------

Importing contacts in bulk
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:func:`~ticketmatic.endpoints.contacts.import_contacts` accepts a list and
returns a per-row status (``ok``, ``id`` and ``error``):

.. code-block:: python

   statuses = contacts.import_contacts(client, [
       {"firstname": "Ada", "lastname": "Lovelace", "email": "ada@example.com"},
       {"firstname": "Bad", "email": "not-an-email"},
   ])
   for s in statuses:
       print(s.ok, s.id, s.error)

Syncing changes incrementally
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Most list endpoints accept ``lastupdatesince`` so you only fetch what changed
since your last sync. Pass a ``datetime``:

.. code-block:: python

   from datetime import datetime, timezone

   since = datetime(2026, 1, 1, tzinfo=timezone.utc)
   changed = contacts.get_list(client, ContactQuery(lastupdatesince=since))
   print(changed.nbrofresults, "contacts changed")

Streaming every ticket of an event
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For large exports, iterate a stream instead of loading everything at once (see
:doc:`guide/streaming`):

.. code-block:: python

   with events.get_tickets(client, event.id) as stream:
       for ticket in stream:
           print(ticket["id"], ticket.get("barcode"))

Generating a signed widget URL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Widgets use their own key pair (see :doc:`guide/widgets`):

.. code-block:: python

   from ticketmatic import Widgets

   widgets = Widgets("myaccount", "widget-access-key", "widget-secret-key")
   url = widgets.generate_url("addtickets", {"event": str(event.id), "skinid": "5"})

Surviving rate limits
~~~~~~~~~~~~~~~~~~~~~~~

Wrap calls in a small retry helper that honours the server's backoff (see
:doc:`guide/error-handling`):

.. code-block:: python

   import time
   from ticketmatic import RateLimitException

   def with_retry(fn, *args, attempts=5):
       for _ in range(attempts):
           try:
               return fn(*args)
           except RateLimitException as e:
               time.sleep(e.backoff)
       raise RuntimeError("still rate limited")

   result = with_retry(events.get_list, client)

Typed models instead of dicts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Anywhere a dict is accepted you can pass a model for autocompletion and type
checking:

.. code-block:: python

   from ticketmatic.models.contact import Contact

   contacts.create(client, Contact(
       firstname="Grace",
       lastname="Hopper",
       email="grace@example.com",
   ))

Receiving translated content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set a language on the client to receive translatable fields in that language:

.. code-block:: python

   client.set_language("fr")
   event = events.get(client, event.id)   # name/description in French where available
