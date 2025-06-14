def usar_limite(self, valor, operacao, usar_limite=False):
    """
    Atualiza saldo, limite e fatura conforme a operação bancária.

    Args:
        valor (float): Valor da operação.
        operacao (str): Tipo da operação: 'saque', 'deposito' ou 'transferencia'.
        usar_limite (bool): Se True, permite usar o limite em operações de débito.

    Returns:
        dict: {'sucesso': bool, 'saldo': float, 'limite': float, 'fatura': float, 'mensagem': str}

    Raises:
        ValueError: Se o valor for inválido ou não houver saldo/limite suficiente.
    """
    # Valida se o valor é positivo e do tipo correto
    if valor <= 0 or not isinstance(valor, (float, int)):
        raise ValueError("O valor é inválido, verifique o valor informado.")

    # Operação de depósito: adiciona valor ao saldo
    if operacao == 'deposito':
        self.saldo += valor  # Atualiza saldo com o valor depositado
        return {
            'sucesso': True,
            'saldo': self.saldo,
            'limite': self.limite,
            'fatura': self.fatura,
            'mensagem': 'Depósito realizado com sucesso.'
        }

    # Operações de saque ou transferência
    elif operacao in ['saque', 'transferencia']:
        if valor <= self.saldo:
            # Se há saldo suficiente, debita do saldo normalmente
            self.saldo -= valor
            return {
                'sucesso': True,
                'saldo': self.saldo,
                'limite': self.limite,
                'fatura': self.fatura,
                'mensagem': f'{operacao.capitalize()} realizado com sucesso.'
            }
        elif usar_limite:
            # Se não há saldo suficiente, verifica se pode usar o limite
            valor_restante = valor - self.saldo  # Calcula quanto falta para completar a operação
            if valor_restante <= self.limite:
                # Se o limite cobre o valor restante, atualiza fatura e limite
                self.fatura += valor_restante
                self.limite -= valor_restante
                self.saldo = 0.0  # Zera o saldo, pois foi totalmente utilizado
                return {
                    'sucesso': True,
                    'saldo': self.saldo,
                    'limite': self.limite,
                    'fatura': self.fatura,
                    'mensagem': f'{operacao.capitalize()} realizado com sucesso usando o limite.'
                }
            else:
                # Nem saldo nem limite são suficientes
                raise ValueError("Saldo e limite insuficientes para realizar a operação, verifique o valor informado.")
        else:
            # Não autorizado a usar o limite e saldo insuficiente
            raise ValueError("Saldo insuficiente para realizar a operação e uso do limite não autorizado.")
    else:
        # Operação não reconhecida
        raise ValueError("Operação inválida. Use 'saque', 'deposito' ou 'transferencia'.")
    