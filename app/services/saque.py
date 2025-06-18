from app.services.transacoes_validators import validar_saque
from app.core.utils import clear_console, transformar_valor

def sacar(conta, valor_saque, senha=""):
    """ Serviço para realizar saque em uma conta bancária. """
    valor_saque = transformar_valor(valor_saque)

    if valor_saque <= 0:
        raise ValueError("Valor mínimo do saque é R$0.01.")

    validar_saque(conta, valor_saque)

    print(f"Saque de R${valor_saque:.2f} realizado com sucesso na conta {conta.numero}.")
    input("Pressione Enter para continuar...")
    clear_console()

    return conta.saldo