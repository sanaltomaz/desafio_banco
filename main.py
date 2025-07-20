from app.models.conta import ContaBancaria
from app.services.registrar_cliente import registrar_cliente
from app.services.registrar_conta import registrar_conta

conta = ContaBancaria(
    numero=451256,
    agencia=1001,
    banco=101,
    saldo=1000.0,
    limite=5000.0,
    senha="senha123",
    fatura=200.0
)

registrar_conta(dados=conta)
