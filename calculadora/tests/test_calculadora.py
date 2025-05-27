"""Testes unitários para a calculadora antropométrica"""
import unittest
from datetime import date
from ..models import Paciente, CalculadoraAntropometrica
from ..validators import validar_medidas_antropometricas, validar_data, validar_formula_peso_ideal

class TestCalculadoraAntropometrica(unittest.TestCase):
    def setUp(self):
        """Configura os dados para os testes"""
        self.paciente = Paciente(
            id_paciente="001",
            nome="Teste",
            sexo="Masculino",
            data_nascimento_str="1990-01-01",
            data_avaliacao_str=date.today().strftime("%Y-%m-%d"),
            posicao_medicao="Em pé",
            edema="Não",
            peso_kg=70.0,
            estatura_m=1.75,
            dobra_tricipital_mm=15.0,
            circ_pescoco_cm=38.0,
            circ_braco_cm=30.0,
            circ_cintura_cm=80.0,
            circ_quadril_cm=95.0,
            circ_coxa_cm=55.0,
            circ_panturrilha_cm=35.0
        )
        self.calculadora = CalculadoraAntropometrica(self.paciente)

    def test_calculo_imc(self):
        """Testa o cálculo do IMC"""
        self.calculadora._calcular_imc()
        imc_esperado = 70.0 / (1.75 ** 2)
        self.assertAlmostEqual(self.calculadora.resultados["imc_valor"], round(imc_esperado, 2))

    def test_validacao_medidas(self):
        """Testa a validação de medidas antropométricas"""
        medidas = {
            'peso_kg': 70.0,
            'estatura_m': 1.75,
            'circ_pescoco_cm': 38.0
        }
        erros = validar_medidas_antropometricas(medidas)
        self.assertEqual(len(erros), 0)

    def test_validacao_medidas_invalidas(self):
        """Testa a validação de medidas antropométricas inválidas"""
        medidas = {
            'peso_kg': -1,
            'estatura_m': 0,
            'circ_pescoco_cm': 400
        }
        erros = validar_medidas_antropometricas(medidas)
        self.assertTrue(len(erros) > 0)

    def test_validacao_data(self):
        """Testa a validação de datas"""
        self.assertIsNotNone(validar_data("2023-01-01"))
        self.assertIsNone(validar_data("2023-13-01"))

    def test_validacao_formula_peso_ideal(self):
        """Testa a validação de fórmulas de peso ideal"""
        self.assertTrue(validar_formula_peso_ideal("devine"))
        self.assertFalse(validar_formula_peso_ideal("invalida"))

if __name__ == '__main__':
    unittest.main() 