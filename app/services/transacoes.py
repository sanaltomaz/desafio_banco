def validar_deposito(self, valor_deposito, senha=""):
    """
    Valida e realiza um depósito na conta.
    """
    if not isinstance(valor_deposito, (float, int)) or valor_deposito <= 0:
        raise ValueError("O valor do depósito é inválido, verifique o valor informado.")

    self.saldo += valor_deposito

    return {
        'sucesso': True,
        'saldo': self.saldo,
        'limite': self.limite,
        'fatura': self.fatura
    }

def validar_saque(self, valor_saque, senha="", usar_limite=False):
    """
    Valida e realiza um saque, utilizando o limite se autorizado.
    """
    if not isinstance(valor_saque, (float, int)) or valor_saque <= 0:
        raise ValueError("O valor do saque é inválido, verifique o valor informado.")

    if valor_saque <= self.saldo:
        self.saldo -= valor_saque
        return {
            'sucesso': True,
            'saldo': self.saldo,
            'limite': self.limite,
            'fatura': self.fatura,
        }
    elif usar_limite:
        valor_restante = valor_saque - self.saldo
        if valor_restante <= self.limite:
            self.fatura += valor_restante
            self.limite -= valor_restante
            self.saldo = 0.0
            return {
                'sucesso': True,
                'saldo': self.saldo,
                'limite': self.limite,
                'fatura': self.fatura
            }
        else:
            raise ValueError("Saldo e limite insuficientes para realizar o saque.")
    else:
        raise ValueError("Saldo insuficiente para realizar o saque e uso do limite não autorizado.")

def validar_transferencia(self, valor_transferencia, conta_destino, senha="", usar_limite=False):
    """
    Valida e realiza uma transferência, utilizando o limite se autorizado.
    """
    if not isinstance(valor_transferencia, (float, int)) or valor_transferencia <= 0:
        raise ValueError("O valor da transferência é inválido, verifique o valor informado.")

    if valor_transferencia <= self.saldo:
        self.saldo -= valor_transferencia
        conta_destino.saldo += valor_transferencia
        return {
            'sucesso': True,
            'saldo': self.saldo,
            'limite': self.limite,
            'fatura': self.fatura,
        }
    elif usar_limite:
        valor_restante = valor_transferencia - self.saldo
        if valor_restante <= self.limite:
            self.fatura += valor_restante
            self.limite -= valor_restante
            self.saldo = 0.0
            conta_destino.saldo += valor_transferencia
            return {
                'sucesso': True,
                'saldo': self.saldo,
                'limite': self.limite,
                'fatura': self.fatura,
                'mensagem': 'Transferência realizada com sucesso usando o limite.'
            }
        else:
            raise ValueError("Saldo e limite insuficientes para realizar a transferência.")
    else:
        raise ValueError("Saldo insuficiente para realizar a transferência e uso do limite não autorizado.")

def usar_limite(self, valor, senha="", usar_limite_flag=False):
    """
    Valida e utiliza o limite de crédito da conta.
    """
    if not isinstance(valor, (float, int)) or valor <= 0:
        raise ValueError("O valor é inválido, verifique o valor informado.")

    if valor > self.limite:
        raise ValueError("Valor excede o limite disponível.")

    if not usar_limite_flag:
        raise ValueError("Uso do limite não autorizado.")

    self.fatura += valor
    self.limite -= valor
    self.saldo = 0.0

    return {
        'sucesso': True,
        'saldo': self.saldo,
        'limite': self.limite,
        'fatura': self.fatura,
    }
