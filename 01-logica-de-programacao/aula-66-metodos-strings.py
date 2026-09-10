nome1='Amias Bento'
nome2='José Senda'
titulo = 'a excelência é a minha porção!'

print("Nome: ",nome1)
print("Em Letras miúsculas: ",nome1.upper())
print("Em letras minúsculas: ",nome1.lower())
print("Script:  ",nome1.strip())

print("Subistituir O sobrenome:", nome1.replace('Bento',nome2))
listaNome  = nome1.split()
print("Tornar a string em lista: ",listaNome)
print("Tornar lista em string: ",' '.join(listaNome))
print("Verificar se o nome termina com Bento: ",nome1.endswith('Bento'))
print("Verificar a posição onde se inicia o nome 'Bento': ", nome1.find('Bento'))
print("Quantas vezes a letra 'a' aparece no nome ? | R: ",nome1.count('a'))
print("Primeira letra maiúscula e todas as outras minúsculas: ", nome1.capitalize())
print("Todas as letras estão em Maiúsculas ? | R: ", nome1.isupper())
print("Todas as letras estão minúsculas ? | R:", nome1.islower())
print("Título do filme: ",titulo.title())
print()


