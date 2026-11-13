"""FastAPI entry for the read API.

The application built here will bind:

- ``GET /health`` to ``health``
- ``GET /scores`` to ``scores_for_quarter``
- ``GET /scores/{ticker}`` to ``score_for_ticker``
- ``GET /monitor`` to ``monitor``

Score and monitor routes receive the session from ``get_db``. No route calls a
job runner. This module does not construct the FastAPI application yet.
"""


def create_app() -> object:
    """Build the read API. The FastAPI application is not constructed yet."""
    raise NotImplementedError
