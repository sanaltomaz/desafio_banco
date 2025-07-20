from app.core.utils import escrever_dados
from app.models.conta import ContaBancaria
from app.core.class_para_obj import conta_para_dict

caminho = "app/data/contas.json"

def registrar_conta(dados=None):
    if dados is not None and isinstance(dados, ContaBancaria):
        numero = dados.numero
        agencia = dados.agencia
        banco = dados.banco
        saldo = dados.saldo
        limite = dados.limite
        senha = dados.senha
        fatura = dados.fatura
    else:
        raise ValueError("Dados da conta não fornecidos.")

    conta = ContaBancaria(
        numero=numero,
        agencia=agencia,
        banco=banco,
        saldo=saldo,
        limite=limite,
        senha=senha,
        fatura=fatura
    )

    dados_conta = conta_para_dict(conta)
    escrever_dados(caminho, dados_conta)
