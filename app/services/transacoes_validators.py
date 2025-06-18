def validar_deposito(conta, valor_deposito, senha=""):
    if not isinstance(valor_deposito, (float, int)) or valor_deposito <= 0:
        raise ValueError("O valor do depósito é inválido, verifique o valor informado.")

    conta.saldo += valor_deposito

    return {
        'sucesso': True,
        'saldo': conta.saldo,
        'limite': conta.limite,
        'fatura': conta.fatura
    }

def validar_saque(conta, valor_saque, senha="", usar_limite=False):
    if not isinstance(valor_saque, (float, int)) or valor_saque <= 0:
        raise ValueError("O valor do saque é inválido, verifique o valor informado.")

    if valor_saque <= conta.saldo:
        conta.saldo -= valor_saque
        return {
            'sucesso': True,
            'saldo': conta.saldo,
            'limite': conta.limite,
            'fatura': conta.fatura,
        }
    elif usar_limite:
        valor_restante = valor_saque - conta.saldo
        if valor_restante <= conta.limite:
            conta.fatura += valor_restante
            conta.limite -= valor_restante
            conta.saldo = 0.0
            return {
                'sucesso': True,
                'saldo': conta.saldo,
                'limite': conta.limite,
                'fatura': conta.fatura
            }
        else:
            raise ValueError("Saldo e limite insuficientes para realizar o saque.")
    else:
        raise ValueError("Saldo insuficiente para realizar o saque e uso do limite não autorizado.")

def validar_transferencia(conta_origem, valor_transferencia, conta_destino, senha="", usar_limite=False):
    if not isinstance(valor_transferencia, (float, int)) or valor_transferencia <= 0:
        raise ValueError("O valor da transferência é inválido, verifique o valor informado.")

    if valor_transferencia <= conta_origem.saldo:
        conta_origem.saldo -= valor_transferencia
        conta_destino.saldo += valor_transferencia
        return {
            'sucesso': True,
            'saldo': conta_origem.saldo,
            'limite': conta_origem.limite,
            'fatura': conta_origem.fatura,
        }
    elif usar_limite:
        valor_restante = valor_transferencia - conta_origem.saldo
        if valor_restante <= conta_origem.limite:
            conta_origem.fatura += valor_restante
            conta_origem.limite -= valor_restante
            conta_origem.saldo = 0.0
            conta_destino.saldo += valor_transferencia
            return {
                'sucesso': True,
                'saldo': conta_origem.saldo,
                'limite': conta_origem.limite,
                'fatura': conta_origem.fatura,
                'mensagem': 'Transferência realizada com sucesso usando o limite.'
            }
        else:
            raise ValueError("Saldo e limite insuficientes para realizar a transferência.")
    else:
        raise ValueError("Saldo insuficiente para realizar a transferência e uso do limite não autorizado.")

def usar_limite(conta, valor, senha="", usar_limite_flag=False):
    if not isinstance(valor, (float, int)) or valor <= 0:
        raise ValueError("O valor é inválido, verifique o valor informado.")

    if valor > conta.limite:
        raise ValueError("Valor excede o limite disponível.")

    if not usar_limite_flag:
        raise ValueError("Uso do limite não autorizado.")

    conta.fatura += valor
    conta.limite -= valor
    conta.saldo = 0.0

    return {
        'sucesso': True,
        'saldo': conta.saldo,
        'limite': conta.limite,
        'fatura': conta.fatura,
    }
