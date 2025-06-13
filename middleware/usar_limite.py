def usar_limite (self, valor_saque):
    if valor_saque <= self.saldo:
            self.saldo -= valor_saque # O saldo é reduzido pelo valor do saque
            print(f"Saque de R${valor_saque:.2f} realizado com sucesso na conta {self.numero}.") 
            print("Saldo atual:", self.saldo)
            return self.saldo
    else:
        print("Saldo insuficiente para realizar o saque. Deseja usar seu limite?")
        print("Saldo atual:", self.saldo)
        print("Limite disponível:", self.limite)
        print("Fatura atual:", self.fatura)
        print("1. Sim")
        print("2. Não")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            valor_restante = valor_saque - self.saldo
            if valor_restante <= self.limite:
                self.fatura += valor_restante # O valor restante é adicionado à fatura
                self.limite -= valor_restante # O limite é consumido
                self.saldo = 0.0 # O saldo se torna zero
                print("Saque realizado com sucesso usando o limite.")
                print("Saldo atual:", self.saldo)
                print("Limite disponível:", self.limite)
                print("Fatura atual:", self.fatura)
                return self.saldo
            else:
                raise ValueError("Saldo e limite insuficientes para realizar o saque, verifique o valor informado.")
        elif escolha == '2':
            raise ValueError("Seu saldo é insuficiente para realizar o saque, verifique o valor informado.")
        else:
            raise ValueError("Opção inválida.")