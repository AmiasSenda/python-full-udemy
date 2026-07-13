frase = 'Amias Bento jose Senda '.lower()

print(frase)

#print(frase.count('python'))

i = 0
apareceu_mais = 0
letra_apareceu_mais = ' '
while i < len(frase):
    letra_actual = frase[i]

    if letra_actual == ' ':
        i+=1
        continue
    quantas_vezes = frase.count(letra_actual)
    if (apareceu_mais < quantas_vezes):
        apareceu_mais = quantas_vezes
        letra_apareceu_mais = letra_actual
    i+=1

print('Letra que apareceu mais vezes:"',letra_apareceu_mais.upper(), '" ', apareceu_mais)