from app.core.utils import ler_dados
from app.core.utils import escrever_dados
from app.models.cliente import Cliente

caminho = "app/data/clientes.json"

def registar_cliente(dados=None):
    if dados != None:
        nome = dados.get("nome")
        idade = dados.get("idade")
        cpf = dados.get("cpf")
        email = dados.get("email")
        telefone = dados.get("telefone")
    else:
        nome = str(input("Nome: "))
        idade = int(input("Idade: "))
        cpf = str(input("CPF: "))
        email = str(input("Email: "))
        telefone = str(input("Telefone: "))

    cliente = Cliente(nome=nome, idade=idade, cpf=cpf, email=email, telefone=telefone)

    escrever_dados(caminho, cliente)