# py-clean-arch

Este documento é uma réplica traduzida do README.md do repositório [py-clean-arch](https://github.com/cdddg/py-clean-arch). O intuito é ter ele como referência para entendimento futuro.

## Descrição

A Clean Architecture, popularizada por [Uncle Bob](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html), enfatiza vários princípios fundamentais:

1. **Independência de Frameworks**: O sistema não depende de bibliotecas ou frameworks externos.
2. **Testabilidade**: As regras de negócio podem ser validadas sem dependências externas.
3. **Independência da UI**: A interface do usuário pode ser substituída sem afetar o sistema subjacente.
4. **Independência de Banco de Dados**: A lógica de negócio do sistema não está vinculada a um banco de dados específico.
5. **Independência de Agências Externas**: A lógica de negócio não é afetada por integrações externas.

![clean-arch-01](./docs/images/clean-arch-01.png)
*Fonte: [yoan-thirion.gitbook.io](https://yoan-thirion.gitbook.io/knowledge-base/software-craftsmanship/code-katas/clean-architecture)*

### ✨ Recursos Adicionais e Padrões Neste Projeto

Além de seguir os princípios da Clean Architecture de Uncle Bob, este projeto incorpora adaptações modernas e funcionalidades extras para atender às necessidades contemporâneas de desenvolvimento:

- **GraphQL vs HTTP**:<br>O módulo `entrypoints` contém duas interfaces de API. `graphql` fornece uma API robusta baseada em GraphQL, enquanto `http` foca em rotas e controles RESTful.
- **Banco de Dados Relacional vs NoSQL**:<br>O módulo `repositories` oferece suporte a bancos relacionais (e.g., SQLite, MySQL, PostgreSQL) e bancos NoSQL, incluindo armazenamento orientado a documentos (e.g., MongoDB, CouchDB) e armazenamento chave-valor (e.g., Redis, Memcached).

Este projeto também incorpora:

- **Padrão Repository**:<br>Abstração que simplifica o desacoplamento entre a camada de modelo e o armazenamento de dados, promovendo flexibilidade e manutenção. [^1]
- **Padrão Unit of Work**:<br>Garante que todas as operações dentro de uma transação sejam concluídas com sucesso ou nenhuma seja concluída. [^2]
- **Padrão de Injeção de Dependência**:<br>Reduz dependências diretas no código, aumentando testabilidade e flexibilidade dos módulos. [^3]
- **SQLAlchemy Assíncrono**:<br>Usa capacidades assíncronas do SQLAlchemy 2.0 para otimizar operações no banco de dados e lidar melhor com multitarefas. [^4]

### 🧱 Visão Geral da Estrutura do Projeto & Mapeamento da Clean Architecture

Com base nos princípios da Clean Architecture de Uncle Bob, a estrutura e os fluxos arquiteturais do projeto seguem esses princípios.

#### Estrutura de Diretórios

Abaixo está a estrutura de diretórios do projeto destacando os principais arquivos e diretórios:

```ini
./
├── ...
├── src/
│   ├── di/                   - Configurações de injeção de dependência.
│   ├── entrypoints/          - Interfaces externas como HTTP & GraphQL.
│   ├── usecases/             - Contém regras de negócio específicas da aplicação.
│   ├── repositories/         - Camada de interação com dados.
│   ├── models/               - Entidades de domínio.
│   ├── common/               - Código compartilhado e utilitários.
│   ├── settings/db/          - Configurações do banco de dados.
│   └── main.py               - Arquivo principal da aplicação.
│
└── tests/                    - Testes unitários e de integração.
```
