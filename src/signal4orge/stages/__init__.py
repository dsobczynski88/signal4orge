"""Pipeline stages for the extract, mature, and train jobs.

Each stage module adds its public class to this package when that module is created.
The score job does not use a stage here. It loads the champion from ``models/champion/``.
``Monitor`` is read by the API and does not train.
"""

from signal4orge.stages.data_ingestion import DataIngestion
from signal4orge.stages.data_transformation import DataTransformation
from signal4orge.stages.maturity import Maturity
from signal4orge.stages.model_trainer import ModelTrainer
from signal4orge.stages.monitor import Monitor

__all__ = [
    "DataIngestion",
    "DataTransformation",
    "Maturity",
    "ModelTrainer",
    "Monitor",
]
