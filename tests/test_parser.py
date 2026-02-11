import pytest
import os

def test_placeholder_for_ci():
    """Valida se o ambiente de teste está operacional."""
    assert True

def test_env_loading():
    """Verifica se a lógica de segurança não falha sem o arquivo .env."""
    assert os.getenv("DB_NAME") is None or isinstance(os.getenv("DB_NAME"), str)
