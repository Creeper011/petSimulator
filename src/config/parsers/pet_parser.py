"""Parser for pet configuration files format. resolve operations like inf, >number etc."""

import re
from typing import Any, Callable, Dict, Tuple
from src.core.constants import OPERATORS_MAP

# pylint: disable=too-few-public-methods
class PetParser():
    """Parser for pet configuration files format."""

    def _parse_operators(self, condition_str: str) -> Tuple[Callable, float]:
        match = re.match(r"^([<>=!]+)\s*(-?\d+\.?\d*)$", condition_str)

        if not match:
            raise ValueError(f"Invalid condition format: {condition_str}")

        op_sym, value_str = match.groups()
        operator_func = OPERATORS_MAP.get(op_sym)

        if operator_func is None:
            raise ValueError(f"Invalid operator: {op_sym}")
        return operator_func, float(value_str)

    def _parse_types(self, value: Any) -> Any:
        if value == "inf":
            return float("inf")

        if isinstance(value, str):
            if value.isdigit():
                return int(value)

            if any(value.startswith(s) for s in "<>=!"):
                return self._parse_operators(value)

        return value

    def _parse_recursive(self, data: Any) -> Any:
        """Recursively parse all values in the config structure."""
        if isinstance(data, dict):
            return {
                key: self._parse_recursive(value)
                for key, value in data.items()
            }

        if isinstance(data, list):
            return [self._parse_recursive(item) for item in data]

        return self._parse_types(data)

    def parse(self, raw_config: Dict[str, Any]) -> Dict[str, Any]:
        """Parse the raw configuration dictionary."""
        return self._parse_recursive(raw_config)
