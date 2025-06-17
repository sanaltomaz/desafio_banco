from app.services.transacoes import validar_deposito
from app.core.utils import clear_console

def depositar(conta, valor_deposito, senha=""):
    """ Serviço para realizar depósito em uma conta bancária. """
    if valor_deposito <= 0 or not isinstance(valor_deposito, (int, float)):
        raise ValueError("O valor do depósito é inválido. Verifique o valor informado.")

    validar_deposito(conta, valor_deposito)

    print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso na conta {conta.numero}.")
    input("Pressione Enter para continuar...")
    clear_console()

    return conta.saldo