"""Response model for the pet."""

from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Response():
    """Represents success and failure messages for an action."""
    success: str
    fail: Optional[str] = None
