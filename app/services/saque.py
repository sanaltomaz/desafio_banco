from app.middlewares.transacoes import autentificar
from app.core.utils import clear_console

def sacar(conta, valor_saque):
    """ Serviço para realizar saque em uma conta bancária. """
    if valor_saque <= 0 or not isinstance(valor_saque, (int, float)):
        raise ValueError("O valor do saque é inválido, verifique o valor informado.")

    autentificar(conta, valor_saque, "saque", usar_limite=True)

    print(f"Saque de R${valor_saque:.2f} realizado com sucesso na conta {conta.numero}.")
    input("Pressione Enter para continuar...")
    clear_console()

    return conta.saldo