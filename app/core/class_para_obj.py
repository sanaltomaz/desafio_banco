from app.models import cliente

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
    return cliente.Cliente(
        nome=dados.get("nome"),
        idade=dados.get("idade"),
        cpf=dados.get("cpf"),
        email=dados.get("email"),
        telefone=dados.get("telefone")
    )
