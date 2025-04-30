import re

texto = "Em 2023, o Brasil teve a temeperatura 21 graus Celsius. Em 2024, o Brasil teve a temperatura 22 graus Celsius."
ano = re.findall(r'\b\d{4}\b', texto)
temperatura = re.findall(r'\b\d{1,2}\s*graus\s*Celsius\b', texto)
print("Anos encontrados:", ano)
print("Temperaturas encontradas:", temperatura)
