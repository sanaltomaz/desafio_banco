from unittest import TestCase
from app.models.conta import ContaBancaria
from unittest.mock import patch
from app.services.saque import sacar

class TestSaque(TestCase):
    def setUp(self):
        self.conta = ContaBancaria(numero="12345", agencia="001", banco="Banco A", saldo=100.0, senha="1234")

    @patch("app.services.saque.validar_saque")
    @patch("app.services.saque.clear_console")
    @patch("builtins.input", return_value="")
    def test_saque_valido(self, mock_input, mock_clear, mock_validar):
        saldo_antes = self.conta.saldo
        valor_saque = 50.0
        novo_saldo = sacar(self.conta, valor_saque, senha="1234")
        self.assertEqual(novo_saldo, saldo_antes)  # saldo não é alterado na função sacar
        mock_validar.assert_called_once_with(self.conta, valor_saque)

    @patch("app.services.saque.validar_saque")
    def test_saque_valor_invalido(self, mock_validar):
        with self.assertRaises(ValueError):
            sacar(self.conta, 0)

    @patch("app.services.saque.validar_saque")
    def test_saque_valor_negativo(self, mock_validar):
        with self.assertRaises(ValueError):
            sacar(self.conta, -10)

    @patch("app.services.saque.clear_console")
    @patch("builtins.input", return_value="")
    def test_saque_chama_validar_saque(self, mock_input, mock_clear):
        with patch("app.services.saque.validar_saque") as mock_validar:
            sacar(self.conta, 10)
            mock_validar.assert_called_once()
