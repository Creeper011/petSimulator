"""Effect model for pet actions."""

from dataclasses import dataclass
from src.models.stat import Stat

@dataclass(frozen=True)
class Effect():
    """Represents an effect on a stat."""
    stat: Stat
    value: float
