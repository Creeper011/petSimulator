"""Defines the Stat model."""

from dataclasses import dataclass

@dataclass()
class Stat():
    """Represents a stat with its constraints."""
    name: str
    value: float
    min: float
    max: float
