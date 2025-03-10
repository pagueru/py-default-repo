# copilot-instructions.md

Projetos em Python devem aderir às Python Enhancement Proposals (PEPs), às Convenções de Nomenclatura e Tipagem do Python e às melhores práticas da linguagem. Além disso, as seguintes convenções específicas devem ser observadas ao sugerir ou gerar código:

* Variáveis, funções, classes e objetos similares devem ser nomeados em inglês.
* Comentários de código e docstrings devem ser nomeados em português do Brasil.
* Os scripts devem possuir tipagem forte utilizando o módulo `typing`.
* Os scripts devem seguir as boas práticas de lint e formatação de código utilizando as ferramentas:
  * `mypy` para verificação de tipagem estática.
  * `pylint` ou `pyright` para análise de qualidade de código.
  * `black` para formatação automática de código.
* Antes de submeter ou aceitar sugestões de código, verifique se ele está conforme essas ferramentas e se as mensagens de erro são resolvidas.
* Os script devem utilizar o módulo `logging` para registrar mensagens do sistema.
* Os scripts devem utilizar o módulo `pathlib` para trabalhar com caminhos de arquivos e diretórios.
* Ao criar docstrings, utilize o estilo de docstrings do Google.
* As mensagens de commit devem seguir o padrão de commits convencionais, utilizando o tipo `init`, `feat`, `fix` ou `update`, conforme as definições a seguir:
  * `init`: indica inicializações importantes no projeto, como a configuração ou organização inicial da estrutura do ambiente.
  * `feat`: indica adições de novas funcionalidades ao projeto, como novos módulos, processos ou scripts.
  * `fix`: indica correções de erros ou bugs encontrados no projeto.
  * `update`: indica ajustes ou melhorias que não introduzem novas funcionalidades nem corrigem erros.
* Todos os comentários devem ser feitos na linguagem imperativa, exemplo: "trata", "corrige", "faz".
