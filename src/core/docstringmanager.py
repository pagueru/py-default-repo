"""
Funcionalidade para manipular docstrings em scripts Python de forma programática,
utilizando arquivos YAML como fonte de mapeamento. 

#### Funcionalidades:
- Adiciona docstrings a funções e classes com base em um arquivo YAML.
- Remove docstrings específicas ou todas as docstrings de um script.
- Preserva o formato original do código, usando `RedBaron` para manipulação segura da AST.
- Registra ações de adição ou remoção via logs.
"""

from pathlib import Path
from typing import Callable, Dict, NewType, Optional, Union

import yaml
from redbaron import RedBaron

from core.logger import logger

DocMap = NewType("DocMap", Dict[str, Dict[str, str]])
"""Tipagem para o mapeamento de docstrings: Dict[str, Dict[str, str]]

É um alias para dicionários aninhados com strings como chaves e valores.
"""


def log_action(action: str, name: str, node_type: str) -> None:
    """
    Loga uma ação realizada em um nó (função ou classe).

    Args:
        action (str): Ação realizada, como 'Adicionada' ou 'Removida'.
        name (str): Nome do nó (função ou classe).
        node_type (str): Tipo do nó ('def' ou 'class').
    """
    logger.info(f'{action} docstring para {node_type} "{name}"')


def remove_docstrings(
    script_path: Union[str, Path],
    yaml_path: Union[str, Path, None] = None,
    target_names: Optional[list | str] = None,
) -> None:
    """
    Remove docstrings do script Python com base em um arquivo YAML ou em uma lista/nome
    de funções/classes.

    Args:
        script_path (str): O caminho do script Python.
        yaml_path (str, optional): O caminho do arquivo YAML contendo as docstrings a
            serem removidas. Se fornecido, utiliza o mapeamento YAML.
        target_names (list | str, optional): Lista ou nome único de funções/classes
            cujas docstrings devem ser removidas. Ignorado se o `yaml_path` for
            fornecido. Se ambos `yaml_path` e `target_names` forem `None`, remove
            todas as docstrings.
    """
    # Carrega docstrings do arquivo YAML, se fornecido
    doc_map: Optional[DocMap] = None
    if yaml_path:
        with open(yaml_path, "r", encoding="utf-8") as f:
            doc_map = yaml.safe_load(f)

    # Converte `target_names` para lista, caso seja uma string única
    target_names = [target_names] if isinstance(target_names, str) else target_names

    # Lê o script Python usando RedBaron para manipular a AST
    with open(script_path, "r", encoding="utf-8") as f:
        code = RedBaron(f.read())

    def remove_action(name: str, node: RedBaron, docstring: Optional[str]) -> None:
        """
        Define a ação de remoção de docstrings em nós de função ou classe.

        Args:
            name (str): Nome do nó (função ou classe).
            node (RedBaron): Representação do nó no AST.
            docstring (Optional[str]): Docstring associada ao nó, se aplicável.
        """
        # Determina se a docstring deve ser removida com base nos critérios fornecidos
        should_remove = (
            doc_map is None and (target_names is None or name in target_names)
        ) or (doc_map is not None and docstring is not None)
        if should_remove and node.value and node.value[0].type == "string":
            del node.value[0]  # Remove a primeira string (docstring)
            log_action("Removida", name, node.type)

    # Processa docstrings com base no mapeamento YAML ou na lista de alvos
    process_docstrings(code, doc_map, remove_action)

    # Salva o script atualizado no mesmo arquivo
    with open(script_path, "w", encoding="utf-8") as f:
        f.write(code.dumps())


def process_docstrings(
    code: RedBaron,
    doc_map: Optional[DocMap],
    action: Callable[[str, RedBaron, Optional[str]], None],
) -> None:
    """
    Processa os docstrings em funções ou classes de acordo com uma ação fornecida.

    Args:
        code (RedBaron): Representação do código a ser manipulado.
        doc_map (Optional[DocMap]): Mapeamento de docstrings.
        action (Callable): Função que realiza a ação (adicionar ou remover).
    """
    # Itera por tipos de nós: funções ('def') e classes ('class')
    for node_type, key in [("def", "functions"), ("class", "classes")]:
        # Encontra todos os nós do tipo especificado no AST
        for node in code.find_all(node_type):
            name = node.name  # Nome do nó (função ou classe)
            docstring = doc_map.get(key, {}).get(name) if doc_map else None
            action(name, node, docstring)  # Executa a ação para o nó


def add_docstrings_from_yaml(
    script_path: Union[str, Path], yaml_path: Union[str, Path]
) -> None:
    """
    Adiciona docstrings ao script Python com base no mapeamento definido em um arquivo YAML.
    Remove previamente quaisquer docstrings existentes antes de adicionar as novas.

    Args:
        script_path (str): O caminho do script Python.
        yaml_path (str): O caminho do arquivo YAML contendo as docstrings.
    """
    # Remove as docstrings existentes para evitar duplicação
    remove_docstrings(script_path, yaml_path)

    # Carrega docstrings do arquivo YAML
    with open(yaml_path, "r", encoding="utf-8") as f:
        doc_map: DocMap = yaml.safe_load(f)

    # Lê o script Python usando RedBaron para manipulação
    with open(script_path, "r", encoding="utf-8") as f:
        code = RedBaron(f.read())

    def add_action(name: str, node: RedBaron, docstring: Optional[str]) -> None:
        """
        Define a ação de adição de docstrings em nós de função ou classe.

        Args:
            name (str): Nome do nó (função ou classe).
            node (RedBaron): Representação do nó no AST.
            docstring (Optional[str]): Docstring a ser adicionada.
        """
        if docstring:
            # Calcula a indentação do nó atual para alinhar a docstring
            indentation = node.indentation if node.indentation else ""

            # Formata a nova docstring com a indentação correta
            formatted_docstring = (
                f'{indentation}"""\n{docstring.strip()}\n{indentation}"""'
            )

            # Insere a docstring formatada como o primeiro elemento do nó
            node.value.insert(0, formatted_docstring)
            log_action("Adicionada", name, node.type)

    # Processa docstrings para adicioná-las ao código
    process_docstrings(code, doc_map, add_action)

    # Salva o script atualizado no mesmo arquivo
    with open(script_path, "w", encoding="utf-8") as f:
        f.write(code.dumps())
