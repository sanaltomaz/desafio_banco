from app.services.transacoes_validators import validar_deposito
from app.core.utils import clear_console, transformar_valor

def depositar(conta, valor_deposito, senha=""):
    """ Serviço para realizar depósito em uma conta bancária. """
    # Se o valor do depósito for não númerico, transforma para float
    valor_deposito = transformar_valor(valor_deposito)

    if valor_deposito <= 0:
        raise ValueError("Valor mínimo do depósito é R$0.01.")

    validar_deposito(conta, valor_deposito)

    print(f"Depósito de {(valor_deposito)} realizado com sucesso na conta {conta.numero}.")
    input("Pressione Enter para continuar...")
    clear_console()

    return conta.saldo