import math
from datetime import datetime, timedelta

class Paciente:
    def __init__(self, id_paciente, nome, sexo, data_nascimento_str, data_avaliacao_str,
                 posicao_medicao, edema, peso_kg, estatura_m, dobra_tricipital_mm,
                 circ_pescoco_cm, circ_braco_cm, circ_cintura_cm, circ_quadril_cm,
                 circ_coxa_cm, circ_panturrilha_cm):
        self.id_paciente = id_paciente
        self.nome = nome
        self.sexo = sexo.lower()
        try:
            self.data_nascimento = datetime.strptime(data_nascimento_str, "%Y-%m-%d").date()
            self.data_avaliacao = datetime.strptime(data_avaliacao_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Formato de data inválido. Use YYYY-MM-DD.")

        self.posicao_medicao = posicao_medicao.lower()
        self.edema = edema.lower() == "sim"
        
        if not all(isinstance(m, (int, float)) and m >= 0 for m in [
            peso_kg, estatura_m, dobra_tricipital_mm, circ_pescoco_cm,
            circ_braco_cm, circ_cintura_cm, circ_quadril_cm, circ_coxa_cm, circ_panturrilha_cm
        ]):
            raise ValueError("Medidas antropométricas devem ser números não negativos.")
        if estatura_m == 0:
            raise ValueError("Estatura não pode ser zero.")

        self.peso_kg = float(peso_kg)
        self.estatura_m = float(estatura_m)
        self.dobra_tricipital_mm = float(dobra_tricipital_mm)
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
            if today.month == 1:
                dias_no_mes_anterior = 31
            else:
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
        self._calcular_percentual_gordura_deurenberg()
        self._calcular_massas()
        self._calcular_rcq()
        self._calcular_rca()
        self._calcular_indice_conicidade()
        self._calcular_area_muscular_braco()
        self._calcular_peso_ideal(formula_peso_ideal)
        self._processar_circ_pescoco()
        return self.resultados

    def _calcular_imc(self):
        imc = self.paciente.peso_kg / (self.paciente.estatura_m ** 2)
        self.resultados["imc_valor"] = round(imc, 2)
        self.resultados["imc_class"] = self._classificar_imc_adulto(imc)

    def _classificar_imc_adulto(self, imc):
        if self.paciente.idade_anos < 19:
            return "Classificação por Z-score (OMS) recomendada para esta idade"
        if imc < 18.5: return "Baixo peso"
        elif 18.5 <= imc <= 24.9: return "Peso normal (eutrófico)"
        elif 25.0 <= imc <= 29.9: return "Sobrepeso"
        elif 30.0 <= imc <= 34.9: return "Obesidade Grau I"
        elif 35.0 <= imc <= 39.9: return "Obesidade Grau II"
        else: return "Obesidade Grau III"

    def _calcular_percentual_gordura_deurenberg(self):
        if "imc_valor" not in self.resultados:
            self._calcular_imc()

        imc = self.resultados["imc_valor"]
        idade = self.paciente.idade_decimal
        sex_factor = 1 if self.paciente.sexo == "masculino" else 0
        
        percentual_gordura = (1.20 * imc) + (0.23 * idade) - (10.8 * sex_factor) - 5.4
        
        self.resultados["percentual_gordura_valor"] = round(percentual_gordura, 2)
        class_gc = "N/A (Requer tabelas de referência específicas por idade/sexo)"
        if self.paciente.idade_anos >= 18:
            if self.paciente.sexo == "masculino":
                if 8 <= percentual_gordura <= 19: class_gc = "Saudável"
                elif percentual_gordura > 19 and percentual_gordura <=25: class_gc = "Aceitável / Sobrepeso"
                elif percentual_gordura > 25: class_gc = "Obeso"
                else: class_gc = "Abaixo do saudável"
            elif self.paciente.sexo == "feminino":
                if 21 <= percentual_gordura <= 33: class_gc = "Saudável"
                elif percentual_gordura > 33 and percentual_gordura <=39: class_gc = "Aceitável / Sobrepeso"
                elif percentual_gordura > 39: class_gc = "Obeso"
                else: class_gc = "Abaixo do saudável"
        self.resultados["percentual_gordura_class"] = class_gc
        self.resultados["percentual_gordura_metodo"] = "Deurenberg (1991)"

    def _calcular_massas(self):
        if "percentual_gordura_valor" not in self.resultados:
            self.resultados["massa_gorda_kg_valor"] = "N/A"
            self.resultados["massa_magra_kg_valor"] = "N/A"
            self.resultados["massa_magra_perc_valor"] = "N/A"
            return

        pg_perc = self.resultados["percentual_gordura_valor"]
        if pg_perc < 0:
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
        if rca < 0.4: return "Baixo risco / Magreza"
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
        class_ic = "N/A (Requer dados de referência específicos)"
        if self.paciente.idade_anos >= 18:
            if self.paciente.sexo == "masculino" and ic_val > 1.25: class_ic = "Risco aumentado"
            elif self.paciente.sexo == "feminino" and ic_val > 1.18: class_ic = "Risco aumentado"
            elif (self.paciente.sexo == "masculino" and ic_val <= 1.25) or \
                 (self.paciente.sexo == "feminino" and ic_val <= 1.18): class_ic = "Risco normal"
        self.resultados["ic_class"] = class_ic

    def _calcular_area_muscular_braco(self):
        tsf_cm = self.paciente.dobra_tricipital_mm / 10.0
        amb = ((self.paciente.circ_braco_cm - (math.pi * tsf_cm))**2) / (4 * math.pi)
        self.resultados["amb_valor"] = round(amb, 2)
        self.resultados["amb_class"] = "N/A (Requer tabelas de referência por idade/sexo)"

    def _calcular_peso_ideal(self, formula_nome="devine"):
        altura_pol = self.paciente.estatura_m * 39.3701
        peso_ideal_kg = None
        formula_usada = ""

        if altura_pol < 58:
            self.resultados["pi_valor"] = None
            self.resultados["pi_class"] = "Altura abaixo do limite comum para estas fórmulas"
            self.resultados["pi_formula"] = "N/A"
            return
        
        polegadas_acima_5pes = altura_pol - 60

        if formula_nome == "devine":
            formula_usada = "Devine (1974)"
            if self.paciente.sexo == "masculino":
                peso_ideal_kg = 50 + (2.3 * polegadas_acima_5pes)
            else:
                peso_ideal_kg = 45.5 + (2.3 * polegadas_acima_5pes)
        elif formula_nome == "robinson":
            formula_usada = "Robinson (1983)"
            if self.paciente.sexo == "masculino":
                peso_ideal_kg = 52 + (1.9 * polegadas_acima_5pes)
            else:
                peso_ideal_kg = 49 + (1.7 * polegadas_acima_5pes)
        elif formula_nome == "miller":
            formula_usada = "Miller (1983)"
            if self.paciente.sexo == "masculino":
                peso_ideal_kg = 56.2 + (1.41 * polegadas_acima_5pes)
            else:
                peso_ideal_kg = 53.1 + (1.36 * polegadas_acima_5pes)
        else:
            self.resultados["pi_valor"] = None
            self.resultados["pi_class"] = "Fórmula de peso ideal desconhecida"
            self.resultados["pi_formula"] = "N/A"
            return

        self.resultados["pi_valor"] = round(peso_ideal_kg, 2) if peso_ideal_kg is not None else None
        self.resultados["pi_class"] = "N/A (Comparar com peso atual para adequação)"
        self.resultados["pi_formula"] = formula_usada
        
    def _processar_circ_pescoco(self):
        cp_cm = self.paciente.circ_pescoco_cm
        self.resultados["cp_valor"] = cp_cm
        class_cp = "N/A"
        if self.paciente.idade_anos >=18:
            if self.paciente.sexo == "masculino":
                if cp_cm > 39: class_cp = "Risco aumentado (sugestivo de SM)"
            elif self.paciente.sexo == "feminino":
                if cp_cm > 35: class_cp = "Risco aumentado (sugestivo de SM)"
            else:
                class_cp = "Risco normal"
        self.resultados["cp_class"] = class_cp 