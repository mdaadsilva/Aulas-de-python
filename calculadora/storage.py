import json
import os
from .models import Paciente

DATA_DIR = "dados_pacientes"
os.makedirs(DATA_DIR, exist_ok=True)

def salvar_paciente(paciente: Paciente, resultados: dict):
    filename = os.path.join(DATA_DIR, f"paciente_{paciente.id_paciente}.json")
    data_to_save = {
        "paciente_info": paciente.to_dict(),
        "resultados_avaliacao": resultados
    }
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data_to_save, f, indent=4, ensure_ascii=False)
        print(f"\nDados do paciente salvos em: {filename}")
    except IOError as e:
        print(f"Erro ao salvar arquivo: {e}")

def carregar_paciente(id_paciente):
    filename = os.path.join(DATA_DIR, f"paciente_{id_paciente}.json")
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data_loaded = json.load(f)
        paciente = Paciente.from_dict(data_loaded["paciente_info"])
        resultados = data_loaded["resultados_avaliacao"]
        print(f"Dados do paciente {id_paciente} carregados.")
        return paciente, resultados
    except FileNotFoundError:
        print(f"Nenhum dado encontrado para o ID: {id_paciente}")
        return None, None
    except Exception as e:
        print(f"Erro ao carregar arquivo: {e}")
        return None, None 