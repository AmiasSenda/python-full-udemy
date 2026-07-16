linha = 1
qtlinhas = 5
qtcolunas = 5

while linha <= qtlinhas:
    coluna = 1
    print('Linha: ',linha)

    while coluna <= qtcolunas:
        print(f'{linha=} {coluna=}')
        coluna+=1
    linha +=1


print(linha)