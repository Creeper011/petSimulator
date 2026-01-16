"""Unit tests for the pet configuration parser."""

# pylint: disable=wrong-import-order
# pylint: disable=protected-access

import pytest
import operator
from src.config.parsers.pet_parser import PetParser

def test_pet_parser_parse_types():
    """Test parsing of different types in the pet configuration parser."""

    parser = PetParser()

    assert parser._parse_types("inf") == float("inf")
    assert parser._parse_types(">42") == (operator.gt, 42.0)

    op, value = parser._parse_types("> 10")
    assert op(11, value) is True
    assert op(5, value) is False
    assert op(10, value) is False

    assert parser._parse_types("some_string") == "some_string"
    assert parser._parse_types(3.14) == 3.14

def test_pet_parser_parse_recursive():
    """Test recursive parsing of nested structures in the pet configuration parser."""

    parser = PetParser()

    raw_config = {
        "stats": {
            "hunger": {
                "max": "inf",
                "min": 0
            },
            "happiness": {
                "max": ">100",
                "min": 0
            }
        },
        "actions": [
            {"name": "feed", "effect": "<50"},
            {"name": "play", "effect": ">=20"}
        ]
    }

    parsed_config = parser.parse(raw_config)

    assert parsed_config["stats"]["hunger"]["max"] == float("inf")
    assert parsed_config["stats"]["hunger"]["min"] == 0

    op, value = parsed_config["stats"]["happiness"]["max"]
    assert op(101, value) is True
    assert op(100, value) is False

    op_feed, value_feed = parsed_config["actions"][0]["effect"]
    assert op_feed(49, value_feed) is True
    assert op_feed(50, value_feed) is False

    op_play, value_play = parsed_config["actions"][1]["effect"]
    assert op_play(20, value_play) is True
    assert op_play(19, value_play) is False

def test_pet_parser_invalid_operator():
    """Test that invalid operator strings raise ValueError."""

    parser = PetParser()

    with pytest.raises(ValueError):
        parser._parse_types(">>42")
