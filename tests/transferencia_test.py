import unittest
from unittest.mock import patch, MagicMock
from app.services.transferencia import transferir

# python -m unittest tests.transferencia_test

class ContaMock:
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo

class TestTransferencia(unittest.TestCase):
    def setUp(self):
        self.conta_origem = ContaMock(numero="123", saldo=1000.0)
        self.conta_destino = ContaMock(numero="456", saldo=500.0)

    @patch("app.services.transferencia.transformar_valor", side_effect=lambda x: float(x))
    @patch("app.services.transferencia.validar_transferencia")
    @patch("app.services.transferencia.depositar")
    @patch("app.services.transferencia.clear_console")
    def test_transferencia_sucesso(self, mock_clear, mock_depositar, mock_validar, mock_transformar):
        valor = 200.0
        with patch("builtins.input", return_value=""):
            saldo = transferir(self.conta_origem, valor, self.conta_destino)
        mock_validar.assert_called_once_with(self.conta_origem, valor, self.conta_destino)
        mock_depositar.assert_called_once_with(self.conta_destino, valor)
        self.assertEqual(saldo, self.conta_origem.saldo)

    @patch("app.services.transferencia.transformar_valor", side_effect=lambda x: float(x))
    def test_transferencia_valor_negativo(self, mock_transformar):
        with self.assertRaisesRegex(ValueError, "Valor mínimo de transferência é R\$0.01."):
            transferir(self.conta_origem, -10, self.conta_destino)

    @patch("app.services.transferencia.transformar_valor", side_effect=lambda x: float(x))
    def test_transferencia_valor_zero(self, mock_transformar):
        with self.assertRaisesRegex(ValueError, "Valor mínimo de transferência é R\$0.01."):
            transferir(self.conta_origem, 0, self.conta_destino)

    @patch("app.services.transferencia.transformar_valor", side_effect=lambda x: float(x))
    @patch("app.services.transferencia.validar_transferencia", side_effect=Exception("Saldo insuficiente"))
    def test_transferencia_validacao_falha(self, mock_validar, mock_transformar):
        with self.assertRaisesRegex(Exception, "Saldo insuficiente"):
            transferir(self.conta_origem, 100, self.conta_destino)

    @patch("app.services.transferencia.transformar_valor", side_effect=lambda x: float(x))
    def test_transferencia_mesma_conta(self, mock_transformar):
        conta = ContaMock(numero="123", saldo=1000.0)
        with self.assertRaisesRegex(ValueError, "Não é possível transferir para a mesma conta."):
            transferir(conta, 100, conta)

if __name__ == "__main__":
    unittest.main()
