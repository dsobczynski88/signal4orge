def get_db() -> object:
    """Open one Postgres session for this request.

    The session comes from ``signal4orge.db.get_session``. The request closes it
    when the response is finished. Job runners call ``get_session`` themselves.
    """
    raise NotImplementedError
