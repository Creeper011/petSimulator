"""Configuration model for the application settings."""

from dataclasses import dataclass
from src.models.entities.pet import Character

@dataclass(frozen=True)
class ApplicationSettings():
    """Dataclass representing application settings."""
    pet_character: Character
