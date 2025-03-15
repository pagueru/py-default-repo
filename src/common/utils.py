"""
Módulo de utilitários do projeto.

Este módulo fornece a classe `ProjectUtils` que contém métodos para diversas tarefas
comuns em projetos.

Classes:
    ProjectUtils: Classe de utilitários do projeto.
"""

from logging import Logger
import os
from pathlib import Path
import platform
import time
from typing import Any
import winsound

import yaml

from src.common.constypes import PathLike


class ProjectUtils:
    """Classe de utilitários do projeto."""

    def __init__(self, start_dir: Path | None = None, logger: Logger | None = None):
        """Inicializa a classe ProjectUtils."""
        self.start_dir = start_dir or Path.cwd()
        self.repo_path = Path(__file__).resolve().parent.parent.parent
        self.logger = logger
        self.timer = time.time()

    def set_logger(self, logger: Logger) -> None:
        """Define o logger para a instância da classe."""
        self.logger = logger

    def log_msg(self, message: str, level: str = "info") -> None:
        """Registra uma mensagem usando o logger, se disponível, ou imprime no console."""
        if self.logger:
            if level == "error":
                self.logger.error(message)
            elif level == "debug":
                self.logger.debug(message)
            else:
                self.logger.info(message)
        else:
            print(message)  # noqa: T201

    def find_project_root(self) -> Path:
        """Encontra o diretório raiz do projeto a partir do diretório que instancia a classe."""
        start_path: Path = self.start_dir
        for parent in start_path.parents:
            if (parent / "pyproject.toml").exists():
                return parent
        return Path("./").resolve()

    def add_gitkeep_if_empty(self) -> None:
        """Adiciona um arquivo .gitkeep em diretórios vazios do repositório."""
        self.log_msg(f"Verificando diretórios vazios em {self.repo_path}", "debug")
        total_dirs = 0
        existing_gitkeep = 0
        created_gitkeep = 0

        for current_path, subdirectories, filenames in os.walk(self.repo_path):
            # Ignorar diretórios .git e .venv
            filtered_subdirectories: list[str] = []
            for subdir in subdirectories:
                if subdir not in [".git", ".venv"]:
                    filtered_subdirectories.append(subdir)
            subdirectories[:] = filtered_subdirectories

            total_dirs += 1

            # Verificar se o diretório está vazio
            if not filenames and not subdirectories:
                gitkeep_path = Path(current_path) / ".gitkeep"
                gitkeep_path.touch()
                created_gitkeep += 1
                self.log_msg(f"Adicionado .gitkeep em {current_path}")
            # Verificar se .gitkeep já existe
            elif ".gitkeep" in filenames:
                existing_gitkeep += 1
                self.log_msg(f".gitkeep já existe em {current_path}", "debug")

        self.log_msg(
            f"Verificação de diretórios vazios concluída. Total: {total_dirs}, "
            f"Existentes: {existing_gitkeep}, Criados: {created_gitkeep}"
        )

    def terminal_line(self, value: int = 79, char: str = "-") -> None:
        """Imprime uma linha no terminal com o caractere especificado."""
        if value <= 0:
            msg = "O valor deve ser maior que 0."
            raise ValueError(msg)
        print(char * value)  # noqa: T201

    def start_config(self, *, clear_terminal: bool = True) -> None:
        """Limpa o terminal e marca o início do script."""
        try:
            if clear_terminal:
                os_name = platform.system().lower()
                if os_name == "windows":
                    print("\033c", end="")  # noqa: T201
                else:
                    print("\033c", end="")  # noqa: T201
            self.terminal_line()
            self.log_msg("Iniciando o script.")
        except RuntimeError as e:
            self.log_msg(f"Erro ao limpar o terminal: {e}", "error")
            raise

    def execution_time(self, *, beep: bool = False) -> None:
        """Calcula e registra o tempo de execução do script."""
        self.log_msg(f"Tempo de execução: {round(time.time() - self.timer, 2)} segundos")
        if beep:
            winsound.Beep(750, 300)

    def load_yaml_file(self, file_path: PathLike) -> dict[str, Any]:
        """Carrega um arquivo YAML e retorna como um dicionário."""
        file_path = self.convert_to_path(file_path)
        with file_path.open("r", encoding="utf-8") as file:
            data: dict[str, Any] = yaml.safe_load(file)
        return data

    def convert_to_path(
        self, path_input: str | PathLike, *, create_if_not_exists: bool = False
    ) -> Path:
        """Converte um PathLike em um objeto Path e garante que o diretório exista."""
        path: Path = Path(path_input)
        if not path.exists():
            if create_if_not_exists:
                if path.suffix:
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.touch()
                else:
                    path.mkdir(parents=True, exist_ok=True)
                self.log_msg(f"Caminho {path} criado.")
            else:
                self.log_msg(f"Caminho {path} não existe.", "error")
                raise FileNotFoundError
        return path
