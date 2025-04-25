from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass(frozen=True)
class DataIngestionEntity:
    source_url: str
    root_dir:Path
    Unzip_dir:Path
    zip_dir:Path

@dataclass(frozen=True)
class dataTransformEntity:
    data_type: str
    raw_data_dirc: Path
    transformed_data_dirc: Path
    image_size: Optional[tuple]=None
    label_columns: Optional[str]=None

@dataclass(frozen=True)
class trainingEntity:
    model_dir: Path
    epochs: int
    training_data: Path
    batch_size: int
    learning_rate: int
    image_size: tuple
    num_classes: int


@dataclass(frozen=True)
class modelevaluationentity:
    model_path: Path
    test_data_path: Path
    image_size: tuple
    batch_size: int
    result: Path