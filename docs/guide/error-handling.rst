Error handling
==============

All exceptions raised by the library derive from
:class:`~ticketmatic.exceptions.TicketmaticError`, so you can catch everything
with a single ``except`` if you want to.

The hierarchy
-------------

- :class:`~ticketmatic.exceptions.TicketmaticError` — base class.

  - :class:`~ticketmatic.exceptions.ClientException` — the API returned a
    non-success HTTP status.
  - :class:`~ticketmatic.exceptions.RateLimitException` — HTTP 429; you are
    being rate limited.
  - :class:`~ticketmatic.exceptions.VerifyException` — widget return-URL
    verification failed (see :doc:`widgets`).

ClientException
---------------

When the API responds with an error it usually includes a JSON body, which is
parsed into structured attributes:

.. code-block:: python

   from ticketmatic import ClientException
   from ticketmatic.endpoints import contacts

   try:
       contact = contacts.get(client, 99999)
   except ClientException as e:
       print(e)                    # human-readable message
       print(e.code)               # numeric error code
       print(e.application_code)   # application-specific code, if any
       print(e.application_data)   # extra data, if any

Rate limiting
-------------

:class:`~ticketmatic.exceptions.RateLimitException` carries a ``backoff`` value
(seconds, from the ``Retry-After`` header). A simple retry loop:

.. code-block:: python

   import time
   from ticketmatic import RateLimitException
   from ticketmatic.endpoints import events

   for attempt in range(5):
       try:
           result = events.get_list(client)
           break
       except RateLimitException as e:
           time.sleep(e.backoff)
   else:
       raise RuntimeError("still rate limited after 5 attempts")

Catching everything
-------------------

Because the exceptions share a base class, you can handle the specific cases
you care about and fall back to the base for the rest:

.. code-block:: python

   from ticketmatic import ClientException, RateLimitException, TicketmaticError

   try:
       order = orders.create(client, {"saleschannelid": 1})
   except RateLimitException as e:
       ...   # back off and retry
   except ClientException as e:
       ...   # inspect e.code / e.application_code
   except TicketmaticError:
       ...   # anything else from the library
