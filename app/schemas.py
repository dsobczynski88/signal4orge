from dataclasses import dataclass


@dataclass
class Score:
    """One company's served score for a quarter on ``GET /scores``.

    ``ticker`` is ``PredictionLog.company``. ``weak_flag`` is the current flag.
    ``pending`` is true until that prediction has an outcome.
    """

    ticker: str
    quarter: str
    score: float
    weak_flag: bool
    model_version: str
    pending: bool


@dataclass
class TickerScore:
    """The served score for one ticker on ``GET /scores/{ticker}``.

    ``ticker`` is ``PredictionLog.company``. The fields match ``Score``.
    """

    ticker: str
    quarter: str
    score: float
    weak_flag: bool
    model_version: str
    pending: bool


@dataclass
class MonitorSummary:
    """The model version, the pending count, and the running confusion totals.

    The four counts include only rows whose return has arrived. They stay at zero
    until the first quarter matures.
    """

    model_version: str
    pending_count: int
    flagged_and_weak: int
    flagged_and_not_weak: int
    unflagged_and_weak: int
    unflagged_and_not_weak: int
