from pathlib import Path


def save_object(path: Path, obj: object) -> None:
    """Write a scikit-learn object with joblib. Promoted weights belong under ``models/champion/``."""
    raise NotImplementedError


def load_object(path: Path) -> object:
    """Read a joblib object. The score job loads the promoted file from ``models/champion/``."""
    raise NotImplementedError
