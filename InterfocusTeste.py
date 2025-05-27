ARQUIVO_DADOS = "dados_vendinha.txt"
ARQUIVO_RELATORIO = "relatorio_vendinha.txt"
ARQUIVO_PAGAMENTOS = "pagamentos.txt"
ARQUIVO_SENHA = "senha.txt"

def inicializar_sistema():
    f = open(ARQUIVO_SENHA, "a+")
    f.seek(0)
    conteudo = f.read()
    if conteudo.strip() == "":
        f.write("admin123\n")
    f.close()

def redefinir_senha():
    print("🔁 Recuperação de senha")
    palavra = input("Digite a palavra secreta: ").strip()
    if palavra == "vendinha":
        nova = input("Digite a nova senha: ").strip()
        f = open(ARQUIVO_SENHA, "w")
        f.write(nova + "\n")
        f.close()
        print("✅ Senha redefinida com sucesso.")
    else:
        print("❌ Palavra secreta incorreta.")

def autenticar():
    print("1. Entrar no sistema")
    print("2. Esqueci a senha")
    escolha = input("Escolha uma opção: ").strip()
    
    if escolha == "2":
        redefinir_senha()
        exit()
    
    f = open(ARQUIVO_SENHA, "r")
    senha_correta = f.read().strip()
    f.close()

    senha = input("Digite a senha do sistema: ").strip()
    if senha != senha_correta:
        print("❌ Acesso negado.")
        exit()

def carregar_dados():
    dados = []
    f = open(ARQUIVO_DADOS, "a+")
    f.seek(0)
    for linha in f:
        partes = linha.strip().split("|")
        if len(partes) == 7:
            nome, cpf, telefone, valor_total, valor_pago, mes, obs = partes
            dados.append({
                "nome": nome,
                "cpf": cpf,
                "telefone": telefone,
                "valor_total": float(valor_total),
                "valor_pago": float(valor_pago),
                "mes": mes,
                "obs": obs
            })
    f.close()
    return dados

def salvar_dados(dados):
    f = open(ARQUIVO_DADOS, "w")
    for d in dados:
        linha = f"{d['nome']}|{d['cpf']}|{d['telefone']}|{d['valor_total']}|{d['valor_pago']}|{d['mes']}|{d['obs']}\n"
        f.write(linha)
    f.close()

def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

def obter_mes_atual():
    t = __import__("time").localtime()
    return f"{t.tm_mon:02}/{t.tm_year}"

def cadastrar_divida():
    nome = input("Nome do cliente: ").strip()
    cpf = input("CPF (somente números): ").strip()
    if not validar_cpf(cpf):
        print("❌ CPF inválido.")
        return
    telefone = input("Telefone do cliente: ").strip()
    valor = float(input("Valor da dívida: R$ "))
    obs = input("Observações: ").strip()
    mes = obter_mes_atual()

    dados = carregar_dados()
    for d in dados:
        if d["cpf"] == cpf and d["mes"] == mes:
            print("⚠️ Este CPF já possui dívida neste mês.")
            return

    nova = {
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "valor_total": valor,
        "valor_pago": 0.0,
        "mes": mes,
        "obs": obs
    }
    dados.append(nova)
    salvar_dados(dados)
    print("✅ Dívida cadastrada.")

def listar_dividas():
    dados = carregar_dados()
    if not dados:
        print("Nenhuma dívida.")
        return

    total_geral = total_pago = total_pendente = 0
    for d in dados:
        restante = d["valor_total"] - d["valor_pago"]
        total_geral += d["valor_total"]
        total_pago += d["valor_pago"]
        total_pendente += max(0, restante)
        status = "QUITADA" if restante <= 0 else "PENDENTE"
        print(f"{d['nome']} | CPF: {d['cpf']} | Tel: {d['telefone']} | Total: R$ {d['valor_total']:.2f} | Pago: R$ {d['valor_pago']:.2f} | Restante: R$ {restante:.2f} | {d['mes']} | {status} | Obs: {d['obs']}")

    print(f"---\nTOTAL GERAL: R$ {total_geral:.2f} | TOTAL PAGO: R$ {total_pago:.2f} | TOTAL PENDENTE: R$ {total_pendente:.2f}\n")

def buscar_cliente():
    cpf = input("CPF do cliente: ").strip()
    dados = carregar_dados()
    encontrados = [d for d in dados if d["cpf"] == cpf]
    if not encontrados:
        print("❌ Nenhuma dívida encontrada.")
        return
    for d in encontrados:
        restante = d["valor_total"] - d["valor_pago"]
        status = "QUITADA" if restante <= 0 else "PENDENTE"
        print(f"{d['nome']} | CPF: {d['cpf']} | Tel: {d['telefone']} | Total: R$ {d['valor_total']:.2f} | Pago: R$ {d['valor_pago']:.2f} | Restante: R$ {restante:.2f} | {d['mes']} | {status} | Obs: {d['obs']}")

def registrar_pagamento_log(cpf, nome, valor, mes):
    f = open(ARQUIVO_PAGAMENTOS, "a")
    f.write(f"{cpf}|{nome}|{valor}|{mes}\n")
    f.close()

def pagar_divida():
    cpf = input("CPF do cliente: ").strip()
    dados = carregar_dados()
    for d in dados:
        if d["cpf"] == cpf:
            restante = d["valor_total"] - d["valor_pago"]
            if restante <= 0:
                print("✅ Dívida já quitada.")
                return
            print(f"Restante: R$ {restante:.2f}")
            valor = float(input("Valor a pagar agora: R$ "))
            if valor <= 0:
                print("❌ Valor inválido.")
                return
            if valor > restante:
                print(f"⚠️ Valor ajustado para R$ {restante:.2f}")
                valor = restante
            d["valor_pago"] += valor
            salvar_dados(dados)
            registrar_pagamento_log(d["cpf"], d["nome"], valor, d["mes"])
            print("💰 Pagamento registrado.")
            return
    print("❌ CPF não encontrado.")

def excluir_divida():
    cpf = input("CPF para excluir: ").strip()
    dados = carregar_dados()
    novos = [d for d in dados if d["cpf"] != cpf]
    if len(novos) == len(dados):
        print("❌ Nenhuma dívida encontrada.")
    else:
        salvar_dados(novos)
        print("🗑️ Dívidas excluídas.")

def gerar_relatorio():
    dados = carregar_dados()
    f = open(ARQUIVO_RELATORIO, "w")
    for d in dados:
        restante = d["valor_total"] - d["valor_pago"]
        status = "QUITADA" if restante <= 0 else "PENDENTE"
        f.write(f"{d['nome']}|{d['cpf']}|{d['telefone']}|{d['valor_total']}|{d['valor_pago']}|{restante}|{d['mes']}|{status}|{d['obs']}\n")
    f.close()
    print("📄 Relatório gerado.")

def listar_por_mes():
    mes = input("Digite o mês no formato MM/AAAA: ").strip()
    dados = carregar_dados()
    encontrados = [d for d in dados if d["mes"] == mes]
    if not encontrados:
        print("❌ Nenhuma dívida encontrada para esse mês.")
        return
    for d in encontrados:
        restante = d["valor_total"] - d["valor_pago"]
        status = "QUITADA" if restante <= 0 else "PENDENTE"
        print(f"{d['nome']} | CPF: {d['cpf']} | Tel: {d['telefone']} | Total: R$ {d['valor_total']} | Pago: R$ {d['valor_pago']} | Restante: R$ {restante} | {status} | Obs: {d['obs']}")

def listar_por_status():
    print("Filtrar por status:")
    print("1. PENDENTE")
    print("2. QUITADA")
    escolha = input("Escolha o tipo de dívida: ").strip()

    if escolha == "1":
        status_desejado = "PENDENTE"
    elif escolha == "2":
        status_desejado = "QUITADA"
    else:
        print("❌ Opção inválida.")
        return

    dados = carregar_dados()
    encontrados = []
    for d in dados:
        restante = d["valor_total"] - d["valor_pago"]
        status = "QUITADA" if restante <= 0 else "PENDENTE"
        if status == status_desejado:
            encontrados.append(d)

    if not encontrados:
        print(f"❌ Nenhuma dívida com status {status_desejado}.")
        return

    for d in encontrados:
        restante = d["valor_total"] - d["valor_pago"]
        print(f"{d['nome']} | CPF: {d['cpf']} | Tel: {d['telefone']} | Total: R$ {d['valor_total']} | Pago: R$ {d['valor_pago']} | Restante: R$ {restante} | {status_desejado} | Obs: {d['obs']}")

def menu():
    autenticar()
    while True:
        print("\n=== SISTEMA VENDINHA ===")
        print("1. Cadastrar dívida")
        print("2. Listar dívidas")
        print("3. Buscar cliente")
        print("4. Registrar pagamento")
        print("5. Excluir dívida")
        print("6. Gerar relatório")
        print("7. Listar dívidas por mês")
        print("8. Listar dívidas por status")
        print("9. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1": cadastrar_divida()
        elif opcao == "2": listar_dividas()
        elif opcao == "3": buscar_cliente()
        elif opcao == "4": pagar_divida()
        elif opcao == "5": excluir_divida()
        elif opcao == "6": gerar_relatorio()
        elif opcao == "7": listar_por_mes()
        elif opcao == "8": listar_por_status()
        elif opcao == "9": break
        else: print("Opção inválida.")

# Início do sistema
inicializar_sistema()
menu()
