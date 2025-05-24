import os
import json
from datetime import datetime

ARQUIVO_DADOS = "dados_vendinha.json"

def carregar_dados():
    if not os.path.exists(ARQUIVO_DADOS):
        return []
    with open(ARQUIVO_DADOS, "r") as f:
        return json.load(f)

def salvar_dados(dados):
    with open(ARQUIVO_DADOS, "w") as f:
        json.dump(dados, f, indent=4)

def cadastrar_divida():
    nome = input("Nome do cliente: ").strip()
    cpf = input("CPF do cliente (apenas números): ").strip()
    valor = float(input("Valor da dívida (R$): "))
    mes = datetime.now().strftime("%m/%Y")

    dados = carregar_dados()

    for divida in dados:
        if divida["cpf"] == cpf and divida["mes"] == mes:
            print(f"\n⚠️ Este CPF já possui uma dívida no mês {mes}.\n")
            return

    nova_divida = {
        "nome": nome,
        "cpf": cpf,
        "valor_total": valor,
        "valor_pago": 0.0,
        "mes": mes
    }

    dados.append(nova_divida)
    salvar_dados(dados)
    print("\n✅ Dívida cadastrada com sucesso!\n")

def listar_dividas():
    dados = carregar_dados()
    if not dados:
        print("\nNenhuma dívida cadastrada.\n")
        return

    for i, d in enumerate(dados, 1):
        restante = d["valor_total"] - d["valor_pago"]
        status = "QUITADA" if restante <= 0 else "PENDENTE"
        print(f"{i}. {d['nome']} - CPF: {d['cpf']} - Total: R$ {d['valor_total']:.2f} - Pago: R$ {d['valor_pago']:.2f} - Restante: R$ {restante:.2f} - {d['mes']} - {status}")
    print()

def buscar_cliente():
    cpf = input("CPF do cliente para buscar: ").strip()
    dados = carregar_dados()
    encontrados = [d for d in dados if d["cpf"] == cpf]
    
    if not encontrados:
        print("\n❌ Nenhuma dívida encontrada para este CPF.\n")
        return

    for d in encontrados:
        restante = d["valor_total"] - d["valor_pago"]
        status = "QUITADA" if restante <= 0 else "PENDENTE"
        print(f"Cliente: {d['nome']} - CPF: {d['cpf']} - Total: R$ {d['valor_total']:.2f} - Pago: R$ {d['valor_pago']:.2f} - Restante: R$ {restante:.2f} - Mês: {d['mes']} - Status: {status}")
    print()

def pagar_divida():
    cpf = input("CPF do cliente para pagamento: ").strip()
    dados = carregar_dados()

    for d in dados:
        if d["cpf"] == cpf:
            restante = d["valor_total"] - d["valor_pago"]
            if restante <= 0:
                print("\n✅ Dívida já está quitada!\n")
                return

            print(f"\nValor restante: R$ {restante:.2f}")
            pagamento = float(input("Valor a pagar agora: R$ "))
            if pagamento <= 0:
                print("❌ Valor inválido.")
                return

            if pagamento > restante:
                print(f"⚠️ Pagamento excede o valor restante. Será ajustado para R$ {restante:.2f}.")
                pagamento = restante

            d["valor_pago"] += pagamento
            salvar_dados(dados)

            novo_restante = d["valor_total"] - d["valor_pago"]
            if novo_restante <= 0:
                print("\n💸 Dívida quitada com sucesso!\n")
            else:
                print(f"\n💰 Pagamento registrado. Restam R$ {novo_restante:.2f}.\n")
            return

    print("\n❌ Cliente não encontrado.\n")

def menu():
    while True:
        print("=== SISTEMA VENDINHA ===")
        print("1. Cadastrar dívida")
        print("2. Listar dívidas")
        print("3. Buscar cliente (por CPF)")
        print("4. Registrar pagamento (por CPF)")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_divida()
        elif opcao == "2":
            listar_dividas()
        elif opcao == "3":
            buscar_cliente()
        elif opcao == "4":
            pagar_divida()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!\n")

if __name__ == "__main__":
    menu()
