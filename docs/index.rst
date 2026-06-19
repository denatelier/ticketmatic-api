ticketmatic-api
===============

A Python client library for the `Ticketmatic API
<https://apps.ticketmatic.com/docs/api>`_ — an idiomatic port of the official
`Ticketmatic PHP SDK <https://github.com/ticketmatic/tm-php>`_.

.. note::

   The distribution is published as ``ticketmatic-api``, but the importable
   package is ``ticketmatic`` (for example ``from ticketmatic import Client``).
   This project is community-maintained and **not affiliated with Ticketmatic**.

Quick start
-----------

.. code-block:: python

   from ticketmatic import Client
   from ticketmatic.endpoints import contacts, events

   with Client("myaccount", "access-key", "secret-key") as client:
       for event in events.get_list(client).data:
           print(event.id, event.name)

       contact = contacts.get(client, 12345)
       print(contact.firstname, contact.lastname)

.. toctree::
   :maxdepth: 2
   :caption: Contents

   api/index

Indices
-------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
