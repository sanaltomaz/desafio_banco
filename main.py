from app.models.conta import ContaBancaria

def main():
    conta = ContaBancaria(numero="12345", agencia="001", banco="Banco A", saldo=1000.0, senha="1234")
    print(conta)

if __name__ == "__main__":
    main()