"""
Módulo de definição de tipos personalizados para caminhos.

Este módulo contém definições de tipos personalizados utilizando TypeAlias para representar
caminhos e listas de caminhos.

Tipos:
    PathLike: Tipo que representa um caminho, podendo ser uma string ou um objeto Path.
    PathLikeAndList: Tipo que representa um caminho ou uma lista de caminhos(strings ou
    objetos Path).
"""

from pathlib import Path
from typing import List, TypeAlias, Union

PathLike: TypeAlias = Union[str, Path]
"""Tipo que representa um caminho, podendo ser uma string ou um objeto Path."""

PathLikeAndList: TypeAlias = Union[PathLike, List[PathLike]]
"""Tipo que representa um caminho ou uma lista de caminhos (strings ou objetos Path)."""
