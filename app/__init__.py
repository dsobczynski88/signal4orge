"""Read API for the current flag, the model version, and the monitor totals.

Schemas, request dependencies, and route modules are exported from this package
as they are created. A request reads ``prediction_log``, ``outcome``, and the
promoted registry row through ``signal4orge.db``. It does not score, train, or
call a job runner.
"""

from app.deps import get_db
from app.main import create_app
from app.routes.health import health
from app.routes.monitor import monitor
from app.routes.scores import score_for_ticker, scores_for_quarter
from app.schemas import MonitorSummary, Score, TickerScore

__all__ = [
    "MonitorSummary",
    "Score",
    "TickerScore",
    "create_app",
    "get_db",
    "health",
    "monitor",
    "score_for_ticker",
    "scores_for_quarter",
]
