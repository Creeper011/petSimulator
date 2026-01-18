"""Test TOML loader with real config.toml file (Requires a valid config.toml!)"""

import logging
from typing import Any, Dict
from src.config.loaders.toml_loader import TomlLoader

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_real_toml_loader() -> Dict[str, Any]:
    """Test the TOML loader with a real config.toml file."""

    toml_loader = TomlLoader(logger=logger) # init loader using the default path
    settings = toml_loader.load_config()

    assert settings is not None

    return settings

if __name__ == "__main__":
    logger.info("Running real TOML loader test...")
    settings_data = test_real_toml_loader()
    logger.info("Loaded settings: %s", settings_data)
