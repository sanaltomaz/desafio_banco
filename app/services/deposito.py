from app.middlewares.transacoes import validar_transacoes
from app.core.utils import clear_console

def depositar(conta, valor_deposito, usar_limite_flag=True):
    """ Serviço para realizar depósito em uma conta bancária. """
    if valor_deposito <= 0 or not isinstance(valor_deposito, (int, float)):
        raise ValueError("O valor do depósito é inválido. Verifique o valor informado.")

    if usar_limite_flag:
        validar_transacoes(conta, valor_deposito, "deposito", usar_limite=True)
    else:
        conta.saldo += valor_deposito

    print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso na conta {conta.numero}.")
    input("Pressione Enter para continuar...")
    clear_console()

    return conta.saldo