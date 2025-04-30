import re

texto = "Exemplo de texto com várias palavras."
palavra = "PALAVRAS"

resultado = re.search(palavra, texto, re.IGNORECASE)
if resultado:
    print("Palavra encontrada!")
else:
    print("Palavra não encontrada.")