"""
Define constantes baseadas nos caminhos do sistema de arquivos, facilitando o acesso a diretórios
e arquivos frequentemente utilizados no projeto.

- Caminhos absolutos para pastas
- Caminhos absolutos para arquivos
"""

from pathlib import Path

# Atribui as constantes raízes
FILE_PATH = Path(__file__).resolve()
PROJECT_PATH = FILE_PATH.parents[2]

# Atribui as constantes de pastas
CONFIG_FOLDER_PATH = PROJECT_PATH / "config"
DATA_FOLDER_PATH = PROJECT_PATH / "data"
LOG_FOLDER_PATH = PROJECT_PATH / "logs"
SRC_FOLDER_PATH = PROJECT_PATH / "src"
CORE_FOLDER_PATH = SRC_FOLDER_PATH / "core"

# Atribui as constantes de arquivos
LOG_FILE_PATH = LOG_FOLDER_PATH / "app.log"
DOCS_YAML_FILE_PATH = CONFIG_FOLDER_PATH / "docstringmanager.yaml"
DOCSTRINGMANAGER_FILE_PATH = SRC_FOLDER_PATH / "docstringmanager.py"
