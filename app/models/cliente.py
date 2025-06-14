class Cliente:
    def __init__(self, id_cliente, nome, cpf, email, telefone):
        self.id_cliente = id_cliente
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone

    def __repr__(self):
        return f"Cliente(id_cliente={self.id_cliente}, nome='{self.nome}', email='{self.email}', telefone='{self.telefone}')"