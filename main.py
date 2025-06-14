import unittest
from app.models.conta import ContaBancaria

class TestContaBancaria(unittest.TestCase):
    def setUp(self):
        self.conta1 = ContaBancaria(numero="12345", agencia="001", banco="Banco A", saldo=1000.0, senha="1")
        self.conta2 = ContaBancaria(numero="67890", agencia="002", banco="Banco B", saldo=500.0, senha="2")

    def test_transferencia_autorizada(self):
        self.conta1.transferir(300, conta_destino=self.conta2, senha="1")
        self.assertEqual(self.conta1.saldo, 700.0)
        self.assertEqual(self.conta2.saldo, 800.0)

    # Adicione outros testes conforme necessário

if __name__ == '__main__':
    unittest.main()
