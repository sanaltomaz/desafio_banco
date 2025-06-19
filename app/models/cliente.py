import uuid
from app.validators.clinte_validator import validar_dados_cliente

class Cliente:
    def __init__(self, nome, cpf, email=None, telefone=None, id_cliente=None):
        validar_dados_cliente(nome, cpf, email, telefone)  # Valida os dados do cliente
        # self.id_cliente = id_cliente or str(uuid.uuid4())  # Gera um ID único se não for fornecido
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone

    def __repr__(self):
        return (f"Cliente(id_cliente={self.id_cliente}, nome='{self.nome}', "
                f"cpf='{self.cpf}', email='{self.email}', telefone='{self.telefone}')")
