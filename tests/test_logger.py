"""Testes para o módulo de logging."""

# pylint: disable=redefined-outer-name

import logging
from typing import Any

import pytest

from src.common.logger import LoggingManager


@pytest.fixture
def config() -> dict[str, Any]:
    """Fixture para fornecer um dicionário de configuração de logging."""
    return {
        "logging": {
            "file": {"enabled": True, "level": "DEBUG", "path": "logs/test.log"},
            "console": {"level": "INFO"},
            "supress": [],
        }
    }


def test_logging_manager_initialization(config: dict[str, Any]) -> None:
    """Testa a inicialização do LoggingManager com um dicionário de configuração."""
    manager = LoggingManager(config)
    assert manager.file_enabled == config["logging"]["file"]["enabled"]
    assert manager.file_level == config["logging"]["file"]["level"]
    assert str(manager.file_path) == config["logging"]["file"]["path"]
    assert manager.console_level == config["logging"]["console"]["level"]
    assert manager.supress_list == config["logging"]["supress"]


def test_logging_manager_dump_config(config: dict[str, Any]) -> None:
    """Testa o método dump_config do LoggingManager."""
    manager = LoggingManager(config)
    config_dump = manager.dump_config()
    assert '"file_enabled": true' in config_dump
    assert '"file_level": "DEBUG"' in config_dump
    assert '"file_path": "logs/test.log"' in config_dump
    assert '"console_level": "INFO"' in config_dump
    assert '"supress_list": []' in config_dump


def test_logging_manager_setup(config: dict[str, Any]) -> None:
    """Testa o método setup do LoggingManager."""
    manager = LoggingManager(config)
    logger = manager.setup()
    assert isinstance(logger, logging.Logger)
