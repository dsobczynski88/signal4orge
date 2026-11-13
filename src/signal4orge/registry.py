from pathlib import Path


class ModelRegistry:
    """Decides whether a challenger replaces the promoted weights in ``models/champion/``."""

    def __init__(self, champion_dir: Path | None = None) -> None:
        """Remember the directory that holds the promoted weights."""
        self.champion_dir = Path("models/champion") if champion_dir is None else champion_dir

    def promote_if_clears(
        self,
        train_through_quarter: str,
        artifact_path: Path,
        rank_correlation: float,
        precision: float,
        median_gap: float,
    ) -> bool:
        """Return whether the challenger replaced the champion.

        The bar is the champion's recorded rank correlation, precision, and median-return
        gap. Rank correlation near +0.067 and precision near 30.8% describe that record,
        and this module does not store them as constants. A promotion records the
        train-through quarter, artifact path, those three metrics, and the promoted time.
        """
        raise NotImplementedError
