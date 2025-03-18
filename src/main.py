"""Módulo principal do projeto."""

from src.common.logger import LoggingManager
from src.common.utils import ProjectUtils
from src.constants.constants import GlobalConstants


def main() -> None:
    """Função principal que imprime 'Olá mundo!'."""
    # Intancia a classe utilidades do projeto
    project_utils = ProjectUtils()

    # Instancia a classe GlobalConstants para acessar as propriedades
    global_constants = GlobalConstants()

    # Define o diretório de início como o diretório atual
    config_file = global_constants.config_file

    # Instancia e configura a classe de logging
    config_file = project_utils.load_yaml_file(config_file)
    logging_manager = LoggingManager(config_file)
    logger = logging_manager.setup()

    # Define o logger na classe de utilidades do projeto
    project_utils.set_logger(logger)

    # Marca o início do projeto
    project_utils.start_config()

    # Adiciona o gitkeep se o diretório estiver vazio
    project_utils.add_gitkeep_if_empty()

    # Define o tempo de execução do projeto
    project_utils.execution_time()

    # Encontra o diretório raiz do projeto
    project_root = project_utils.find_project_root()
    logger.info(f"Diretório raiz do projeto: {project_root}")

    # Retorna a configuração de logging em um JSON dump sem identação
    logging_dump = logging_manager.dump_config()
    logger.info(f"Configuração do logger: {logging_dump}")

    # Imprime 'Olá mundo!'
    logger.info("Olá mundo!")


if __name__ == "__main__":
    main()
