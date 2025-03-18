"""
Módulo de gerenciamento de logging.

Este módulo fornece a classe `LoggingManager` que facilita a configuração e o gerenciamento de
loggers em um projeto Python. Ele permite configurar handlers de console e arquivo, definir níveis
de log e suprimir mensagens de aviso específicas.
"""

import json
import logging
from pathlib import Path
from typing import TYPE_CHECKING, Any
import warnings

if TYPE_CHECKING:
    from src.common.constypes import PathLike


class LoggingManager:
    """Classe de gerenciamento de logging."""

    def __init__(self, config: dict[str, Any]) -> None:
        """Inicializa a classe LoggerSetup com as configurações fornecidas."""
        # Atribui as configurações
        self._assign_config(config)

        # Inicializa o logger
        self.logger: logging.Logger = self._define_handlers()

    def _assign_config(self, config: dict[str, Any]) -> None:
        """Atribui as configurações do dicionário às variáveis da classe."""
        self.file_enabled: str = config["logging"]["file"]["enabled"]
        self.file_level: str = config["logging"]["file"]["level"]
        self.file_path: PathLike = config["logging"]["file"]["path"]
        self.console_level: str = config["logging"]["console"]["level"]
        self.supress_list: list[str] = config["logging"]["supress"]

    def _ensure_path(self, path_str: str) -> Path:
        """Converte uma string de caminho em um objeto Path e garante que o diretório exista."""
        path: Path = Path(path_str)
        if not path.parent.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
        return path

    def _define_handlers(self) -> logging.Logger:
        """Configura e retorna um logger com handlers para console e arquivo (opcional)."""
        # Cria o logger com o nome do módulo atual
        custom_logger: logging.Logger = logging.getLogger(__name__)
        custom_logger.setLevel(self.console_level)

        # Evita adicionar handlers duplicados
        if custom_logger.hasHandlers():
            return custom_logger

        # Formato do log
        formatter: logging.Formatter = logging.Formatter(
            fmt="%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # Handler para console
        console_handler: logging.StreamHandler[Any] = logging.StreamHandler()
        console_handler.setLevel(self.console_level)
        console_handler.setFormatter(formatter)
        custom_logger.addHandler(console_handler)

        # Handler opcional para arquivo
        if self.file_path and self.file_enabled:
            file_handler: logging.FileHandler = logging.FileHandler(
                self.file_path, encoding="utf-8"
            )
            file_handler.setLevel(self.file_level)
            file_handler.setFormatter(formatter)
            custom_logger.addHandler(file_handler)

        # Suprime mensagens de aviso específicas
        if self.supress_list:
            for warning_message in self.supress_list:
                warnings.filterwarnings(action="ignore", message=warning_message)

        return custom_logger

    def dump_config(self) -> str:
        """Retorna a configuração da classe em um JSON dump sem identação."""
        config_dict = {
            "file_enabled": self.file_enabled,
            "file_level": self.file_level,
            "file_path": str(self.file_path),
            "console_level": self.console_level,
            "supress_list": self.supress_list,
        }
        return json.dumps(config_dict)

    def setup(self) -> logging.Logger:
        """Configura e retorna o logger."""
        return self.logger
