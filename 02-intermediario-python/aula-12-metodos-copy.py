pessoa = {
    'nome': 'Amias Bento José',
    'sobrenome': 'Senda',
    'idade':26,
    'altura': 1.76,
}

print(pessoa)
#Fazendo cópia com um método

pessoa2 = pessoa.copy()

#Fazendo a cópia de forma normal

#pessoa1 = pessoa
print()
# ,Manipular a Pessoa 1 
#pessoa1 ['nome'] = 'Adilson Fuxe' # Isso mudar até no dicionário antigo.
#print(pessoa1)

print()
#print(pessoa)

print()


#Manipular o Pessoa 2
pessoa2['nome'] = 'Daniel António'
print(pessoa2)
print(pessoa)