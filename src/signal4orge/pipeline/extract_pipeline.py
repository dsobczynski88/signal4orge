class ExtractPipeline:
    """Append landing rows and build the feature panel."""

    def run(self) -> None:
        """Run ingestion, then transformation.

        Startup calls ``configure_logging``. The stage order is
        ``DataIngestion.initiate_data_ingestion``, then
        ``DataTransformation.initiate_data_transformation``. This runner does not
        train, score, mature, or call the read API.
        """
        raise NotImplementedError
