nome = 'José Pascoal'


tamanho_nome = len(nome)
print(nome)
nome_a = '*'
print(tamanho_nome)

qt = int(tamanho_nome)
i = 0

while i < qt:
    nome_a += nome[i] + '*'
    i += 1
    
print('Término')

print(nome_a)