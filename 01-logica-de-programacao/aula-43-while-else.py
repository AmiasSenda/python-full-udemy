strings = 'Daniel António'

i = 0

while i < len(strings):
    letra = strings[i]
    if letra == ' ':
        break
    print(letra)
    i+=1

else:
    print('Else Exectudado.')

print('Fora do While')