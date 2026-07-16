frase = "Hi! i'm  Amias Senda, I love to study and to cook"
palavras_frase = frase.split(',')
print(palavras_frase)


#SEM ELIMINAR OS ESPAÇOS

for i in range(len(palavras_frase)):
    print(palavras_frase[i])

# A ELIMINAR OS ESPAÇOS

for i in range(len(palavras_frase)):
    print(palavras_frase[i].strip())