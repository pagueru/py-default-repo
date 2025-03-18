"""
Este módulo define enumerações e constantes globais usadas no projeto.

Este módulo contém definições de enumerações para padronização de valores no sistema.
"""

import enum


class BaseEnum(enum.Enum):
    """Classe base para enumerações no projeto."""

    @classmethod
    def to_dict(cls) -> dict[str, str | int]:
        """Converte a enumeração em um dicionário."""
        return {item.name: item.value for item in cls}

    @classmethod
    def values(cls) -> list[str | int]:
        """Retorna todos os valores da enumeração."""
        return [item.value for item in cls]

    @classmethod
    def names(cls) -> list[str]:
        """Retorna todos os nomes da enumeração."""
        return [item.name for item in cls]
