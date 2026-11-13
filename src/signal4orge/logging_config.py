import logging
from pathlib import Path

_LOG_FORMAT = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"


def configure_logging(log_dir: Path | None = None) -> None:
    """Attach one file handler under ``logs/``, and leave an existing setup unchanged.

    Later modules log with ``logging.getLogger(__name__)``. Pipeline runners call
    this once at startup. Importing this module does not configure logging.
    """
    root = logging.getLogger()
    if root.handlers:
        return

    directory = Path("logs") if log_dir is None else log_dir
    directory.mkdir(parents=True, exist_ok=True)
    handler = logging.FileHandler(directory / "signal4orge.log", encoding="utf-8")
    handler.setFormatter(logging.Formatter(_LOG_FORMAT))
    root.setLevel(logging.INFO)
    root.addHandler(handler)
