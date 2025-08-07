import re

# Valida os dados do cliente
def validar_dados_cliente(nome, idade, cpf, email=None):
    if not nome or not isinstance(nome, str):
        raise ValueError("Nome do cliente é obrigatório e deve ser uma string.")

    if not idade or not isinstance(idade, int) or idade <= 0:
        raise ValueError("Idade do cliente é obrigatória e deve ser um número inteiro positivo.")

    if not cpf or not re.match(r'^\d{11}$', cpf):
        raise ValueError("CPF deve conter exatamente 11 dígitos numéricos.")

    if email:
        padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(padrao_email, email):
            raise ValueError("E-mail inválido.")

    return True