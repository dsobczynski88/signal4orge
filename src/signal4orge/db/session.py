def get_session() -> object:
    """Open one Postgres session for a single request or a single job run.

    The connection string is ``DATABASE_URL``. The caller closes the session
    when that request or job ends.
    """
    raise NotImplementedError
