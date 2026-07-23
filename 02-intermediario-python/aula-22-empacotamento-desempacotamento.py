a,b = 1,2
print(a,b)

a,b = b,a

print(a,b)

pessoa = {
    'nome': 'Amias Senda',
    'sobrenome': 'Baby'
}

a,b = pessoa

print(a,b)

(a,b),(c,d)= pessoa.items()

print(a,b)
print(c,d)
print(b,d)


dados_pessoa = {
    'idade': 26,
    'altura':1.67
}

print(pessoa, dados_pessoa)

#Adicionando

pessoa_completa = {**pessoa, **dados_pessoa, 'sexo': 'Femenino'}

def mostrar_argumentos_nomeados (*args, **kwargs):
    print('NÃO NOMEADOS: ',args)

    for chave,valor in kwargs.items():
        print(chave,valor)


#mostrar_argumentos_nomeados (nome = 'Adilson', id = 450)

mostrar_argumentos_nomeados (**pessoa_completa)



