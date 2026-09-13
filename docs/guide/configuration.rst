Configuration
=============

Everything starts with a :class:`~ticketmatic.client.Client`. It holds your
credentials and a pooled HTTP connection, and acts as a factory for every API
call.

Creating a client
------------------

The three credentials are positional arguments:

.. code-block:: python

   from ticketmatic import Client

   client = Client("myaccount", "your-access-key", "your-secret-key")

The client signs each request automatically using the
`TM-HMAC-SHA256 <https://apps.ticketmatic.com/docs/api>`_ scheme — you never
build the ``Authorization`` header yourself.

Choosing a server
-----------------

By default the client talks to production (``https://apps.ticketmatic.com``).
Pass ``server`` to target another environment, such as QA:

.. code-block:: python

   client = Client(
       "testaccount",
       "your-access-key",
       "your-secret-key",
       server="https://qa.ticketmatic.com",
   )

To change the default for *every* client that does not pass ``server``
explicitly, set the class attribute once at startup:

.. code-block:: python

   Client.server = "https://qa.ticketmatic.com"

Timeout
-------

The per-request timeout defaults to 30 seconds. Override it with ``timeout``
(in seconds):

.. code-block:: python

   client = Client("myaccount", "key", "secret", timeout=10.0)

.. note::

   Streaming endpoints override the read timeout with ``None`` for the duration
   of the stream, so long-lived exports are not cut off. See :doc:`streaming`.

Translated content
------------------

Many objects carry translatable fields. Call
:meth:`~ticketmatic.client.Client.set_language` to receive content in a given
language; it is sent as the ``Accept-Language`` header on subsequent requests:

.. code-block:: python

   client.set_language("nl")   # Dutch
   result = events.get_list(client)

Connection pooling and cleanup
------------------------------

Each client owns a pooled ``httpx`` connection, so consecutive calls reuse the
same connection. Use the client as a context manager so the pool is released
when you are done:

.. code-block:: python

   with Client("myaccount", "key", "secret") as client:
       result = events.get_list(client)
   # connection pool closed here

If you cannot use a ``with`` block, call
:meth:`~ticketmatic.client.Client.close` explicitly:

.. code-block:: python

   client = Client("myaccount", "key", "secret")
   try:
       ...
   finally:
       client.close()

.. _credentials-from-the-environment:

Credentials from the environment
--------------------------------

Avoid hard-coding secrets. A common pattern is to read them from environment
variables:

.. code-block:: python

   import os
   from ticketmatic import Client

   client = Client(
       os.environ["TM_ACCOUNTCODE"],
       os.environ["TM_ACCESSKEY"],
       os.environ["TM_SECRETKEY"],
       server=os.environ.get("TM_SERVER", "https://apps.ticketmatic.com"),
   )

The examples in :doc:`../examples` assume a client constructed this way.
