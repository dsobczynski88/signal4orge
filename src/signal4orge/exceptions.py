class Signal4orgeError(Exception):
    """Raised when a signal4orge job cannot finish its own work.

    Callers attach the original failure with ``raise Signal4orgeError(msg) from exc``
    so the underlying traceback stays intact.
    """
