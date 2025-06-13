from models.Conta_Bancaria import ContaBancaria

conta1 = ContaBancaria(numero="12345", agencia="001", saldo=1000.0, senha="1234")
conta2 = ContaBancaria(numero="67890", agencia="002", saldo=500.0, senha="5678")

# Tentativa de saque
# conta1.sacar(200, senha="1234")  # Saque autorizado
# conta1.sacar(100)  # Solicitará a senha no terminal

# Transferência
conta1.transferir(300, conta_destino=conta2, senha="1234")  # Transferência autorizada

