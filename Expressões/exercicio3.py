import re

def validar_cep(cep):
    return bool(re.match(r'^\d{5}-\d{3}$', cep))

cep = "12345-678"
print(validar_cep(cep))