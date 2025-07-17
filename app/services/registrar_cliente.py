# from app.core.utils import ler_dados
from app.core.utils import escrever_dados
from app.models.cliente import Cliente
from app.core.class_para_obj import cliente_para_dict

caminho = "app/data/clientes.json"

def registrar_cliente(dados=None):
    if dados != None:
        nome = dados.get("nome")
        idade = dados.get("idade")
        cpf = dados.get("cpf")
        email = dados.get("email")
        telefone = dados.get("telefone")
    else:
        cliente = Cliente(
            nome=str(input("Nome: ")),
            idade=int(input("Idade: ")),
            cpf=str(input("CPF: ")),
            email=str(input("Email: ")),
            telefone=str(input("Telefone: "))
        )
        
    cliente = Cliente(nome=nome, idade=idade, cpf=cpf, email=email, telefone=telefone)
    dados = cliente_para_dict(cliente)

    escrever_dados(caminho, dados)