"""
Funções que vamos estudar:
findall: 
search : pesquisa um determinado campo ou uma outra coisa.
sub: subistituir
compile:compilar
"""
import re

string ="TESTE DE EXPRESSÕES REGULARES"

print(re.search(r'TESTE',string)) # Me permite encontrar a palavra teste na variavel string.

print(re.findall(r'TESTE',string))
print(re.sub(r'TESTE','AMOR',string))

regexp = re.compile(r'TESTE')
regexp.search(string)
regexp.findall(string)


print(regexp.sub('DEF',string))
