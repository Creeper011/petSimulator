"""Defines hooks for actions."""

from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Hooks():
    """Represents action hooks (commands to execute)."""
    on_success: Optional[str] = None
    on_fail: Optional[str] = None
