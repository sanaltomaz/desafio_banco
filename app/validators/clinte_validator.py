import re

def validar_dados_cliente(nome, cpf, email=None, telefone=None):
    if not nome or not isinstance(nome, str):
        raise ValueError("Nome do cliente é obrigatório e deve ser uma string.")

    if not cpf or not re.match(r'^\d{11}$', cpf):
        raise ValueError("CPF deve conter exatamente 11 dígitos numéricos.")

    if email:
        padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(padrao_email, email):
            raise ValueError("E-mail inválido.")

    if telefone:
        padrao_telefone = r'^\d{10,11}$'
        if not re.match(padrao_telefone, telefone):
            raise ValueError("Telefone deve conter 10 ou 11 dígitos.")

    return True