import pytest
from app.services.registrar_cliente import registar_cliente
from app.core.utils import ler_dados
from app.models.cliente import Cliente

@pytest.fixture(autouse=True)
def limpar_clientes(monkeypatch):
    # Limpa o arquivo antes de cada teste
    def fake_escrever_dados(caminho, cliente):
        if not hasattr(fake_escrever_dados, "clientes"):
            fake_escrever_dados.clientes = []
        fake_escrever_dados.clientes.append(cliente)
    monkeypatch.setattr("app.services.registrar_cliente.escrever_dados", fake_escrever_dados)
    yield
    fake_escrever_dados.clientes = []

def test_registrar_cliente_com_dados(monkeypatch):
    clientes_registrados = []

    def fake_escrever_dados(caminho, cliente):
        clientes_registrados.append(cliente)

    monkeypatch.setattr("app.services.registrar_cliente.escrever_dados", fake_escrever_dados)

    dados = {
        "nome": "João Silva",
        "idade": 30,
        "cpf": "12345678900",
        "email": "joao@email.com",
        "telefone": "11999999999"
    }
    registar_cliente(dados)
    assert len(clientes_registrados) == 1
    cliente = clientes_registrados[0]
    assert cliente.nome == "João Silva"
    assert cliente.idade == 30
    assert cliente.cpf == "12345678900"
    assert cliente.email == "joao@email.com"
    assert cliente.telefone == "11999999999"

def test_registrar_varios_clientes(monkeypatch):
    clientes_registrados = []

    def fake_escrever_dados(caminho, cliente):
        clientes_registrados.append(cliente)

    monkeypatch.setattr("app.services.registrar_cliente.escrever_dados", fake_escrever_dados)

    dados_lista = [
        {"nome": "Maria", "idade": 25, "cpf": "11111111111", "email": "maria@email.com", "telefone": "11988888888"},
        {"nome": "Carlos", "idade": 40, "cpf": "22222222222", "email": "carlos@email.com", "telefone": "11977777777"},
    ]
    for dados in dados_lista:
        registar_cliente(dados)
    assert len(clientes_registrados) == 2
    assert clientes_registrados[0].nome == "Maria"
    assert clientes_registrados[1].nome == "Carlos"
