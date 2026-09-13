"""Sphinx configuration for the ticketmatic-api documentation.

Build the HTML docs from the repository root with::

    pip install -e ".[docs]"
    sphinx-build -b html docs docs/_build/html

or use the provided ``docs/Makefile`` (``make -C docs html``).
"""

import os
import sys

# Make the ``ticketmatic`` package importable for autodoc even when the project
# is not installed (e.g. a clean checkout on a CI runner).
sys.path.insert(0, os.path.abspath("../src"))

# -- Project information ------------------------------------------------------

project = "ticketmatic-api"
author = "ticketmatic-api contributors"
copyright = "2026, ticketmatic-api contributors"  # noqa: A001

try:
    from importlib.metadata import version as _pkg_version

    release = _pkg_version("ticketmatic-api")
except Exception:
    release = "1.0.2"
version = release

# -- General configuration ----------------------------------------------------

# The codebase uses reStructuredText field lists (:param:/:returns:/:class:),
# so napoleon (Google/NumPy style) is intentionally not enabled.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Autodoc / autosummary ----------------------------------------------------

# Generate stub pages for everything referenced by ``.. autosummary::``.
autosummary_generate = True

# Document members in source order so dataclass fields keep their declared order.
autodoc_member_order = "bysource"

# Keep the (often very large) dataclass __init__ signature off the class header.
autodoc_class_signature = "separated"

autodoc_default_options = {
    "members": True,
    "show-inheritance": True,
}

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# -- HTML output --------------------------------------------------------------

html_theme = "furo"
html_static_path = ["_static"]
html_title = f"ticketmatic-api {release}"
html_baseurl = "https://denatelier-ticketmatic-api.readthedocs-hosted.com/en/latest/"
