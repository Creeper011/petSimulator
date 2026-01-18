"""Entities models representing the pet and their stats."""

from dataclasses import dataclass
from typing import List
from src.models.action import Action
from src.models.stat import Stat

@dataclass()
class Character():
    """Represents pet character metadata."""
    name: str
    full_name: str
    age: int
    description: str
    stats: List[Stat]
    actions: List[Action]
