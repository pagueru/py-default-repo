"""
Módulo de utilitários para o projeto.

Este módulo contém funções auxiliares que facilitam o desenvolvimento e manutenção do projeto. 
Inclui operações como limpeza do terminal e inicialização de configurações, além de qualquer 
outra funcionalidade de suporte que possa ser adicionada futuramente.

Funções:
- start_config(): Limpa o terminal e registra o início do script.
"""

import os
import platform

from .logger import logger


def start_config() -> None:
    """
    Limpa o terminal e registra o início do script.

    Raises:
        Exception: Erro ao limpar a tela

    Returns:
        None
    """
    try:
        # Detecta o sistema operacional e limpa a tela
        os.system("cls" if platform.system() == "Windows" else "clear")

    except Exception as e:
        logger.error(f"Erro ao limpar a tela: {e}")
        raise

    # Registra o início do script
    logger.info("Iniciando o script.")
