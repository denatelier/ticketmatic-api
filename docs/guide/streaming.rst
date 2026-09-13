Streaming
=========

Some endpoints can return very large result sets — for example every ticket in
an event. These are served as **newline-delimited JSON** and exposed as a
:class:`~ticketmatic.stream.Stream`, which you iterate one record at a time
instead of loading everything into memory.

Iterating a stream
------------------

:func:`ticketmatic.endpoints.events.get_tickets` returns a stream. Each item is
a parsed JSON object (a ``dict``):

.. code-block:: python

   from ticketmatic.endpoints import events

   with events.get_tickets(client, event_id) as stream:
       for ticket in stream:
           print(ticket["id"], ticket.get("barcode"))

Use the stream as a context manager (the ``with`` block above) so the
underlying connection is released as soon as you are done — even if you break
out of the loop early.

Long-lived connections
----------------------

A stream can stay open for a long time, so it overrides the client's read
timeout with ``None`` for its lifetime. The connection pool itself belongs to
the :class:`~ticketmatic.client.Client` and is **not** closed when the stream
ends — only when you close the client. This means you can open several streams
from one client and keep using it afterwards:

.. code-block:: python

   with Client("myaccount", "key", "secret") as client:
       with events.get_tickets(client, event_id) as stream:
           count = sum(1 for _ in stream)
       print(f"{count} tickets")
       # client is still usable here for more calls

Polling for changes
-------------------

For keeping an external system in sync, the account **event stream** is a
poll-based alternative: :func:`ticketmatic.endpoints.streams.eventstream`
returns the changes since a given marker rather than a long-lived connection.
See also the ``lastupdatesince`` query parameter on most list endpoints, shown
in :doc:`../examples`.
