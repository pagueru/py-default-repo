"""
Módulo de definição de exceções personalizadas para o projeto.

Este módulo contém a definição da classe `ProjectError`, que é uma exceção personalizada
para representar erros específicos do projeto.

Classes:
    ProjectError: Exceção personalizada para erros no projeto.
"""


class ProjectError(RuntimeError):
    """Exceção personalizada para erros no projeto."""

    def __init__(self, message: str):
        """
        Inicializa o ProjectError.

        Args:
            message (str): Mensagem que descreve o erro.
        """
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        """
        Representação da exceção como string.

        Returns:
            str: Representação da exceção.
        """
        return f"{self.message}"

    def __repr__(self) -> str:
        """
        Representação mais detalhada da exceção, útil para debugging.

        Returns:
            str: Representação detalhada da exceção.
        """
        return f"ProjectError(message: {self.message})"


# Define o módulo da exceção como o módulo atual
ProjectError.__module__ = __name__
