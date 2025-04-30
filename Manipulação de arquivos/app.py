import csv

# Função para criar o CSV
def criar_csv():
    dados = [
        ['Nome', 'Idade', 'Cidade'],
        ['Ana', '22', 'Curitiba'],
        ['Lucas', '28', 'Florianópolis']
    ]
    with open('pessoas.csv', 'w', newline='', encoding='utf-8') as f:
        csv.writer(f).writerows(dados)

# Função para ler o CSV
def ler_csv():
    with open('pessoas.csv', newline='', encoding='utf-8') as f:
        for linha in csv.reader(f):
            print(linha)

# Função para editar o CSV
def editar_csv():
    with open('pessoas.csv', newline='', encoding='utf-8') as f:
        pessoas = list(csv.reader(f))
    for p in pessoas:
        if p[0] == 'Ana':
            p[2] = 'Londrina'
    with open('pessoas.csv', 'w', newline='', encoding='utf-8') as f:
        csv.writer(f).writerows(pessoas)

# Execução
criar_csv()
print("Arquivo criado:")
ler_csv()
editar_csv()
print("\nArquivo atualizado:")
ler_csv()
