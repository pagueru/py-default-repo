# py-default-repo

> [!IMPORTANT]  
> Este arquivo README.md está em construção. Algumas informações podem estar incompletas ou imprecisas no momento, e serão atualizadas conforme o projeto evolui.

Este repositório foi criado com o propósito de servir como uma base replicável para a inicialização de novos projetos. A estrutura e o conteúdo deste README.md foram amplamente inspirados no repositório [myDefaultDataProject](https://github.com/alanceloth/myDefaultDataProject), que desempenhou um papel fundamental na concepção deste projeto.

Para usar esta estrutura de projeto, você precisará seguir os passos abaixo.

## Requisitos

Para usar este projeto adequadamente, será necessário instalar:

- [python](https://www.python.org/downloads/)
- [git](https://git-scm.com/downloads)
- [pyenv](https://pypi.org/project/pyenv/)
- [poetry](https://python-poetry.org/)

Para instalar e configurar o Pyenv e o Poetry no Windows, confira [este vídeo](https://www.youtube.com/watch?v=547Jr26duHQ).
Para aprender como gerenciar múltiplas versões do Python usando o pyenv, leia [este artigo](https://realpython.com/intro-to-pyenv/).

## Configuração do ambiente local do Poetry

Para criar a pasta local .venv, digite no terminal:

```bash
poetry config virtualenvs.create true
poetry config virtualenvs.in-project true
```

## Instalação

### 1. Clone o repositório

Abra uma janela de terminal com comandos Git e digite:

```bash
git clone https://github.com/pagueru/py-docstring-manager.git [NOVO_NOME_DO_PROJETO]
cd [NOVO_NOME_DO_PROJETO]
```

### 2. Configure o ambiente

O projeto utiliza a versão do Python 3.12.7:

```bash
pyenv update
pyenv install 3.12.7
pyenv local 3.12.7
```

Para inicializar o Poetry no projeto:

```bash
poetry env use 3.12.7
poetry shell
poetry install --no-root
```

## Estrutura de Pastas

A estrutura básica de pastas do projeto é mostrada abaixo:

```bash
.
├── .vscode/
│   ├── launch.json
│   └── settings.json
├── config/
│   └── docstringmanager.yaml
├── data/
├── logs/
│   └── app.log
├── src/
│   ├── core/
│   │   ├── constants.py
│   │   ├── docstringmanager.py
│   │   ├── logger.py
│   │   ├── utils.py
│   │   └── __init__.py
│   └── main.py
├── tools/
│   ├── commit.txt
│   └── template_commit.txt
├── .gitignore
├── .pre-commit-config.yaml
├── .python-version
├── CONTRIBUTING.md
├── NOTES.md
├── poetry.lock
├── pyproject.toml
└── README.md
```

## Contato

GitHub: [pagueru](https://github.com/pagueru/)

LinkedIn: [Raphael Henrique Vieira Coelho](https://www.linkedin.com/in/raphaelhvcoelho/)

E-mail: [raphael.phael@gmail.com](mailto:raphael.phael@gmail.com)
