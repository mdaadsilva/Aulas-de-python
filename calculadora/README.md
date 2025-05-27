# Calculadora Antropométrica

Uma calculadora avançada para avaliação antropométrica, desenvolvida em Python.

## Funcionalidades

- Cálculo de IMC (Índice de Massa Corporal)
- Percentual de Gordura (Método Deurenberg)
- Relação Cintura-Quadril (RCQ)
- Relação Cintura-Altura (RCA)
- Índice de Conicidade
- Área Muscular do Braço
- Peso Ideal (Fórmulas: Devine, Robinson e Miller)
- Análise de Circunferência do Pescoço

## Como Usar

1. Instale o Python 3.6 ou superior
2. Execute o programa:
```bash
python -m calculadora
```

## Estrutura do Projeto

```
calculadora/
├── __init__.py         # Inicialização do pacote
├── __main__.py         # Ponto de entrada
├── models.py           # Classes principais (Paciente, Calculadora)
├── interface.py        # Interface com usuário
├── storage.py          # Funções de armazenamento
├── utils.py            # Funções utilitárias
└── constants.py        # Constantes do sistema
```

## Armazenamento de Dados

Os dados dos pacientes são salvos em formato JSON no diretório `dados_pacientes/`.

## Referências

- IMC: Organização Mundial da Saúde (OMS)
- Percentual de Gordura: Deurenberg et al. (1991)
- Peso Ideal: Fórmulas de Devine (1974), Robinson (1983) e Miller (1983)

## Limitações

- Classificações para crianças (<19 anos) requerem Z-scores (não implementados)
- Algumas classificações são gerais e podem necessitar contextualização
- Tabelas de referência específicas por idade/sexo não implementadas 