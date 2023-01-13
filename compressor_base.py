from pathlib import Path
from typing import Callable


CompressionFunction = Callable[
    [Path, Path], None
]  # accepts input and output file paths
