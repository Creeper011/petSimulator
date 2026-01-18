"""Represents pet actions and their properties."""

from dataclasses import dataclass
from typing import Optional, Set
from src.models.requirements import Requirement
from src.models.response import Response
from src.models.effect import Effect
from src.models.hooks import Hooks


@dataclass(frozen=True)
class Action():
    """Represents a pet action with all its properties."""
    name: str
    display_name: str
    cooldown: int
    message: Response
    effects: Optional[Set[Effect]] = None
    requirements: Optional[Set[Requirement]] = None
    hooks: Optional[Hooks] = None
