from signal4orge.db.models import (
    FeaturePanel,
    Landing,
    ModelRegistryRow,
    Outcome,
    PredictionLog,
)


class LandingRepository:
    """Append filings and daily bars."""

    def __init__(self, session: object) -> None:
        """Store the session for this request or job run."""
        self._session = session

    def append(self, row: Landing) -> None:
        """Append one retrieved filing or daily bar. An existing row is left as stored."""
        raise NotImplementedError


class FeaturePanelRepository:
    """Write one company-quarter of TimePoint A features."""

    def __init__(self, session: object) -> None:
        """Store the session for this request or job run."""
        self._session = session

    def upsert(self, row: FeaturePanel) -> None:
        """Insert or replace the row for one company and quarter."""
        raise NotImplementedError


class PredictionLogRepository:
    """Write the score served for one company."""

    def __init__(self, session: object) -> None:
        """Store the session for this request or job run."""
        self._session = session

    def add(self, row: PredictionLog) -> None:
        """Insert one prediction_log row, including the feature snapshot."""
        raise NotImplementedError


class OutcomeRepository:
    """Fill the realized return for one logged prediction."""

    def __init__(self, session: object) -> None:
        """Store the session for this request or job run."""
        self._session = session

    def attach(self, row: Outcome) -> None:
        """Write forward_return and actual_weak for one prediction_log row."""
        raise NotImplementedError


class ModelRegistryRepository:
    """Read and record the promoted model."""

    def __init__(self, session: object) -> None:
        """Store the session for this request or job run."""
        self._session = session

    def promoted(self) -> ModelRegistryRow | None:
        """Return the row marked promoted."""
        raise NotImplementedError

    def record(self, row: ModelRegistryRow) -> None:
        """Store a promotion, including the artifact path and the recorded bar."""
        raise NotImplementedError
