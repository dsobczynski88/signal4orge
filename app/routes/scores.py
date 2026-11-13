from app.schemas import Score, TickerScore


def scores_for_quarter(quarter: str, session: object) -> list[Score]:
    """Return every served score for one quarter. Served at ``GET /scores``.

    ``quarter`` is the query value, such as ``2026Q1``. ``session`` comes from
    ``get_db``. Each ``Score`` is read from ``prediction_log``. ``pending`` is true
    when that row has no outcome yet. This route does not call a job runner.
    """
    raise NotImplementedError


def score_for_ticker(ticker: str, session: object) -> TickerScore:
    """Return the served score for one ticker. Served at ``GET /scores/{ticker}``.

    ``ticker`` is ``PredictionLog.company``. ``session`` comes from ``get_db``.
    This route does not call a job runner.
    """
    raise NotImplementedError
