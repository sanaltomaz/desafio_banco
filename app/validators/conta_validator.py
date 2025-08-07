# from app.models.cliente import Cliente

# Valida os dados da conta bancária
def validar_dados_conta(saldo_conta, limite, senha_usuario, fatura):
    if not isinstance(saldo_conta, (int, float)) or saldo_conta < 0:
        raise ValueError("Saldo deve ser um número positivo ou zero.")
    
    if not isinstance(limite, (int, float)) or limite < 0:
        raise ValueError("Limite deve ser um número positivo ou zero.")

    if not isinstance(senha_usuario, str) or len(senha_usuario) < 4:
        raise ValueError("Senha deve ter ao menos 4 caracteres.")
    
    if not isinstance(fatura, (int, float)) or fatura < 0:
        raise ValueError("Fatura deve ser um número positivo ou zero.")