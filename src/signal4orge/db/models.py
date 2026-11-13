from dataclasses import dataclass
from datetime import datetime


@dataclass
class Landing:
    """A filing or a daily bar, stored as retrieved and not overwritten."""

    kind: str
    body: str
    retrieved_at: datetime


@dataclass
class FeaturePanel:
    """One company in one filing quarter. That pair is unique.

    The five feature columns, measured as of TimePoint A, are not named here.
    """

    company: str
    quarter: str


@dataclass
class PredictionLog:
    """The score served for one company, with the features used that day.

    ``feature_snapshot`` is the five served values, stored as JSON.
    """

    id: int
    company: str
    quarter: str
    score: float
    weak_flag: bool
    feature_snapshot: dict[str, float]
    model_version: str
    as_of: datetime


@dataclass
class Outcome:
    """The realized return for one ``prediction_log`` row.

    ``forward_return`` and ``actual_weak`` stay empty until the quarter ends.
    """

    prediction_id: int
    forward_return: float | None = None
    actual_weak: bool | None = None


@dataclass
class ModelRegistryRow:
    """The promoted model's recorded bar and the path to its weights."""

    train_through_quarter: str
    artifact_path: str
    rank_correlation: float
    precision: float
    median_gap: float
    promoted_time: datetime
