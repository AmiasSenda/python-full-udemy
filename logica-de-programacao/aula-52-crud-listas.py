frutas = ['Banana','Laranja','Abacaxi','Uva','Goiaba','Morangos','Loengos','Pacassa']

frutas[2] = 'Ananás'
del frutas[7] #Elimina o valor deste índice
frutas.append('Papaya') #adiciona na lista (no fim)
ultimo_valor =frutas.pop() # remove o último elemento da lista

print('Frutas da época: ')
print()
for i in range(len(frutas)):
    print(i,'-',frutas[i])

print()
print('Valor removido: ',ultimo_valor)
print()