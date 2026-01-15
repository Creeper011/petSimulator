"""Unit tests for the TOML configuration loader."""

from unittest.mock import MagicMock, patch
from src.config.loaders.toml_loader import TomlLoader

def test_load_toml_config_load_success():
    """Test loading a TOML configuration file successfully."""

    mock_logger = MagicMock()
    mock_toml_file = MagicMock()

    mock_toml_file.read.return_value = b"""
    app_name = "foo"
    version = "1.0.0"

    [settings]
    debug_mode = true
    database_url = "https://example.com/db"
    """

    mock_toml_file.__enter__.return_value = mock_toml_file

    with patch("pathlib.Path.open", return_value=mock_toml_file):
        toml_loader = TomlLoader(logger=mock_logger)

        result = toml_loader.load_config()

        assert result["app_name"] == "foo"
        assert result["version"] == "1.0.0"
        assert result["settings"]["debug_mode"] is True
        assert result["settings"]["database_url"] == "https://example.com/db"
