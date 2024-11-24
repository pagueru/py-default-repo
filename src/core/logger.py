"""
Configura um logger para o projeto, com suporte para saída de logs
em arquivo e no console, utilizando formatação personalizada.

Configurações do Logger:
- Nível mínimo de log: DEBUG.
- Saída para arquivo: Logs completos são armazenados no arquivo definido em `LOG_FILE_PATH`.
- Saída para console: Logs com nível INFO ou superior são exibidos no console.
- Formato de log: Inclui timestamp, nome do arquivo, nível do log e mensagem, 
  com formato de data 'YYYY-MM-DD HH:MM:SS' (sem microsegundos).
"""

import logging

from .constants import LOG_FILE_PATH

# Atribui um logger com o menor nível necessário
logger: logging.Logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Atribui um handler para o arquivo
file_handler: logging.FileHandler = logging.FileHandler(LOG_FILE_PATH)
file_handler.setLevel(logging.DEBUG)

# Atribui um handler para o console
console_handler: logging.StreamHandler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Atribui um formato de log (sem microsegundos)
formatter: logging.Formatter = logging.Formatter(
    "%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Atribui handlers ao logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
