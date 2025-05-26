import json
import os
from datetime import datetime

def obter_input_float(mensagem_prompt, min_val=0, max_val=float('inf')):
    while True:
        try:
            valor = float(input(mensagem_prompt))
            if min_val <= valor <= max_val:
                return valor
            else:
                print(f"Valor fora do intervalo permitido ({min_val}-{max_val}). Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def obter_input_data(mensagem_prompt):
    while True:
        data_str = input(mensagem_prompt)
        try:
            datetime.strptime(data_str, "%Y-%m-%d")
            return data_str
        except ValueError:
            print("Formato de data inválido. Use YYYY-MM-DD. Tente novamente.")

def obter_input_escolha(mensagem_prompt, escolhas_validas):
    escolhas_lower = [str(e).lower() for e in escolhas_validas]
    while True:
        escolha = input(mensagem_prompt).strip().lower()
        if escolha in escolhas_lower:
            return escolhas_validas[escolhas_lower.index(escolha)]
        print(f"Escolha inválida. Opções válidas: {', '.join(map(str,escolhas_validas))}. Tente novamente.") 