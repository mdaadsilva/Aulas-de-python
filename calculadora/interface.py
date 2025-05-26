from datetime import date
from .utils import obter_input_float, obter_input_data, obter_input_escolha
from .models import Paciente, CalculadoraAntropometrica
from .storage import carregar_paciente, salvar_paciente

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
    print("-" * 105)
    
    print("\nNotas Importantes:")
    print("- Z-scores e Percentis NÃO foram calculados (requerem dados de referência complexos).")
    print("- Classificações de % Gordura e outras são gerais e podem necessitar de contextualização.")
    print("- Para indivíduos <19 anos, classificações e avaliações devem seguir padrões de crescimento pediátrico (ex: OMS), não totalmente implementados aqui.")

def coletar_dados_paciente():
    print("\n--- Dados do Paciente ---")
    try:
        id_paciente = input("ID do Paciente (ex: 001): ")
        nome_paciente = input("Nome do Paciente: ")
        sexo = obter_input_escolha("Sexo (Masculino/Feminino): ", ["Masculino", "Feminino"])
        data_nasc = obter_input_data("Data de Nascimento (YYYY-MM-DD): ")
        data_aval = obter_input_data("Data da Avaliação (YYYY-MM-DD, deixe em branco para hoje): ")
        if not data_aval:
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

        return Paciente(
            id_paciente, nome_paciente, sexo, data_nasc, data_aval,
            posicao, edema_str, peso, estatura, dc_tricipital,
            circ_pescoco, circ_braco, circ_cintura, circ_quadril,
            circ_coxa, circ_panturrilha
        )
    except ValueError as ve:
        print(f"Erro de Valor: {ve}")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return None

def main():
    print("--- Calculadora Antropométrica Avançada (Python) ---")
    
    acao = obter_input_escolha("Deseja (N)ovo paciente ou (C)arregar existente? ", ["N", "C"])

    if acao == "C":
        id_busca = input("Digite o ID do paciente para carregar: ")
        paciente_obj, resultados_carregados = carregar_paciente(id_busca)
        if paciente_obj and resultados_carregados:
            exibir_resultados(paciente_obj, resultados_carregados)
            print("\nFim da exibição dos dados carregados.")
            return
        else:
            print("Iniciando cadastro de novo paciente.")

    paciente_obj = coletar_dados_paciente()
    if not paciente_obj:
        return

    formula_pi_escolha = obter_input_escolha(
        "Escolha a fórmula para Peso Ideal (Devine/Robinson/Miller): ",
        ["Devine", "Robinson", "Miller"]
    )

    calculadora = CalculadoraAntropometrica(paciente_obj)
    resultados_finais = calculadora.calcular_todos(formula_peso_ideal=formula_pi_escolha.lower())
    
    exibir_resultados(paciente_obj, resultados_finais)
    
    if obter_input_escolha("\nDeseja salvar os dados deste paciente? (S/N): ", ["S", "N"]) == "S":
        salvar_paciente(paciente_obj, resultados_finais) 