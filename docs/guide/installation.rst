Installation
============

Requirements
------------

- **Python 3.11** or newer.
- The only runtime dependency is `httpx <https://www.python-httpx.org/>`_,
  which is installed automatically.

From PyPI
---------

.. code-block:: bash

   pip install ticketmatic-api

This installs the ``ticketmatic-api`` distribution, which provides the
importable ``ticketmatic`` package:

.. code-block:: python

   from ticketmatic import Client

From source
-----------

.. code-block:: bash

   git clone <repo-url>
   cd ticketmatic-api
   pip install -e .

Optional extras
---------------

Two optional dependency groups are available:

- ``dev`` — the test suite and linters (``pytest``, ``pytest-httpx``, ``black``, ``ruff``).
- ``docs`` — the documentation toolchain (``sphinx``, ``furo``).

.. code-block:: bash

   pip install -e ".[dev]"     # contributing / running tests
   pip install -e ".[docs]"    # building this documentation

API credentials
---------------

Every API call is authenticated with three values issued by Ticketmatic:

- an **account code** (your account's short name),
- an **access key**, and
- a **secret key**.

Contact `support@ticketmatic.com <mailto:support@ticketmatic.com>`_ to obtain
credentials. Ticketmatic also runs a separate **QA** environment
(``https://qa.ticketmatic.com``) that is useful for development and testing;
see :doc:`configuration` for how to target it.

.. warning::

   Treat the secret key like a password. Load credentials from the environment
   or a secrets manager rather than hard-coding them — see
   :ref:`credentials-from-the-environment`.
