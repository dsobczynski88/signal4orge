class ModelTrainer:
    """Fit the ridge on completed quarters for the train job."""

    def initiate_model_trainer(self) -> dict[str, float]:
        """Fit on earlier completed quarters and return the newest quarter's holdout metrics.

        The returned keys are ``rank_correlation``, ``precision``, and ``median_gap``.
        The newest completed quarter is the holdout, so its mistakes stay out of the
        fit until a later run. This stage does not promote a challenger and does not
        write ``prediction_log``.
        """
        raise NotImplementedError

    def evaluate_models(
        self,
        holdout_metrics: dict[str, float],
        champion_metrics: dict[str, float],
    ) -> dict[str, float]:
        """Compare the holdout with the champion's recorded rank correlation and median gap.

        The result uses the same three keys as ``initiate_model_trainer``. Promotion
        remains on ``ModelRegistry``.
        """
        raise NotImplementedError
