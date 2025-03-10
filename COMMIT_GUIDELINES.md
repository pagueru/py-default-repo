# Simplificando Commits

Uma versão simplificada do [Conventional Commits](https://www.conventionalcommits.org/) para facilitar o uso constante do Git no dia a dia, mantendo um histórico claro e prático.

## Tipos de Commits

- `init`: indica inicializações importantes no projeto, como a configuração ou organização inicial da estrutura do ambiente.
  - `init: cria a estrutura inicial do projeto`
  - `init: configura ambiente virtual com Poetry`
  - `init: finaliza organização inicial do projeto`

- `feat`: indica adições de novas funcionalidades ao projeto, como novos módulos, processos ou scripts.
  - `feat: adiciona sistema de autenticação`
  - `feat: implementa validação de dados no formulário`
  - `feat: adiciona suporte ao banco de dados SQLite`

- `fix`: indica correções de erros ou bugs encontrados no projeto.
  - `fix: corrige erro ao salvar dados`
  - `fix: corrige estrutura do main.py`
  - `fix: corrige string de conexão com o banco de dados`

- `update`: indica ajustes ou melhorias que não introduzem novas funcionalidades nem corrigem erros.
  - `update: melhora estrutura de logs no projeto`
  - `update: reorganiza módulos para maior clareza`
  - `update: ajusta documentação no README`

## Estrutura do Commit

A estrutura do commit deve seguir o formato abaixo:

```text
<tipo>(<escopo opicional>): <descrição curta>

<corpo opcional>
```

O commit deve ter o tipo da mudança e uma **descrição curta** em modo imperativo (ex.: "adiciona", "corrige"). Opcionalmente, podem ser adicionados o **escopo**, para especificar a área afetada, e o **corpo**, para detalhes adicionais ou informações complementares.

```text
init: configura ambiente inicial do projeto Python

- Cria as pastas principais: src/, tests/, docs/.
- Inclui os arquivos básicos: README.md, .gitignore e pyproject.toml.
- Configura o ambiente virtual
```

## Utilização do Template

Para uma melhor organização do corpo do commit, utilize o arquivo `tools/commit.txt` para estruturá-lo.

```text
git add .
git commit -F tools/commit.txt
git push
```


🚀 init: cria a estrutura inicial do projeto
