class MaturePipeline:
    """Fill realized outcomes after the nowcast quarter has ended."""

    def run(self) -> None:
        """Run maturity for the quarter that just ended.

        Startup calls ``configure_logging``. The only stage is
        ``Maturity.initiate_maturity``, which writes ``forward_return`` and
        ``actual_weak`` on each ``outcome`` row. This runner does not extract,
        score, train, or call the read API.
        """
        raise NotImplementedError
