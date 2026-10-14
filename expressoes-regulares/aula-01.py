# EXPRESSÃO REGULAR: É uma forma de identificar cadeia de caracterer um padrão no seu meio.

# Nos permite validar padrão de caracteres.

# Funções em expressões Regulares


#findall - função
# search - função
#sub - função
# compile - função: me permite compilar as expressões regulares


import re #Me permite trabalhar com expressões regulares.

string = 'Este regulares é um teste de expressões regulares.'

print(re.search(r'regulares',string)) #Acha apenas uma vez

print(re.findall(r'regulares',string)) #Acha todas as vezes que foram encontradas e apresenta um vector. 
print(re.findall(r'ola',string)) # retorna lista vazia porque essa palavra não existe

print(re.sub(r'regulares','verdadeiro',string, count=1)) #Altera apenas uma vez.
print(re.sub(r'regulares','verdadeiro',string)) #Altera todas as vezes queencontrar.

# Compile

regexp = re.compile(r'teste')
print()
print('Com compile: ',regexp.search(string))
print('Com compile: ',regexp.findall(string))