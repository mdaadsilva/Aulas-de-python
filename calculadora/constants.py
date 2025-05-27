"""Constantes utilizadas no sistema"""

# Limites de IMC
IMC_BAIXO_PESO = 18.5
IMC_NORMAL = 24.9
IMC_SOBREPESO = 29.9
IMC_OBESIDADE_1 = 34.9
IMC_OBESIDADE_2 = 39.9

# Limites de Percentual de Gordura
GORDURA_HOMEM_SAUDAVEL_MIN = 8
GORDURA_HOMEM_SAUDAVEL_MAX = 19
GORDURA_HOMEM_SOBREPESO = 25

GORDURA_MULHER_SAUDAVEL_MIN = 21
GORDURA_MULHER_SAUDAVEL_MAX = 33
GORDURA_MULHER_SOBREPESO = 39

# Limites de RCQ (Relação Cintura-Quadril)
RCQ_RISCO_HOMEM = 0.90
RCQ_RISCO_MULHER = 0.85

# Limites de RCA (Relação Cintura-Altura)
RCA_BAIXO_RISCO = 0.4
RCA_RISCO_NORMAL = 0.5
RCA_RISCO_AUMENTADO = 0.6

# Limites de Índice de Conicidade
IC_RISCO_HOMEM = 1.25
IC_RISCO_MULHER = 1.18

# Limites de Circunferência do Pescoço
CP_RISCO_HOMEM = 39
CP_RISCO_MULHER = 35

# Idade mínima para classificações de adulto
IDADE_MINIMA_ADULTO = 18

# Configurações de Arquivos
DIRETORIO_DADOS = "dados_pacientes"

# Fórmulas de Peso Ideal
FORMULAS_PESO_IDEAL = {
    "devine": {
        "nome": "Devine (1974)",
        "masculino": {"base": 50, "fator": 2.3},
        "feminino": {"base": 45.5, "fator": 2.3}
    },
    "robinson": {
        "nome": "Robinson (1983)",
        "masculino": {"base": 52, "fator": 1.9},
        "feminino": {"base": 49, "fator": 1.7}
    },
    "miller": {
        "nome": "Miller (1983)",
        "masculino": {"base": 56.2, "fator": 1.41},
        "feminino": {"base": 53.1, "fator": 1.36}
    }
} 