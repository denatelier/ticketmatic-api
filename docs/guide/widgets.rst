Widgets
=======

Ticketmatic widgets are signed URLs that embed sales flows (ticket selection,
checkout, …) into your own site. Signing uses :class:`~ticketmatic.widgets.Widgets`.

.. important::

   Widgets use a **separate key pair** from the API client. You need a distinct
   widget access key and secret key — the API credentials from
   :doc:`configuration` will not work here.

Generating a signed URL
-----------------------

Create a :class:`~ticketmatic.widgets.Widgets` helper with your widget
credentials and call :meth:`~ticketmatic.widgets.Widgets.generate_url` with the
widget name and its parameters:

.. code-block:: python

   from ticketmatic import Widgets

   widgets = Widgets("myaccount", "widget-access-key", "widget-secret-key")

   url = widgets.generate_url("addtickets", {"event": "123", "skinid": "5"})
   # -> https://apps.ticketmatic.com/widgets/myaccount/addtickets?event=123&...&signature=...

The returned URL carries the access key and a computed signature, so you can
hand it directly to a browser redirect or embed it in a page.

Verifying a return URL
----------------------

When a widget redirects the customer back to your site, verify that the
parameters were not tampered with using
:meth:`~ticketmatic.widgets.Widgets.verify_return_url`. It raises
:class:`~ticketmatic.exceptions.VerifyException` on any mismatch:

.. code-block:: python

   from ticketmatic import VerifyException

   # `params` is the query string of the request your endpoint received.
   try:
       widgets.verify_return_url(params)
   except VerifyException:
       # signature missing, wrong access key, or tampered parameters
       abort(400)
