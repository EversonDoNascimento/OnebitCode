import re

# 1 - Índice inicial e final de palavras
text = "OneBitCode: Transformamos pessoas em programadores sem limites"
# O r significa que estamos trabalhando com uma string bruta(raw string)

match = re.search(r'pessoas em programadores',text)
print('Índice inicial', match.start())
print('Índice final', match.end())

# 2 - Buscando o índice que possui o ponto
site = "https://onebitcode.com"
match = re.search(r'\.',site)
print(match)