class TrainPipeline:
    """Fit a challenger on completed quarters and ask the registry about promotion."""

    def run(self) -> None:
        """Run the trainer, then the registry.

        Startup calls ``configure_logging``. ``ModelTrainer.initiate_model_trainer``
        returns the newest quarter's holdout metrics, and ``save_object`` writes the
        challenger. ``ModelRegistry.promote_if_clears`` is the only following call.
        The caller runs this after maturity. This runner does not extract, score,
        mature, or call the read API.
        """
        raise NotImplementedError
