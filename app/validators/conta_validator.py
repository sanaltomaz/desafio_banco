# from app.models.cliente import Cliente

# Valida os dados da conta bancária
def validar_dados_conta(numero, agencia, banco, saldo, limite, senha, fatura):
    if not isinstance(numero, int):
        raise ValueError("Número da conta deve ser um inteiro.")

    if not isinstance(agencia, int):
        raise ValueError("Número da agência deve ser um inteiro.")

    if not isinstance(banco, int):
        raise ValueError("Número do banco deve ser um inteiro.")

    if not isinstance(saldo, (int, float)) or saldo < 0:
        raise ValueError("Saldo deve ser um número positivo ou zero.")
    
    if not isinstance(limite, (int, float)) or limite < 0:
        raise ValueError("Limite deve ser um número positivo ou zero.")
    
    if not isinstance(senha, str) or len(senha) < 4:
        raise ValueError("Senha deve ter ao menos 4 caracteres.")
    
    if not isinstance(fatura, (int, float)) or fatura < 0:
        raise ValueError("Fatura deve ser um número positivo ou zero.")

    # Validação do titular (deve ser uma instância da classe Cliente)
    # if not isinstance(titular, Cliente):
        # raise ValueError("Titular deve ser uma instância da classe Cliente.")

    # Validação do id_cliente (deve ser igual ao id do titular)
    # if not hasattr(titular, 'id') or titular.id != id_cliente:
        # raise ValueError("id_cliente deve corresponder ao id do titular.")
