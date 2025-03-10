include config.mk

help: ## Mostra esta ajuda.
	@echo -e "$(BOLD)$(CYAN)$(APP_NAME)$(RESET) ($(GREEN)$(BOLD)$(VERSION)$(RESET))"
	@if [ $(EXEC_MODE) = debug ]; then \
		echo -e "$(INFO) Makefile em modo de execução: $(GREEN)DEBUG$(RESET)"; \
		echo -e ""; \
	else \
		echo -e ""; \
	fi
	@echo -e "$(BOLD)Uso:$(RESET)"
	@echo -e "  make [alvo]"
	@echo -e ""
	@echo -e "$(BOLD)Opções disponíveis:$(RESET)"

	@grep -E '^[a-zA-Z0-9_.-]+:.*## ' $(firstword $(MAKEFILE_LIST)) | \
	sed -e 's/\\$$//' -e 's/##//' | \
	awk -F ': ' '{ printf "  $(CYAN)%-30s$(RESET) %s\n", $$1, $$2 }'

	@echo -e ""
	@echo -e "Para mais informações, veja: $(CYAN)https://github.com/pagueru/py-default-repo$(RESET)"

install: ## Instala as dependências do projeto
	@echo -e "$(INFO) Instalando dependências..."
	@if [ $(EXEC_MODE) = "run" ]; then \
		poetry install; \
	else \
		echo -e "$(INFO) Comando em modo debug: poetry install"; \
	fi

start: ## Inicializa a aplicação em produção
	@echo -e "$(INFO) Iniciando aplicação..."
	@if [ ! -d ".venv" ]; then echo -e "$(WARN) Ambiente virtual não encontrado! Criando..."; poetry install; fi
	@if [ $(EXEC_MODE) = "run" ]; then \
		poetry run python src/main.py; \
	else \
		echo -e "$(INFO) Comando em modo debug: poetry run python src/main.py"; \
		echo -e "$(WARN) Ambiente virtual não encontrado! Criando..."; \
	fi

test: ## Executa todos os testes com pytest
	@echo -e "$(INFO) Executando testes..."
	@if [ -d "tests" ]; then \
		if [ $(EXEC_MODE) = "run" ]; then \
			poetry run pytest; \
		else \
			echo -e "$(INFO) Comando em modo debug: poetry run pytest"; \
		fi \
	else \
		echo -e "$(WARN) Diretório de testes não encontrado"; \
	fi

test.debug: ## Executa os testes e imprime os logs
	@echo -e "$(INFO) Executando testes com logs..."
	@if [ -d "tests" ]; then \
		if [ $(EXEC_MODE) = "run" ]; then \
			poetry run pytest -s; \
		else \
			echo -e "$(INFO) Comando em modo debug: poetry run pytest -s"; \
		fi \
	else \
		echo -e "$(WARN) Diretório de testes não encontrado"; \
	fi

test.cobertura: ## Executa análise de cobertura do projeto
	@echo -e "$(INFO) Executando análise de cobertura..."
	@if [ -d "tests" ]; then \
		if [ $(EXEC_MODE) = "run" ]; then \
			poetry run pytest tests --cov=src; \
		else \
			echo -e "$(INFO) Comando em modo debug: poetry run pytest tests --cov=src"; \
		fi \
	else \
		echo -e "$(WARN) Diretório de testes não encontrado"; \
	fi

test.cobertura.html: ## Executa análise de cobertura e gera relatório em HTML.
	@echo -e "$(INFO) Gerando relatório de cobertura em HTML..."
	@if [ -d "tests" ]; then \
		if [ $(EXEC_MODE) = "run" ]; then \
			poetry run pytest tests --cov=src --cov-report=html; \
		else \
			echo -e "$(INFO) Comando em modo debug: poetry run pytest tests --cov=src --cov-report=html"; \
		fi \
	else \
		echo -e "$(WARN) Diretório de testes não encontrado"; \
	fi

test.lint: ## Verifica a formatação do código
	@echo -e "$(INFO) Verificando formatação do código..."
	@if [ -d "src" ]; then \
		if [ $(EXEC_MODE) = run ]; then \
			poetry run black --check src tests; \
		else \
			echo -e "$(INFO) Comando em modo debug: poetry run black --check src tests"; \
		fi \
	else \
		echo -e "$(WARN) Diretório de código-fonte não encontrado"; \
	fi

clean.venv: ## Remove o ambiente virtual do projeto
	@echo -e "$(INFO) Removendo ambiente virtual..."
	@if [ -d ".venv" ]; then \
		if [ $(EXEC_MODE) = "run" ]; then \
			rm -rf .venv; \
		else \
			echo -e "$(INFO) Comando em modo debug: rm -rf .venv"; \
		fi \
	else \
		echo -e "$(WARN) .venv já removido"; \
	fi

clean.images: ## Remove todas as imagens Docker relacionadas ao projeto
	@echo -e "$(INFO) Removendo imagens Docker..."
	@if [ $(EXEC_MODE) = "run" ]; then \
		docker-compose down; \
		images=$$(docker images --filter=reference="$(APP_NAME)*" -q); \
		if [ -n "$$IMAGES" ]; then \
			docker rmi -f $$IMAGES; \
		else \
			echo -e "$(WARN) Nenhuma imagem para remover"; \
		fi \
	else \
		echo -e "$(INFO) Comando em modo debug: docker-compose down"; \
		echo -e "$(INFO) Comando em modo debug: docker rmi -f \$$IMAGES"; \
	fi
