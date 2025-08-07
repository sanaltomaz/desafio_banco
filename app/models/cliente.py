from app.validators.clinte_validator import validar_dados_cliente

# Classe de modelo para Clientes
class Cliente:
    def __init__(self, nome, idade, cpf, email=None, id_cliente=None):
        validar_dados_cliente(nome, idade, cpf, email)  # Valida os dados do cliente
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email

    def __repr__(self):
        return (f"nome='{self.nome}', "
                f"idade={self.idade}, cpf='{self.cpf}', email='{self.email}')")
