pessoa = {
    'nome': 'Amias Bento José',
    'sobrenome': 'Senda',
    'idade':26,
    'altura': 1.76,
}

print('Dicionário completo')
print(pessoa)
print()
print('Método get')
print(pessoa.get('palavra',None)) # Procura ver se a chave existe ou não.
print()
print('Após remover a primeira chave e o item da chave')
nome = pessoa.pop('nome') #Elimina a chave e o seu valor
print(nome)

print(pessoa)
ultima_chave = pessoa.popitem() #Remove a última chave e o seu item
print()
print('Após remover a última chave e o item da chave')
print(pessoa)

print()

print('Actualizando o dicionário')

pessoa.update({
    'telefone': '942-827-224'
})

print(pessoa)
print()

