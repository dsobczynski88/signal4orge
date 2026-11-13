class DataIngestion:
    """Append source rows to the landing table for the extract job."""

    def initiate_data_ingestion(self) -> None:
        """Append filings and daily bars to landing as retrieved, without training.

        Landing rows are stored as retrieved and are not overwritten. This stage does
        not build feature_panel and does not read prices from after TimePoint A.
        """
        raise NotImplementedError
