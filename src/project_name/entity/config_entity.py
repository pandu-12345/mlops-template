from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionEntity:
    source_url: str
    root_dir:Path
    Unzip_dir:Path
    zip_dir:Path