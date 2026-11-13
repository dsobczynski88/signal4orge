"""Read routes for health, scores, and the monitor summary.

Each route module adds its function to this package when that module is created.
``GET /health`` answers without a database session. Score and monitor routes
receive the request session from ``get_db`` and return a schema from
``app.schemas``. No route calls a job runner.
"""

from app.routes.health import health
from app.routes.monitor import monitor
from app.routes.scores import score_for_ticker, scores_for_quarter

__all__ = ["health", "monitor", "score_for_ticker", "scores_for_quarter"]
