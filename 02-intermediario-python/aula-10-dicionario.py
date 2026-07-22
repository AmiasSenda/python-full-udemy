pessoa = {
    'nome': 'Amias Bento José',
    'sobrenome': 'Senda',
    'idade':26,
    'altura': 1.76,
    'enderecos':
    [
        {
            'rua': 'A & B', 'numero':123
        },
        {
            'rua': 'C & D', 'numero':898
        }
    ]
}

#pessoa = dict(nome = 'Adilson Muta', sobrenome = 'Fuxe')
print(pessoa['nome'],pessoa['sobrenome'])
print(pessoa['idade'])
print(pessoa['altura'])
print(pessoa['enderecos'])
print()

for chave in pessoa:
    print(chave, ': ', pessoa[chave])