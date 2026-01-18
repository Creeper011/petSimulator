"""Module for defining requirement conditions for pet actions."""

from dataclasses import dataclass
from typing import Callable
from src.models.stat import Stat

@dataclass(frozen=True)
class Requirement():
    """Represents a requirement condition for an action."""
    stat: Stat
    operator: Callable    # ex: operator.lt
    value: float

    def check(self, current_value: float) -> bool:
        """Check if the requirement is met based on the current stat value."""
        return self.operator(current_value, self.value)
