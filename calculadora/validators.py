"""Funções de validação de dados"""
from datetime import datetime
from typing import List, Union, Dict, Any

def validar_medidas_antropometricas(medidas: Dict[str, float]) -> List[str]:
    """
    Valida as medidas antropométricas.
    
    Args:
        medidas: Dicionário com as medidas a serem validadas
        
    Returns:
        Lista de mensagens de erro. Lista vazia se não houver erros.
    """
    erros = []
    
    # Validação de peso
    if medidas.get('peso_kg', 0) <= 0:
        erros.append("Peso deve ser maior que zero")
    elif medidas.get('peso_kg', 0) > 500:
        erros.append("Peso não pode ser maior que 500 kg")
        
    # Validação de estatura
    if medidas.get('estatura_m', 0) <= 0:
        erros.append("Estatura deve ser maior que zero")
    elif medidas.get('estatura_m', 0) > 3:
        erros.append("Estatura não pode ser maior que 3 metros")
        
    # Validação de circunferências
    for nome, valor in medidas.items():
        if 'circ_' in nome and (valor < 0 or valor > 300):
            erros.append(f"{nome.replace('_', ' ').title()} deve estar entre 0 e 300 cm")
            
    return erros

def validar_data(data_str: str) -> Union[datetime, None]:
    """
    Valida e converte uma string de data.
    
    Args:
        data_str: Data no formato YYYY-MM-DD
        
    Returns:
        Objeto datetime se válido, None caso contrário
    """
    try:
        return datetime.strptime(data_str, "%Y-%m-%d")
    except ValueError:
        return None

def validar_formula_peso_ideal(formula: str) -> bool:
    """
    Valida se a fórmula de peso ideal é suportada.
    
    Args:
        formula: Nome da fórmula
        
    Returns:
        True se a fórmula é válida, False caso contrário
    """
    return formula.lower() in ['devine', 'robinson', 'miller']

def validar_sexo(sexo: str) -> bool:
    """
    Valida o sexo informado.
    
    Args:
        sexo: Sexo informado
        
    Returns:
        True se válido, False caso contrário
    """
    return sexo.lower() in ['masculino', 'feminino'] 