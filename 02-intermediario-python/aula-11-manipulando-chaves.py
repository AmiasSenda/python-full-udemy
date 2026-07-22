# Métodos úteis dos dicionários em Python

pessoa = {
    'nome': 'Amias Bento José',
    'sobrenome': 'Senda',
    'idade':26,
    'altura': 1.76,
}

print(len(pessoa)) # Mostra a quantidade de chaves.
print(pessoa.keys()) #Mostra as chaves
print(pessoa.values()) #Apresenta só os valores 
print(pessoa.items()) #Apresenta a chave e o valor
print(pessoa.setdefault('telefone','942-837-224')) #Acrescenta uma nova chave e um valore




