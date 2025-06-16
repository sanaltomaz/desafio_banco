import getpass

def validar_senha():
    """Middleware para validar a senha da conta bancária."""
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            senha = kwargs.get('senha', None)
            if not senha:
                senha = getpass.getpass("Digite sua senha: ")
            if senha != self.senha:
                raise ValueError("Senha inválida.")
            return func(self, *args, **kwargs)
        return wrapper
    return decorator
