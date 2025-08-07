from app.middlewares.validar_senha import validar_senha
from app.services.deposito import depositar
from app.services.saque import sacar
from app.services.transferencia import transferir
from app.validators.conta_validator import validar_dados_conta

# Classe de modelo para Contas Bancárias
class ContaBancaria:
    def __init__(self, saldo_conta=0.0, limite=0.0, senha_usuario="", fatura=0.0):
        validar_dados_conta(saldo_conta, limite, senha_usuario, fatura)  # Valida os dados da conta
        # Inicializa os atributos da conta bancária
        self.saldo_conta = saldo_conta
        self.limite = limite
        self.senha_usuario = senha_usuario
        self.fatura = fatura

    def __str__(self):
        return f"Conta - Saldo: R${self.saldo_conta:.2f} - Limite: R${self.limite:.2f} - Fatura: R${self.fatura:.2f}"

    @validar_senha()  # Decorador para validar a senha antes de realizar operações
    def depositar(self, valor_deposito, senha="", usar_limite_flag=True):
        return depositar(self, valor_deposito, usar_limite_flag)  # Chama o serviço de depósito

    @validar_senha()  # Decorador para validar a senha antes de realizar operações
    def sacar(self, valor_saque, senha=""):
        return sacar(self, valor_saque)  # Chama o serviço de saque

    @validar_senha()  # Decorador para validar a senha antes de realizar operações
    def transferir(self, valor_transferencia, conta_destino, senha=""):
        return transferir(self, valor_transferencia, conta_destino)