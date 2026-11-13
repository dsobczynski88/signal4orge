from app.schemas import MonitorSummary


def monitor(session: object) -> MonitorSummary:
    """Return the pending count and the running confusion totals. Served at ``GET /monitor``.

    ``session`` comes from ``get_db``. ``pending_count`` counts predictions that
    still have no outcome. The four confusion counts and the model version come
    from matured rows and the promoted registry row. ``Monitor.summarize`` is the
    calculation. This route does not call a job runner.
    """
    raise NotImplementedError
