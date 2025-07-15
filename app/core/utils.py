# Utility functions for the application
import os
import json

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

def ler_dados(caminho):
    """Faz a leitura do caminho dos arquivos."""
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        raise FileNotFoundError("Arquivo não encontrado.")
    except json.JSONDecodeError:
        raise ValueError("Erro ao decodificar o JSON.")
    
def escrever_dados(caminho, dados):
    try:
        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4)
    except (FileNotFoundError, PermissionError) as e:
        raise RuntimeError(f"Erro ao escrever no arquivo: {e}")
    except TypeError:
        raise ValueError("Os dados fornecidos não são serializáveis em JSON.")