from app.models.conta import ContaBancaria

# Criando contas para teste
conta1 = ContaBancaria(numero="12345", agencia="001", banco="Banco A", saldo=1000.0, limite=500.0, senha="1234")
conta2 = ContaBancaria(numero="67890", agencia="002", banco="Banco B", saldo=500.0, limite=300.0, senha="5678")

# Testando depósito
conta1.depositar(200, senha="1234")
print(conta1)  # Deve mostrar saldo atualizado

# Testando saque
conta1.sacar(300, senha="1234")
print(conta1)  # Deve mostrar saldo atualizado

# Testando transferência
conta1.transferir(400, conta_destino=conta2, senha="1234")
print(conta1)  # Deve mostrar saldo atualizado
print(conta2)  # Deve mostrar saldo atualizado