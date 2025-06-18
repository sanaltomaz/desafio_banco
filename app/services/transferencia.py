from app.services.deposito import depositar
from app.services.transacoes_validators import validar_transferencia
from app.core.utils import clear_console

def transferir(conta_origem, valor_transferencia, conta_destino, senha=""):
    """ Serviço para realizar transferência entre contas bancárias. """
    if valor_transferencia <= 0 or not isinstance(valor_transferencia, (int, float)):
        raise ValueError("O valor da transferência é inválido, verifique o valor informado.")

    validar_transferencia(conta_origem, valor_transferencia, conta_destino)

    if conta_origem.numero == conta_destino.numero:
        raise ValueError("Não é possível transferir para a mesma conta.")
    
    # Realiza o depósito na conta de destino
    depositar(conta_destino, valor_transferencia)

    print(f"Transferência de R${valor_transferencia:.2f} realizada com sucesso para a conta {conta_destino.numero}.")
    input("Pressione Enter para continuar...")
    clear_console()

    return conta_origem.saldo