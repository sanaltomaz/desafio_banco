# Utility functions for the application
import os

def clear_console():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def transformar_valor(valor):
    """Transforma uma string de valor monetário para float."""
    if isinstance(valor, str):
        try:
            return float(valor)
        except (ValueError, TypeError):
            raise ValueError("O valor deve ser um número válido.")
    return valor