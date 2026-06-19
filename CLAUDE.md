# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

`ticketmatic-api` is a Python client library for the [Ticketmatic REST API](https://apps.ticketmatic.com/docs/api). It is an **idiomatic Python port of the official [Ticketmatic PHP SDK](https://github.com/ticketmatic/tm-php)** (`ticketmatic/phpsdk`, build 1.0.122). When adding or changing endpoints/models, mirror the PHP SDK's structure, naming, and URL paths — it is the reference implementation. The project is community-maintained and **not affiliated with Ticketmatic**.

Note the name split: the **distribution** is `ticketmatic-api` (the `[project].name` in `pyproject.toml`, used for `pip install`), while the **importable package** stays `ticketmatic` (`src/ticketmatic/`, `from ticketmatic import Client`). Keep the package directory named `ticketmatic`.

Requires Python 3.11+. The only runtime dependency is `httpx`.

## Commands

```bash
# Editable install with dev tools (required for tests to import `ticketmatic`)
pip install -e ".[dev]"

# Unit tests — no credentials, no network (test_client, test_models, test_request, test_stream, test_widgets)
pytest -m "not integration"

# A single test
pytest tests/test_models.py::TestContactRoundTrip::test_custom_fields

# Integration tests — hit the real QA API; require credentials
TM_TEST_ACCOUNTCODE=xxx TM_TEST_ACCESSKEY=xxx TM_TEST_SECRETKEY=xxx pytest -m integration
# Optional: TM_TEST_SERVER overrides the target (default https://qa.ticketmatic.com)

# Format and lint (run both before committing)
black .
ruff check .          # add --fix to autofix
```

Integration tests skip automatically when credentials are absent, so plain `pytest` runs the unit suite and skips the rest. The `tm_client` fixture (`tests/conftest.py`) builds the client from the `TM_TEST_*` env vars.

ruff config: line-length 88, target py311, rule sets `E,W,F,I,UP,B,C4,SIM` (see `pyproject.toml`).

## Architecture

The library is layered: **Client → Request → Stream**, with **endpoint functions** wrapping requests and **Model dataclasses** handling JSON conversion. Understanding these four pieces explains how any call flows end-to-end.

### Request flow

1. **`Client`** (`client.py`) holds credentials, the per-instance pooled `httpx.Client`, and config (`server`, `version`, `timeout`, `language`). It is a factory: `client.new_request(method, url)` returns a `Request`. Use it as a context manager (or call `close()`) to release the connection pool. Setting `Client.server` (class attribute) changes the default server for all clients that don't pass `server=`.
2. **`Request`** (`request.py`) builds and executes **one** call. It owns: TM-HMAC-SHA256 auth-header signing, URL templating (`{accountname}` → account code, `{id}` and other path params), query encoding (bool → `true`/`false`, dict/list → JSON), body encoding (`json`/`svg`/`jpg`), stripping of `None` values, and error mapping. `.run()` returns parsed JSON (or text); `.stream()` returns a `Stream`.
3. **`Stream`** (`stream.py`) iterates newline-delimited JSON responses (e.g. event/ticket streams). It overrides the pool's read timeout to `None` for long-lived connections and shares — but does not close — the Client's pool.

### Endpoints (`endpoints/`)

Endpoints are **module-level functions, not methods**. Every function takes `client: Client` as its first argument, builds a `Request`, and wraps the response in a model. Callers import modules, e.g. `from ticketmatic.endpoints import contacts; contacts.get_list(client)`.

- Functions accept **either a Model instance or a plain dict** for input; dicts are converted via `Model.from_dict` before sending. Follow this dual-input convention in new endpoints (see `endpoints/contacts.py` for the canonical CRUD shape).
- **Settings endpoints** (`endpoints/settings/**`) are deeply nested (`communication`, `events`, `pricing`, `seating_plans`, `system`, `ticket_sales`) and mostly share one CRUD shape. They delegate to helpers in `endpoints/settings/_crud.py` (`crud_get_list/get/create/update/delete/translations/translate` + the `make_list_type` factory). To add one, declare the URL constants, model, and query field list, then call the `crud_*` helpers rather than hand-rolling — see `endpoints/settings/system/custom_fields.py`.
- List results follow the `{data: [...], nbrofresults: N}` shape, wrapped either by a hand-written dataclass (`ContactsList`) or by `make_list_type`.

### Models (`models/`)

All models are `@dataclasses.dataclass` subclasses of **`Model`** (`models/base.py`), which provides reflection-based `from_dict`/`to_dict` driven by the dataclass type hints (`get_type_hints`). Key behaviors to know before touching models:

- **Type hints are load-bearing at runtime.** `from_dict` reads annotations to recursively coerce nested `Model`s, `datetime` (ISO-8601 round-trip via `json_utils.py`), lists, and optionals/unions. Keep annotations accurate — the package ships `py.typed`.
- **`None` is omitted** from `to_dict` output (and `None` query/body values are dropped in `Request`), matching the API's sparse semantics.
- **Custom fields:** models that set `_has_custom_fields = True` collect `c_`-prefixed JSON keys into a `custom_fields: dict` on the way in, and re-emit them with the `c_` prefix on the way out.
- **Python keyword collisions:** an API field named `from` maps to the dataclass field `from_` and is remapped back on `to_dict` (see `ProductInstancePricetypeValue`). Handle similar collisions the same way.

### Auth — two separate HMAC schemes

- **API requests** (`Request._generate_auth_header`): `TM-HMAC-SHA256 key=… ts=… sign=…`, where `sign = HMAC-SHA256(secret_key, access_key + account_code + timestamp)`.
- **Widgets** (`widgets.py`): a **separate keypair** and a different signature (sorted concat of params, excluding `l`/`ordercode`). `Widgets.generate_url` produces signed widget URLs; `verify_return_url` validates return URLs and raises `VerifyException`.

### Exceptions (`exceptions.py`)

`TicketmaticError` is the base. `ClientException` (non-2xx) parses a JSON error body into `code` / `application_code` / `application_data`. `RateLimitException` (HTTP 429) carries `backoff` from the `retry-after` header. `VerifyException` is for widget verification failures. The public API (`Client`, `Widgets`, exceptions) is re-exported from `ticketmatic/__init__.py`.
