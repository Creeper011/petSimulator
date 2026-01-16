"""Module-level constants for the project."""

import operator
from pathlib import Path

DEFAULT_TOML_CONFIG_PATH: Path = Path("config.toml")
DEFAULT_ENV_FILE_PATH: Path = Path(".env")
OPERATORS_MAP = {
    "<": operator.lt,
    ">": operator.gt,
    "<=": operator.le,
    ">=": operator.ge,
    "==": operator.eq,
    "!=": operator.ne
}
