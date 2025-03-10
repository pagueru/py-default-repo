# Definição de cores ANSI
RESET  = \033[0m
BOLD   = \033[1m
ITALIC = \033[3m
UNDER  = \033[4m
RED    = \033[31m
GREEN  = \033[32m
YELLOW = \033[33m
BLUE   = \033[34m
MAGENTA= \033[35m
CYAN   = \033[36m
WHITE  = \033[37m
GRAY   = \033[90m

# Formatação de mensagens
SUCCESS = $(BOLD)$(GREEN)[✓]$(RESET)
ERROR   = $(BOLD)$(RED)✖$(RESET)
INFO    = $(BOLD)$(BLUE)i$(RESET)
WARN    = $(BOLD)$(YELLOW)!$(RESET)
WAIT    = $(BOLD)$(CYAN)...$(RESET)
TITLE   = $(BOLD)$(BOLD)$(RESET)
LINE    = ..................................................
TAB     = "  "
TITLE   = $(BOLD)

# Definição de variáveis
APP_NAME=py-default-repo
IMAGE=$(APP_NAME):latest
VERSION=0.1.0
EXEC_MODE=run  # Pode ser 'run' ou 'debug'
