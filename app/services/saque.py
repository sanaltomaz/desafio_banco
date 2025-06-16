from app.services.transacoes import validar_transacoes
from app.core.utils import clear_console

def sacar(conta, valor_saque, usar_limite_flag=True):
    """ Serviço para realizar saque em uma conta bancária. """
    if valor_saque <= 0 or not isinstance(valor_saque, (int, float)):
        raise ValueError("O valor do saque é inválido, verifique o valor informado.")

    validar_transacoes(conta, valor_saque, "saque", usar_limite_flag)

    print(f"Saque de R${valor_saque:.2f} realizado com sucesso na conta {conta.numero}.")
    input("Pressione Enter para continuar...")
    clear_console()

    return conta.saldo