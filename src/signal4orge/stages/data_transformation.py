class DataTransformation:
    """Build the feature panel for the extract job."""

    def initiate_data_transformation(self) -> None:
        """Write the five TimePoint A features onto feature_panel.

        A row is one company in one filing quarter, unique on that pair. Prices from
        after TimePoint A are out of reach. Serving uses the champion artifact, so
        this stage does not fit a scaler and does not train.
        """
        raise NotImplementedError
