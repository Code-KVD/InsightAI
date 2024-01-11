# update entity.
from dataclasses import dataclass
from pathlib import Path

# data classes are special classes in python used to store the data.
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path