def health() -> dict[str, str]:
    """Report that the read API process is up. Served at ``GET /health``.

    The response is ``{"status": "ok"}``. This route does not open a database
    session and does not call a job runner.
    """
    raise NotImplementedError
