import uuid
from app.validators.clinte_validator import validar_dados_cliente

class Cliente:
    def __init__(self, nome, idade, cpf, email=None, telefone=None, id_cliente=None):
        validar_dados_cliente(nome, idade, cpf, email, telefone)  # Valida os dados do cliente
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
        self.telefone = telefone

    def __repr__(self):
        return (f"nome='{self.nome}', "
                f"idade={self.idade}, cpf='{self.cpf}', email='{self.email}', telefone='{self.telefone}')")
