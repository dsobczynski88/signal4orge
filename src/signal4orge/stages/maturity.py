class Maturity:
    """Fill realized outcomes after a filing quarter has ended."""

    def initiate_maturity(self) -> None:
        """Join each prediction_log row to its realized return and set actual_weak.

        ``outcome`` points at one prediction_log row. ``forward_return`` and
        ``actual_weak`` stay empty until this stage runs, and the prediction stays
        pending until then. A miss against the worst-fifth label is a confusion-matrix
        count, not a training row by itself. This stage does not train.
        """
        raise NotImplementedError
