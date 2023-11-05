# --- Imports ---
import os
from pathlib import Path

# --- Constants ---
PARENT_DIR = Path(__file__).parent.resolve().parent
DATA_DIR = PARENT_DIR / 'data'


# --- Functions ---
def create_dir_if_not_exists(directory: Path) -> None:
    """Creates the specified directory if it doesn't exist."""
    if not directory.exists():
        os.mkdir(directory)


# --- Directory Creation ---
create_dir_if_not_exists(DATA_DIR)
