ticketmatic-api
===============

A Python client library for the `Ticketmatic API
<https://apps.ticketmatic.com/docs/api>`_ — an idiomatic port of the official
`Ticketmatic PHP SDK <https://github.com/ticketmatic/tm-php>`_. It covers the
full REST API surface: contacts, events, orders, settings, widgets and more.

.. note::

   The distribution is published on PyPI as ``ticketmatic-api``, but the
   importable package is ``ticketmatic`` (for example
   ``from ticketmatic import Client``). This project is community-maintained
   and **not affiliated with Ticketmatic**.

Features
--------

- **Complete API coverage** — every endpoint and data type from the official SDK.
- **Typed data models** — dataclasses with full type hints; the package ships ``py.typed``.
- **Dict or model input** — pass plain ``dict``\ s for quick calls or model objects for IDE autocompletion.
- **Streaming** — iterate large event and ticket exports as newline-delimited JSON.
- **Widget signing** — generate signed widget URLs and verify return URLs.
- **Pooled HTTP** — a reusable connection pool per client, built on ``httpx``.

Installation
------------

.. code-block:: bash

   pip install ticketmatic-api

Requires Python 3.11+. See :doc:`guide/installation` for details.

Hello, Ticketmatic
------------------

.. code-block:: python

   from ticketmatic import Client
   from ticketmatic.endpoints import events

   with Client("myaccount", "your-access-key", "your-secret-key") as client:
       result = events.get_list(client)
       for event in result.data:
           print(f"{event.id}: {event.name}")

Continue with :doc:`guide/configuration` to set up a client properly, or jump
straight to the :doc:`examples` for a full order-to-ticket walkthrough.

.. toctree::
   :maxdepth: 2
   :caption: User Guide
   :hidden:

   guide/installation
   guide/configuration
   guide/concepts
   guide/error-handling
   guide/streaming
   guide/widgets

.. toctree::
   :maxdepth: 2
   :caption: Examples
   :hidden:

   examples

.. toctree::
   :maxdepth: 2
   :caption: Reference
   :hidden:

   api/index

Indices
-------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
