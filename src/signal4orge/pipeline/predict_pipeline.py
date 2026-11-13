class PredictPipeline:
    """Score every company with the promoted model and write the prediction log."""

    def run(self) -> None:
        """Load the champion, then write one prediction_log row per company.

        Startup calls ``configure_logging``. ``load_object`` reads ``models/champion/``.
        Each row stores the score, the weak flag, the five feature values as JSON, the
        model version, and the as-of time. This runner does not refit, and it does not
        call extract, mature, train, or the read API.
        """
        raise NotImplementedError
