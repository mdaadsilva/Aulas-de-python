# calculadora_avancada.py
import json
import math
import os
from datetime import datetime, date

# --- Constantes e Configurações ---
DATA_DIR = "dados_pacientes" # Pasta para salvar os arquivos JSON
os.makedirs(DATA_DIR, exist_ok=True)

# --- Classes ---
class Paciente:
    def __init__(self, id_paciente, nome, sexo, data_nascimento_str, data_avaliacao_str,
                 posicao_medicao, edema, peso_kg, estatura_m, dobra_tricipital_mm,
                 circ_pescoco_cm, circ_braco_cm, circ_cintura_cm, circ_quadril_cm,
                 circ_coxa_cm, circ_panturrilha_cm):
        self.id_paciente = id_paciente
        self.nome = nome
        self.sexo = sexo.lower() # "masculino" ou "feminino"
        try:
            self.data_nascimento = datetime.strptime(data_nascimento_str, "%Y-%m-%d").date()
            self.data_avaliacao = datetime.strptime(data_avaliacao_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Formato de data inválido. Use YYYY-MM-DD.")

        self.posicao_medicao = posicao_medicao.lower()
        self.edema = edema.lower() == "sim"
        
        # Validação básica de medidas
        if not all(isinstance(m, (int, float)) and m >= 0 for m in [
            peso_kg, estatura_m, dobra_tricipital_mm, circ_pescoco_cm,
            circ_braco_cm, circ_cintura_cm, circ_quadril_cm, circ_coxa_cm, circ_panturrilha_cm
        ]):
            raise ValueError("Medidas antropométricas devem ser números não negativos.")
        if estatura_m == 0:
            raise ValueError("Estatura não pode ser zero.")

        self.peso_kg = float(peso_kg)
        self.estatura_m = float(estatura_m)
        self.dobra_tricipital_mm = float(dobra_tricipital_mm) # Coletada, mas não usada em todas as fórmulas de %GC implementadas
        self.circ_pescoco_cm = float(circ_pescoco_cm)
        self.circ_braco_cm = float(circ_braco_cm)
        self.circ_cintura_cm = float(circ_cintura_cm)
        self.circ_quadril_cm = float(circ_quadril_cm)
        self.circ_coxa_cm = float(circ_coxa_cm)
        self.circ_panturrilha_cm = float(circ_panturrilha_cm)
        
        self.idade_anos, self.idade_meses, self.idade_dias = self._calcular_idade_detalhada()
        self.idade_decimal = self.idade_anos + (self.idade_meses / 12) + (self.idade_dias / 365.25)


    def _calcular_idade_detalhada(self):
        today = self.data_avaliacao
        born = self.data_nascimento
        
        anos = today.year - born.year
        meses = today.month - born.month
        dias = today.day - born.day

        if dias < 0:
            meses -= 1
            # Encontrar o número de dias no mês anterior à data de avaliação
            # Se o mês for janeiro, o mês anterior é dezembro do ano anterior
            if today.month == 1:
                dias_no_mes_anterior = 31 # Dias em Dezembro
            else:
                # today.replace(day=1) nos dá o primeiro dia do mês atual
                # subtrair um dia nos dá o último dia do mês anterior
                ultimo_dia_mes_anterior = today.replace(day=1) - timedelta(days=1)
                dias_no_mes_anterior = ultimo_dia_mes_anterior.day
            dias += dias_no_mes_anterior
        
        if meses < 0:
            anos -= 1
            meses += 12
            
        return anos, meses, dias

    def to_dict(self):
        return {
            "id_paciente": self.id_paciente,
            "nome": self.nome,
            "sexo": self.sexo,
            "data_nascimento": self.data_nascimento.isoformat(),
            "data_avaliacao": self.data_avaliacao.isoformat(),
            "posicao_medicao": self.posicao_medicao,
            "edema": "sim" if self.edema else "não",
            "peso_kg": self.peso_kg,
            "estatura_m": self.estatura_m,
            "dobra_tricipital_mm": self.dobra_tricipital_mm,
            "circ_pescoco_cm": self.circ_pescoco_cm,
            "circ_braco_cm": self.circ_braco_cm,
            "circ_cintura_cm": self.circ_cintura_cm,
            "circ_quadril_cm": self.circ_quadril_cm,
            "circ_coxa_cm": self.circ_coxa_cm,
            "circ_panturrilha_cm": self.circ_panturrilha_cm,
            "idade_anos": self.idade_anos,
            "idade_meses": self.idade_meses,
            "idade_dias": self.idade_dias,
            "idade_decimal": self.idade_decimal
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id_paciente"], data["nome"], data["sexo"],
            data["data_nascimento"], data["data_avaliacao"],
            data["posicao_medicao"], data["edema"],
            data["peso_kg"], data["estatura_m"], data["dobra_tricipital_mm"],
            data["circ_pescoco_cm"], data["circ_braco_cm"],
            data["circ_cintura_cm"], data["circ_quadril_cm"],
            data["circ_coxa_cm"], data["circ_panturrilha_cm"]
        )

class CalculadoraAntropometrica:
    def __init__(self, paciente: Paciente):
        self.paciente = paciente
        self.resultados = {}

    def calcular_todos(self, formula_peso_ideal="devine"):
        self._calcular_imc()
        self._calcular_percentual_gordura_deurenberg() # Usando Deurenberg como exemplo
        self._calcular_massas() # Depende do %GC
        self._calcular_rcq()
        self._calcular_rca()
        self._calcular_indice_conicidade()
        self._calcular_area_muscular_braco()
        self._calcular_peso_ideal(formula_peso_ideal)
        self._processar_circ_pescoco()
        
        # Adicionar Z-scores e Percentis aqui exigiria lógica complexa e tabelas de referência
        # Exemplo:
        # self.resultados["imc_zscore"] = calcular_zscore_oms(self.paciente.idade_decimal, self.paciente.sexo, "imc", self.resultados["imc_valor"])
        # self.resultados["imc_percentil"] = calcular_percentil_oms(self.resultados["imc_zscore"])
        return self.resultados

    def _calcular_imc(self):
        imc = self.paciente.peso_kg / (self.paciente.estatura_m ** 2)
        self.resultados["imc_valor"] = round(imc, 2)
        self.resultados["imc_class"] = self._classificar_imc_adulto(imc)

    def _classificar_imc_adulto(self, imc):
        # Para crianças e adolescentes, usar Z-score de IMC-para-idade (OMS)
        if self.paciente.idade_anos < 19:
            return "Classificação por Z-score (OMS) recomendada para esta idade"
        if imc < 18.5: return "Baixo peso"
        elif 18.5 <= imc <= 24.9: return "Peso normal (eutrófico)"
        elif 25.0 <= imc <= 29.9: return "Sobrepeso"
        elif 30.0 <= imc <= 34.9: return "Obesidade Grau I"
        elif 35.0 <= imc <= 39.9: return "Obesidade Grau II"
        else: return "Obesidade Grau III"

    def _calcular_percentual_gordura_deurenberg(self):
        # Fórmula de Deurenberg et al. (1991) - não usa dobras cutâneas
        # %GC = (1.20 * IMC) + (0.23 * Idade) - (10.8 * sexo) - 5.4
        # sexo = 1 para masculino, 0 para feminino
        # Válida para idades > 7 anos aproximadamente.
        # Existem variações para crianças.
        if "imc_valor" not in self.resultados:
            self._calcular_imc() # Garante que o IMC foi calculado

        imc = self.resultados["imc_valor"]
        idade = self.paciente.idade_decimal # Idade em anos decimais
        sex_factor = 1 if self.paciente.sexo == "masculino" else 0
        
        # Fórmula específica para crianças de Deurenberg se necessário
        # if idade < 16 (aproximadamente):
        # %GC_crianca = (1.51 * imc) - (0.70 * idade) - (3.6 * sex_factor) + 1.4
        
        # Fórmula geral (principalmente para adultos, mas usada amplamente)
        percentual_gordura = (1.20 * imc) + (0.23 * idade) - (10.8 * sex_factor) - 5.4
        
        self.resultados["percentual_gordura_valor"] = round(percentual_gordura, 2)
        # Classificação de %GC varia muito com idade, sexo, nível de atividade.
        # Exemplo de classificação muito geral (Gallagher et al., 2000, para adultos):
        class_gc = "N/A (Requer tabelas de referência específicas por idade/sexo)"
        if self.paciente.idade_anos >= 18: # Exemplo para adultos
            if self.paciente.sexo == "masculino":
                if 8 <= percentual_gordura <= 19: class_gc = "Saudável"
                elif percentual_gordura > 19 and percentual_gordura <=25: class_gc = "Aceitável / Sobrepeso"
                elif percentual_gordura > 25 : class_gc = "Obeso"
                else: class_gc = "Abaixo do saudável"
            elif self.paciente.sexo == "feminino":
                if 21 <= percentual_gordura <= 33: class_gc = "Saudável"
                elif percentual_gordura > 33 and percentual_gordura <=39: class_gc = "Aceitável / Sobrepeso"
                elif percentual_gordura > 39: class_gc = "Obeso"
                else: class_gc = "Abaixo do saudável"
        self.resultados["percentual_gordura_class"] = class_gc
        self.resultados["percentual_gordura_metodo"] = "Deurenberg (1991)"


    def _calcular_massas(self):
        if "percentual_gordura_valor" not in self.resultados or self.resultados["percentual_gordura_valor"] is None:
            self.resultados["massa_gorda_kg_valor"] = "N/A"
            self.resultados["massa_magra_kg_valor"] = "N/A"
            self.resultados["massa_magra_perc_valor"] = "N/A"
            return

        pg_perc = self.resultados["percentual_gordura_valor"]
        if pg_perc < 0: # Se %GC for negativo (pode acontecer com algumas fórmulas em indivíduos magros)
             self.resultados["massa_gorda_kg_valor"] = 0
             self.resultados["massa_magra_kg_valor"] = self.paciente.peso_kg
             self.resultados["massa_magra_perc_valor"] = 100.0
        else:
            massa_gorda_kg = self.paciente.peso_kg * (pg_perc / 100.0)
            massa_magra_kg = self.paciente.peso_kg - massa_gorda_kg
            massa_magra_perc = (massa_magra_kg / self.paciente.peso_kg) * 100 if self.paciente.peso_kg > 0 else 0

            self.resultados["massa_gorda_kg_valor"] = round(massa_gorda_kg, 2)
            self.resultados["massa_magra_kg_valor"] = round(massa_magra_kg, 2)
            self.resultados["massa_magra_perc_valor"] = round(massa_magra_perc, 2)
        
        # Classificação para massa magra/gorda geralmente é contextual ou baseada em Z-scores
        self.resultados["massa_gorda_kg_class"] = "N/A (Contextual)"
        self.resultados["massa_magra_kg_class"] = "N/A (Contextual)"
        self.resultados["massa_magra_perc_class"] = "N/A (Contextual)"


    def _calcular_rcq(self):
        if self.paciente.circ_quadril_cm <= 0:
            self.resultados["rcq_valor"] = None
            self.resultados["rcq_class"] = "Circ. Quadril inválida"
            return
        rcq = self.paciente.circ_cintura_cm / self.paciente.circ_quadril_cm
        self.resultados["rcq_valor"] = round(rcq, 2)
        self.resultados["rcq_class"] = self._classificar_rcq_adulto(rcq)

    def _classificar_rcq_adulto(self, rcq):
        # OMS: Risco aumentado para doenças metabólicas
        if self.paciente.sexo == "masculino":
            if rcq >= 0.90: return "Risco cardiovascular aumentado"
        elif self.paciente.sexo == "feminino":
            if rcq >= 0.85: return "Risco cardiovascular aumentado"
        return "Risco cardiovascular normal"

    def _calcular_rca(self):
        if self.paciente.estatura_m <= 0:
            self.resultados["rca_valor"] = None
            self.resultados["rca_class"] = "Estatura inválida"
            return
        estatura_cm = self.paciente.estatura_m * 100
        rca = self.paciente.circ_cintura_cm / estatura_cm
        self.resultados["rca_valor"] = round(rca, 2)
        self.resultados["rca_class"] = self._classificar_rca_adulto(rca)

    def _classificar_rca_adulto(self, rca):
        if rca < 0.4: return "Baixo risco / Magreza" # Variações nos pontos de corte
        elif 0.4 <= rca < 0.5: return "Risco normal / Saudável"
        elif 0.5 <= rca < 0.6: return "Risco aumentado / Sobrepeso"
        else: return "Risco muito aumentado / Obesidade central"

    def _calcular_indice_conicidade(self):
        if self.paciente.estatura_m <= 0 or self.paciente.peso_kg <=0:
            self.resultados["ic_valor"] = None
            self.resultados["ic_class"] = "Peso ou Estatura inválidos"
            return
        circ_cintura_m = self.paciente.circ_cintura_cm / 100.0
        ic_val = circ_cintura_m / (0.109 * math.sqrt(self.paciente.peso_kg / self.paciente.estatura_m))
        self.resultados["ic_valor"] = round(ic_val, 2)
        # Classificação do IC é mais complexa e depende de tabelas de referência por sexo e idade/população.
        # Exemplo de ponto de corte (Valdez et al.): Homens > 1.25, Mulheres > 1.18 (Risco aumentado)
        class_ic = "N/A (Requer dados de referência específicos)"
        if self.paciente.idade_anos >= 18:
            if self.paciente.sexo == "masculino" and ic_val > 1.25: class_ic = "Risco aumentado"
            elif self.paciente.sexo == "feminino" and ic_val > 1.18: class_ic = "Risco aumentado"
            elif (self.paciente.sexo == "masculino" and ic_val <= 1.25) or \
                 (self.paciente.sexo == "feminino" and ic_val <= 1.18): class_ic = "Risco normal"
        self.resultados["ic_class"] = class_ic


    def _calcular_area_muscular_braco(self):
        # AMB (cm²) = [CB (cm) - (π * DCT (cm))]² / 4π
        # DCT = Dobra Cutânea Tricipital
        tsf_cm = self.paciente.dobra_tricipital_mm / 10.0
        amb = ((self.paciente.circ_braco_cm - (math.pi * tsf_cm))**2) / (4 * math.pi)
        self.resultados["amb_valor"] = round(amb, 2)
        # Classificação da AMB requer tabelas de referência (ex: Frisancho)
        self.resultados["amb_class"] = "N/A (Requer tabelas de referência por idade/sexo)"
        # Para CMB (Circunferência Muscular do Braço) = CB - (pi * TSF)
        # Para AMBc (corrigida) subtrai-se um fator (10 para homens, 6.5 para mulheres da AMB) - não implementado aqui

    def _calcular_peso_ideal(self, formula_nome="devine"):
        # Altura em polegadas
        altura_pol = self.paciente.estatura_m * 39.3701
        peso_ideal_kg = None
        formula_usada = ""

        if altura_pol < 58: # Muitas fórmulas são para 5 pés (60 pol) ou mais
            self.resultados["pi_valor"] = None
            self.resultados["pi_class"] = "Altura abaixo do limite comum para estas fórmulas"
            self.resultados["pi_formula"] = "N/A"
            return
        
        polegadas_acima_5pes = altura_pol - 60

        if formula_nome == "devine":
            formula_usada = "Devine (1974)"
            if self.paciente.sexo == "masculino":
                peso_ideal_kg = 50 + (2.3 * polegadas_acima_5pes)
            else: # feminino
                peso_ideal_kg = 45.5 + (2.3 * polegadas_acima_5pes)
        elif formula_nome == "robinson":
            formula_usada = "Robinson (1983)"
            if self.paciente.sexo == "masculino":
                peso_ideal_kg = 52 + (1.9 * polegadas_acima_5pes)
            else: # feminino
                peso_ideal_kg = 49 + (1.7 * polegadas_acima_5pes)
        elif formula_nome == "miller":
            formula_usada = "Miller (1983)"
            if self.paciente.sexo == "masculino":
                peso_ideal_kg = 56.2 + (1.41 * polegadas_acima_5pes)
            else: # feminino
                peso_ideal_kg = 53.1 + (1.36 * polegadas_acima_5pes)
        else:
            self.resultados["pi_valor"] = None
            self.resultados["pi_class"] = "Fórmula de peso ideal desconhecida"
            self.resultados["pi_formula"] = "N/A"
            return

        self.resultados["pi_valor"] = round(peso_ideal_kg, 2) if peso_ideal_kg is not None else None
        # Adequação do Peso = (Peso Atual / Peso Ideal) * 100. Pode ser adicionado.
        self.resultados["pi_class"] = "N/A (Comparar com peso atual para adequação)"
        self.resultados["pi_formula"] = formula_usada
        
    def _processar_circ_pescoco(self):
        cp_cm = self.paciente.circ_pescoco_cm
        self.resultados["cp_valor"] = cp_cm
        # Pontos de corte para risco metabólico (exemplos, podem variar)
        class_cp = "N/A"
        if self.paciente.idade_anos >=18:
            if self.paciente.sexo == "masculino":
                if cp_cm > 39: class_cp = "Risco aumentado (sugestivo de SM)" # Ajuste conforme referência
            elif self.paciente.sexo == "feminino":
                if cp_cm > 35: class_cp = "Risco aumentado (sugestivo de SM)" # Ajuste conforme referência
            else:
                class_cp = "Risco normal"
        self.resultados["cp_class"] = class_cp

# --- Funções Auxiliares (Input/Output, Arquivos) ---
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
            # Retorna a escolha no formato original (para manter capitalização se houver)
            return escolhas_validas[escolhas_lower.index(escolha)]
        print(f"Escolha inválida. Opções válidas: {', '.join(map(str,escolhas_validas))}. Tente novamente.")

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

def exibir_resultados(paciente: Paciente, resultados: dict):
    print("\n\n--- RESULTADOS DA AVALIAÇÃO ANTROPOMÉTRICA ---")
    print(f"Paciente: {paciente.nome} (ID: {paciente.id_paciente})")
    print(f"Data da Avaliação: {paciente.data_avaliacao.strftime('%d/%m/%Y')}")
    print(f"Idade: {paciente.idade_anos} anos, {paciente.idade_meses} meses, {paciente.idade_dias} dias (Decimal: {paciente.idade_decimal:.2f} anos)")
    if paciente.edema:
        print("ATENÇÃO: Presença de edema reportada, pode afetar algumas medidas.")
    print("-" * 70)
    
    tabela = [
        ("IMC (kg/m²)", resultados.get('imc_valor'), resultados.get('imc_class')),
        (f"% Gordura ({resultados.get('percentual_gordura_metodo','N/A')})", resultados.get('percentual_gordura_valor'), resultados.get('percentual_gordura_class')),
        ("Massa Gorda (kg)", resultados.get('massa_gorda_kg_valor'), resultados.get('massa_gorda_kg_class')),
        ("Massa Magra (kg)", resultados.get('massa_magra_kg_valor'), resultados.get('massa_magra_kg_class')),
        ("Massa Magra (%)", resultados.get('massa_magra_perc_valor'), resultados.get('massa_magra_perc_class')),
        ("Relação Cintura-Quadril (RCQ)", resultados.get('rcq_valor'), resultados.get('rcq_class')),
        ("Relação Cintura-Altura (RCA)", resultados.get('rca_valor'), resultados.get('rca_class')),
        ("Índice de Conicidade (IC)", resultados.get('ic_valor'), resultados.get('ic_class')),
        ("Circ. Pescoço (cm)", resultados.get('cp_valor'), resultados.get('cp_class')),
        ("Área Musc. Braço (cm²)", resultados.get('amb_valor'), resultados.get('amb_class')),
        (f"Peso Ideal (kg) [{resultados.get('pi_formula','N/A')}]", resultados.get('pi_valor'), resultados.get('pi_class')),
    ]

    print(f"{'Medida':<35} | {'Valor':<15} | {'Classificação (Geral/Adulto)':<50}")
    print("-" * 105)
    for nome, valor, classificacao in tabela:
        val_str = str(valor) if valor is not None else "N/A"
        class_str = str(classificacao) if classificacao is not None else "N/A"
        print(f"{nome:<35} | {val_str:<15} | {class_str:<50}")
        # Aqui seria o local para adicionar Z-score e Percentil se calculados
        # print(f"{'':<35} | Z-score: {resultados.get(nome.lower().replace(' ','_')+'_zscore','N/A'):<10} | Percentil: {resultados.get(nome.lower().replace(' ','_')+'_perc','N/A'):<10}")
    print("-" * 105)
    
    print("\nNotas Importantes:")
    print("- Z-scores e Percentis NÃO foram calculados (requerem dados de referência complexos).")
    print("- Classificações de % Gordura e outras são gerais e podem necessitar de contextualização.")
    print("- Para indivíduos <19 anos, classificações e avaliações devem seguir padrões de crescimento pediátrico (ex: OMS), não totalmente implementados aqui.")


# --- Fluxo Principal ---
def main():
    print("--- Calculadora Antropométrica Avançada (Python) ---")
    
    acao = obter_input_escolha("Deseja (N)ovo paciente ou (C)arregar existente? ", ["N", "C"])

    if acao == "C":
        id_busca = input("Digite o ID do paciente para carregar: ")
        paciente_obj, resultados_carregados = carregar_paciente(id_busca)
        if paciente_obj and resultados_carregados:
            exibir_resultados(paciente_obj, resultados_carregados)
            # Permitir recalcular ou adicionar nova avaliação no futuro
            print("\nFim da exibição dos dados carregados.")
            return # Finaliza após carregar e exibir
        else:
            print("Iniciando cadastro de novo paciente.")
            # Prossegue para novo cadastro se o carregamento falhar

    print("\n--- Dados do Paciente ---")
    try:
        id_paciente = input("ID do Paciente (ex: 001): ")
        nome_paciente = input("Nome do Paciente: ")
        sexo = obter_input_escolha("Sexo (Masculino/Feminino): ", ["Masculino", "Feminino"])
        data_nasc = obter_input_data("Data de Nascimento (YYYY-MM-DD): ")
        data_aval = obter_input_data("Data da Avaliação (YYYY-MM-DD, deixe em branco para hoje): ")
        if not data_aval: # Se deixado em branco, usa a data de hoje
            data_aval = date.today().strftime("%Y-%m-%d")


        posicao = obter_input_escolha("Posição de Medição (Em pé/Deitado): ", ["Em pé", "Deitado"])
        edema_str = obter_input_escolha("Presença de Edema (Sim/Não): ", ["Sim", "Não"])

        print("\n--- Medidas Antropométricas ---")
        peso = obter_input_float("Peso Corporal (kg): ", 0.1, 500)
        estatura = obter_input_float("Estatura (metros, ex: 1.75): ", 0.1, 3.0)
        dc_tricipital = obter_input_float("Dobra Tricipital (mm): ", 0, 100)
        circ_pescoco = obter_input_float("Circunferência do Pescoço (cm): ", 0, 100)
        circ_braco = obter_input_float("Circunferência do Braço (cm): ", 0, 100)
        circ_cintura = obter_input_float("Circunferência da Cintura (cm): ", 0, 300)
        circ_quadril = obter_input_float("Circunferência do Quadril (cm): ", 0, 300)
        circ_coxa = obter_input_float("Circunferência da Coxa (cm): ", 0, 150)
        circ_panturrilha = obter_input_float("Circunferência da Panturrilha (cm): ", 0, 100)

        paciente_obj = Paciente(
            id_paciente, nome_paciente, sexo, data_nasc, data_aval,
            posicao, edema_str, peso, estatura, dc_tricipital,
            circ_pescoco, circ_braco, circ_cintura, circ_quadril,
            circ_coxa, circ_panturrilha
        )

        formula_pi_escolha = obter_input_escolha(
            "Escolha a fórmula para Peso Ideal (Devine/Robinson/Miller): ",
            ["Devine", "Robinson", "Miller"]
        )

        calculadora = CalculadoraAntropometrica(paciente_obj)
        resultados_finais = calculadora.calcular_todos(formula_peso_ideal=formula_pi_escolha.lower())
        
        exibir_resultados(paciente_obj, resultados_finais)
        
        if obter_input_escolha("\nDeseja salvar os dados deste paciente? (S/N): ", ["S", "N"]) == "S":
            salvar_paciente(paciente_obj, resultados_finais)

    except ValueError as ve:
        print(f"Erro de Valor: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    from datetime import date, timedelta # Adicionado para _calcular_idade_detalhada
    main()