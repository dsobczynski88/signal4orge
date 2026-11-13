"""Runners for the extract, score, mature, and train jobs.

Each runner module adds its public class to this package when that module is created.
A runner calls its own stages and does not call another runner or the read API.
The score runner loads the champion from ``models/champion/``.
"""

from signal4orge.pipeline.extract_pipeline import ExtractPipeline
from signal4orge.pipeline.predict_pipeline import PredictPipeline
from signal4orge.pipeline.mature_pipeline import MaturePipeline
from signal4orge.pipeline.train_pipeline import TrainPipeline

__all__ = ["ExtractPipeline", "PredictPipeline", "MaturePipeline", "TrainPipeline"]
