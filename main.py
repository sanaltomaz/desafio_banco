from app.models.conta import ContaBancaria

def main():
    print("Bem-vindo ao sistema bancário!")
    conta1 = ContaBancaria(numero="12345", agencia="001", banco="Banco A", saldo=1000.0, senha="1234")
    conta2 = ContaBancaria(numero="67890", agencia="002", banco="Banco B", saldo=500.0, senha="5678")

    # Exemplo de operações
    conta1.depositar(200, senha="1234")
    conta1.sacar(300, senha="1234")
    conta1.transferir(400, conta_destino=conta2, senha="1234")

    print(conta1)
    print(conta2)

if __name__ == "__main__":
    main()