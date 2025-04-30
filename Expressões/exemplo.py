import re

texto = "O produto custa 150 reais e o frete é 20 reais."

numeros = re.findall(r'\d+', texto)

print("Números encontrados:", numeros)