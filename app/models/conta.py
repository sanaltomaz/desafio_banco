from middleware.usar_limite import usar_limite
from middleware.validar_senha import validar_senha
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class ContaBancaria:
    def __init__(self, numero, agencia, saldo=0.0, limite=0.0, senha="", fatura = 0.0):
        self.numero = numero
        self.agencia = agencia
        self.saldo = saldo
        self.limite = limite
        self.senha = senha
        self.fatura = fatura

    def __str__ (self):
        return f"Conta {self.numero} - Agência {self.agencia} - Saldo: R${self.saldo:.2f} - Limite: R${self.limite:.2f} - Fatura: R${self.fatura:.2f}"

    @validar_senha()  # Decorador para validar a senha antes de realizar operações
    def depositar(self, valor_deposito, senha="", usar_limite_flag=True):
        """ Função para depositar um valor na conta bancária.
    
        Argumentos:
            valor_deposito (float): O valor a ser depositado.
            usar_limite_flag (bool): Se True, chama usar_limite; se False, apenas adiciona ao saldo.
    
        Retorna o valor do saldo atualizado.
        """
        if valor_deposito <= 0 or not isinstance(valor_deposito, (int, float)):
            raise ValueError("O valor do depósito é inválido. Verifique o valor informado.")

        if usar_limite_flag:
            usar_limite(self, valor_deposito, "depositar")  # Chama a função usar_limite para verificar e realizar o depósito
        else:
            self.saldo += valor_deposito

        print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso na conta {self.numero}.")
        input("Pressione Enter para continuar...")
        clear_console()  # Limpa o console após o depósito

        return self.saldo
    @validar_senha()  # Decorador para validar a senha antes de realizar operações
    def sacar(self, valor_saque, senha=""):
        """ Função para realizar um saque na conta bancária.

        Argumentos:
            valor_saque (float): O valor a ser sacado.

        Retorna o valor do saldo atualizado.
        """

        if valor_saque <= 0 or not isinstance(valor_saque, (int, float)):
            raise ValueError("O valor do saque é inválido, verifique o valor informado.")
        
        usar_limite(self, valor_saque, "sacar")  # Chama a função usar_limite para verificar e realizar o saque
        
        input("Pressione Enter para continuar...")
        clear_console()  # Limpa o console após o saque

        return self.saldo  # Retorna o saldo atualizado após o saque

    @validar_senha()  # Decorador para validar a senha antes de realizar operações
    def transferir(self, valor_transferencia, conta_destino, senha=""):
        """ Função para realizar uma transferência entre contas bancárias.

        Argumentos:
            valor_transferencia (float): O valor a ser transferido.
            conta_destino (ContaBancaria): A conta de destino da transferência.

        Retorna o valor do saldo atualizado da conta de origem.
        """
        if valor_transferencia <= 0 or not isinstance(valor_transferencia, (int, float)):
            raise ValueError("O valor da transferência é inválido, verifique o valor informado.")

        usar_limite(self, valor_transferencia, "transferencia")
        conta_destino.depositar(valor_transferencia, senha=conta_destino.senha, usar_limite_flag=False) # Usar o método depositar da conta de destino sem usar_limite
        print(f"Transferência de R${valor_transferencia:.2f} realizada com sucesso para a conta {conta_destino.numero}.")
        print("Novo saldo:", self.saldo)
        input("Pressione Enter para continuar...")
        clear_console()
        return self.saldo