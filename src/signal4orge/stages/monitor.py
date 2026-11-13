class Monitor:
    """Summarize matured and pending predictions for the read API."""

    def summarize(self) -> dict[str, object]:
        """Count pending rows apart from matured rows, and total the confusion matrix.

        The four counts and the median-return gap use only rows whose return has
        arrived. Keys are ``pending_count``, ``matured_count``, ``flagged_and_weak``,
        ``flagged_and_not_weak``, ``unflagged_and_weak``, ``unflagged_and_not_weak``,
        and ``median_gap``. Precision near 30.8% is the baseline. An alert is two
        matured quarters in which the flagged group's typical return is no longer
        worse, or precision falls to the 20% a random flag would get. Feature drift
        is a warning beside that result. One ticker is a cell in the matrix.
        """
        raise NotImplementedError
