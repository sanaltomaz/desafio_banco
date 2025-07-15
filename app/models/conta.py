from app.middlewares.validar_senha import validar_senha
from app.services.deposito import depositar
from app.services.saque import sacar
from app.services.transferencia import transferir
from app.validators.conta_validator import validar_dados_conta

# Classe de modelo para Contas Bancárias

class ContaBancaria:
    def __init__(self, numero, agencia, banco, saldo=0.0, limite=0.0, senha="", fatura=0.0):
        validar_dados_conta(numero, agencia, banco, saldo, limite, senha, fatura)  # Valida os dados da conta
        # Inicializa os atributos da conta bancária
        self.numero = numero
        self.agencia = agencia
        self.banco = banco
        self.saldo = saldo
        self.limite = limite
        self.senha = senha
        self.fatura = fatura

    def __str__(self):
        return f"Conta {self.numero} - Agência {self.agencia} - Banco {self.banco}- Saldo: R${self.saldo:.2f} - Limite: R${self.limite:.2f} - Fatura: R${self.fatura:.2f}"

    @validar_senha()  # Decorador para validar a senha antes de realizar operações
    def depositar(self, valor_deposito, senha="", usar_limite_flag=True):
        return depositar(self, valor_deposito, usar_limite_flag)  # Chama o serviço de depósito

    @validar_senha()  # Decorador para validar a senha antes de realizar operações
    def sacar(self, valor_saque, senha=""):
        return sacar(self, valor_saque)  # Chama o serviço de saque

    @validar_senha()  # Decorador para validar a senha antes de realizar operações
    def transferir(self, valor_transferencia, conta_destino, senha=""):
        return transferir(self, valor_transferencia, conta_destino)