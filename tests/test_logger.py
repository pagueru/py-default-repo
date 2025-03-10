# pylint: disable=W0621

import logging

import pytest

from src.common.logger import LoggingManager


@pytest.fixture
def config():
    return {
        "logging": {
            "file": {"enabled": True, "level": "DEBUG", "path": "logs/test.log"},
            "console": {"level": "INFO"},
            "supress": [],
        }
    }


def test_logging_manager_initialization(config):
    manager = LoggingManager(config)
    assert manager.file_enabled == config["logging"]["file"]["enabled"]
    assert manager.file_level == config["logging"]["file"]["level"]
    assert str(manager.file_path) == config["logging"]["file"]["path"]
    assert manager.console_level == config["logging"]["console"]["level"]
    assert manager.supress_list == config["logging"]["supress"]


def test_logging_manager_dump_config(config):
    manager = LoggingManager(config)
    config_dump = manager.dump_config()
    assert '"file_enabled": true' in config_dump
    assert '"file_level": "DEBUG"' in config_dump
    assert '"file_path": "logs/test.log"' in config_dump
    assert '"console_level": "INFO"' in config_dump
    assert '"supress_list": []' in config_dump


def test_logging_manager_setup(config):
    manager = LoggingManager(config)
    logger = manager.setup()
    assert isinstance(logger, logging.Logger)
