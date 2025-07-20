from app.models.cliente import Cliente
from app.models.conta import ContaBancaria

# Funções para converter entre Cliente e dicionário
def cliente_para_dict(cliente):
    return {
        "nome": cliente.nome,
        "idade": cliente.idade,
        "cpf": cliente.cpf,
        "email": cliente.email,
        "telefone": cliente.telefone
    }

# Funções para converter entre dicionário e Cliente
def dict_para_cliente(dados):
    return Cliente(
        nome=dados.get("nome"),
        idade=dados.get("idade"),
        cpf=dados.get("cpf"),
        email=dados.get("email"),
        telefone=dados.get("telefone")
    )

def conta_para_dict(conta):
    return {
        "numero": conta.numero,
        "agencia": conta.agencia,
        "banco": conta.banco,
        "saldo": conta.saldo,
        "limite": conta.limite,
        "senha": conta.senha,
        "fatura": conta.fatura
    }

def dict_para_conta(dados):
    return ContaBancaria(
        numero=dados.get("numero"),
        agencia=dados.get("agencia"),
        banco=dados.get("banco"),
        saldo=dados.get("saldo"),
        limite=dados.get("limite"),
        senha=dados.get("senha"),
        fatura=dados.get("fatura")
    )