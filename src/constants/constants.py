"""
Módulo de definição de constantes globais para o projeto.

Este módulo contém definições de constantes globais que são usadas em todo o projeto.
"""

from pathlib import Path
from zoneinfo import ZoneInfo

from common.constypes import PathLike


class GlobalConstants:
    """Constantes globais do projeto."""

    @property
    def app_name(self) -> str:
        """Nome da aplicação."""
        return "py-default-repo"

    @property
    def version(self) -> str:
        """Versão da aplicação."""
        return "0.1.0"

    @property
    def config_file(self) -> PathLike:
        """Caminho para o arquivo de configuração."""
        return Path("./src/config/config.yaml")

    @property
    def timezone(self) -> ZoneInfo:
        """Fuso horário padrão."""
        return ZoneInfo("UTC")
