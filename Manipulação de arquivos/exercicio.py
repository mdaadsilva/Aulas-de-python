import csv  # Importa a biblioteca que ajuda a trabalhar com arquivos CSV

# Cria uma lista vazia que vai guardar os dados dos alunos
alunos = []

# Pede ao usuário para cadastrar 3 alunos
for i in range(3):
    # Solicita o nome do aluno
    nome = input("Digite o nome do aluno: ")
    
    # Solicita a idade do aluno
    idade = input("Digite a idade do aluno: ")
    
    # Solicita o curso do aluno
    curso = input("Digite o curso do aluno: ")
    
    # Aqui você deve adicionar os dados desse aluno à lista 'alunos'
    # Dica: use uma lista com nome, idade e curso dentro da lista principal
    # Exemplo: alunos.append([...])
    

# Abre (ou cria) um arquivo chamado 'alunos.csv' para escrita
with open('alunos.csv', 'w', newline='', encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo)
    
    # Escreva os nomes das colunas no topo do arquivo (cabeçalho)
    # Dica: use .writerow() com uma lista com os nomes das colunas
    
    # Escreva os dados dos alunos no arquivo
    # Dica: use .writerows() para gravar todos os alunos de uma vez


# Agora vamos abrir o mesmo arquivo para leitura e exibir os dados
with open('alunos.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    
    print("\n--- Lista de Alunos ---")
    
    # Pule a primeira linha (cabeçalho) antes de exibir os dados
    # Dica: use next(leitor) para isso
    
    # Percorra cada linha do arquivo e mostre os dados formatados
    for linha in leitor:
        # Dica: use print() com f-string para mostrar os dados no formato:
        # Nome: ... | Idade: ... | Curso: ...
        pass  # Remova o 'pass' e escreva seu código aqui
