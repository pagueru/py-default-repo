"""
Módulo de utilitários para o projeto.

Este módulo contém funções auxiliares que facilitam o desenvolvimento e manutenção do projeto. 
Inclui operações como limpeza do terminal, inicialização de configurações, e configuração de 
log, além de qualquer outra funcionalidade de suporte que possa ser adicionada futuramente.

Funções:
- start_config: Limpa o terminal e registra o início do script.
- ensure_directory_exists: Garante que o diretório especificado exista, criando-o se necessário.
- setup_logger: Configura o logger para registrar mensagens do sistema.
"""

import logging
import os
import platform
from pathlib import Path
from typing import Optional, Union

try:
    from .constants import LOG_FILE
except ImportError:
    from constants import LOG_FILE


def setup_logger(
    log_file_path: Optional[Union[Path, str]] = None,
    enable_file_log: bool = False,
    level: int = logging.INFO,
) -> logging.Logger:
    """
    Configura e retorna um logger personalizado.

    Args:
        log_file_path (Path | str): Caminho para o arquivo de log. Se o valor for
            None, o log será escrito apenas para a saída padrão. (padrão: "./logs/app.log")
        enable_file_log (bool): Habilita ou desabilita o log em arquivo. (padrão: False)
        level (int): Nível de log. (padrão: logging.INFO)

    Retorna:
        logging.Logger: Logger configurado.
    """
    logger_setup: logging.Logger = logging.getLogger(__name__)
    logger_setup.setLevel(level)

    if logger_setup.hasHandlers():
        logger_setup.handlers.clear()

    # Formato do log, com suporte a um campo personalizado e valor padrão
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(custom_filename)s:%(lineno)-3d - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Define uma função de filtro para adicionar um campo personalizado ao log
    def add_defaults_to_record(record: logging.LogRecord) -> bool:
        if not hasattr(record, "custom_filename"):
            record.custom_filename = record.filename
        return True

    # Handler para console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    console_handler.addFilter(add_defaults_to_record)
    logger_setup.addHandler(console_handler)

    # Handler opcional para arquivo
    if log_file_path and enable_file_log:
        file_handler = logging.FileHandler(log_file_path, encoding="utf-8")
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        file_handler.addFilter(add_defaults_to_record)
        logger_setup.addHandler(file_handler)

    return logger_setup


# Inicializa o logger
logger = setup_logger(log_file_path=LOG_FILE, enable_file_log=True, level=logging.DEBUG)


def start_config() -> None:
    """
    Limpa o terminal e registra o início do script.

    Raises:
        RuntimeError: Erro ao limpar a tela
    """
    try:
        # Detecta o sistema operacional e limpa a tela
        os.system("cls" if platform.system() == "Windows" else "clear")

    except Exception as e:
        logger.error(f"Erro ao limpar a tela: {e}")
        raise RuntimeError from e

    # Registra o início do script
    logger.info("Iniciando o script.", extra={"custom_filename": "main.py"})
