"""Postgres access shared by the job runners and the read API.

Table dataclasses, ``get_session``, and the repositories are exported from this
package as those modules are created. Alembic owns the schema. A runner does not
call the API, and a request does not call a runner. Both talk to Postgres here.
"""

from signal4orge.db.models import (
    FeaturePanel,
    Landing,
    ModelRegistryRow,
    Outcome,
    PredictionLog,
)
from signal4orge.db.repositories import (
    FeaturePanelRepository,
    LandingRepository,
    ModelRegistryRepository,
    OutcomeRepository,
    PredictionLogRepository,
)
from signal4orge.db.session import get_session

__all__ = [
    "FeaturePanel",
    "FeaturePanelRepository",
    "Landing",
    "LandingRepository",
    "ModelRegistryRepository",
    "ModelRegistryRow",
    "Outcome",
    "OutcomeRepository",
    "PredictionLog",
    "PredictionLogRepository",
    "get_session",
]
