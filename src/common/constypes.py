"""
Módulo de definição de tipos personalizados para caminhos.

Este módulo contém definições de tipos personalizados utilizando TypeAlias para representar
caminhos e listas de caminhos.
"""

from pathlib import Path

type PathLike = str | Path
"""Tipo que representa um caminho, podendo ser uma string ou um objeto Path."""

type PathLikeAndList = PathLike | list[PathLike]
"""Tipo que representa um caminho ou uma lista de caminhos (strings ou objetos Path)."""
