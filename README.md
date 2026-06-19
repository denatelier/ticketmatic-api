# ticketmatic-api

A Python client library for the [Ticketmatic API](https://apps.ticketmatic.com/docs/api).

The distribution is published as `ticketmatic-api`, but it installs the `ticketmatic`
package, so imports use the short name (e.g. `from ticketmatic import Client`).

This library is a port of the official [Ticketmatic PHP SDK](https://github.com/ticketmatic/tm-php) (`ticketmatic/phpsdk`) to idiomatic Python. It covers the full Ticketmatic REST API surface: contacts, events, orders, settings, and more.

> [!IMPORTANT]
> **This project is not affiliated with, endorsed by, or connected to Ticketmatic in any way.** It is an independent, community-maintained library. Ticketmatic is not involved in its development or support. Please direct all questions, bug reports, and issues regarding this library to this project's GitHub page (issue tracker) — do **not** contact Ticketmatic about this project at any time.

## Requirements

- Python 3.11+
- An active [Ticketmatic](https://www.ticketmatic.com/) account with API credentials (access key + secret key)

## Installation

```bash
pip install ticketmatic-api
```

Or install from source:

```bash
git clone <repo-url>
cd ticketmatic-api
pip install -e .
```

## Quick Start

```python
from ticketmatic import Client
from ticketmatic.endpoints import contacts, events, orders

# Create a client
client = Client("myaccount", "your-access-key", "your-secret-key")

# List events
result = events.get_list(client)
for event in result.data:
    print(f"{event.id}: {event.name}")

# Get a single contact
contact = contacts.get(client, 12345)
print(f"{contact.firstname} {contact.lastname}")

# Create an order
order = orders.create(client, {"saleschannelid": 1})
print(f"Order created: {order.orderid}")
```

## Usage

### Authentication

The client uses [TM-HMAC-SHA256](https://apps.ticketmatic.com/docs/api) authentication. Each request is signed automatically — just provide your account code, access key, and secret key.

```python
from ticketmatic import Client

client = Client("myaccount", "access-key", "secret-key")
```

Contact [support@ticketmatic.com](mailto:support@ticketmatic.com) to obtain API credentials.

### Working with Endpoints

Endpoints are organized as module-level functions that take a `Client` as the first argument. You can pass either model objects or plain dicts:

```python
from ticketmatic.endpoints import contacts

# Using a dict (convenient for simple calls)
contact = contacts.create(client, {
    "firstname": "John",
    "lastname": "Doe",
    "email": "john@example.com",
})

# Using a model object (useful for IDE autocompletion)
from ticketmatic.models.contact import ContactQuery

result = contacts.get_list(client, ContactQuery(
    searchterm="John",
    limit=10,
))
```

### Available Endpoints

| Module | Description |
|--------|-------------|
| `endpoints.contacts` | Contact CRUD, batch operations, import, remarks |
| `endpoints.events` | Event CRUD, batch, tickets, lock/unlock, images |
| `endpoints.orders` | Order CRUD, tickets, products, payments, PDF export |
| `endpoints.diagnostics` | Server time check |
| `endpoints.tools` | Account info, custom queries, data export |
| `endpoints.jobs` | Async job status |
| `endpoints.subscribers` | Mailing subscriber sync |
| `endpoints.streams` | Event stream polling |
| `endpoints.sales.waiting_list_requests` | Waiting list management |

**Settings endpoints** (under `endpoints.settings`):

| Module | Description |
|--------|-------------|
| `settings.account_parameters` | Account-level parameters |
| `settings.products` | Products and product categories |
| `settings.vouchers` | Voucher management and codes |
| `settings.communication.*` | Documents, order mails, ticket layouts, web skins |
| `settings.events.event_locations` | Event locations |
| `settings.pricing.*` | Price lists, price types, ticket fees, order fee definitions |
| `settings.seating_plans.*` | Seating plans (with SVG, logical plans), seat ranks |
| `settings.system.*` | Contact fields, custom fields, reports, views, opt-ins, and more |
| `settings.ticket_sales.*` | Delivery scenarios, payment methods/scenarios, sales channels, etc. |

### Streaming

Some endpoints return streaming responses (newline-delimited JSON). Use them as iterators:

```python
from ticketmatic.endpoints import events

with events.get_tickets(client, event_id) as stream:
    for ticket in stream:
        print(ticket["id"], ticket["barcode"])
```

### Widget Signing

To generate signed widget URLs (using separate widget API keys):

```python
from ticketmatic import Widgets

widgets = Widgets("myaccount", "widget-access-key", "widget-secret-key")
url = widgets.generate_url("addtickets", {"event": "123", "skinid": "5"})
```

### Multi-language Support

Set a language to receive translated content:

```python
client.set_language("nl")
result = events.get_list(client)  # Returns Dutch translations
```

### Error Handling

```python
from ticketmatic import ClientException, RateLimitException

try:
    contact = contacts.get(client, 99999)
except RateLimitException as e:
    print(f"Rate limited, retry after {e.backoff} seconds")
except ClientException as e:
    print(f"API error {e.code}: {e}")
```

### Client Configuration

Each client maintains a pooled HTTP connection, so consecutive API calls
reuse the same connection. Close the client when you're done, or use it as
a context manager:

```python
from ticketmatic import Client

with Client("myaccount", "key", "secret") as client:
    result = events.get_list(client)
```

The server URL (e.g. for a staging environment) and request timeout can be
set per client:

```python
client = Client(
    "testaccount",
    "key",
    "secret",
    server="https://qa.ticketmatic.com",
    timeout=10.0,  # seconds, default 30
)
```

Setting `Client.server = "..."` before creating clients still works and
changes the default for all clients that don't pass `server=` explicitly.

## Development

```bash
# Install with dev dependencies
pip install -e ".[dev]"

# Run unit tests
pytest tests/test_models.py tests/test_widgets.py

# Run integration tests (requires API credentials)
TM_TEST_ACCOUNTCODE=xxx TM_TEST_ACCESSKEY=xxx TM_TEST_SECRETKEY=xxx pytest tests/ -m integration
```

## Credits

This library is a Python port of the [Ticketmatic PHP SDK](https://github.com/ticketmatic/tm-php) (`ticketmatic/phpsdk`, build 1.0.122) by [Ticketmatic BVBA](https://www.ticketmatic.com/). The PHP SDK served as the reference implementation for all API endpoints, data models, and authentication logic. Full credit to the Ticketmatic team for the original design and documentation.

This project was created with the help of [Claude Code](https://claude.ai/code) by Anthropic.

## License

MIT License — see [LICENSE](LICENSE) for details.
