"""Configuration model for the application settings."""

from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class ApplicationSettings():
    """Dataclass representing application settings."""
    pet_actions: Dict[str, Dict[str, Any]]
