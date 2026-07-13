for i in range(10):
    if i == 2:
        print('Pulando')
        continue
    if i == 8:
        print(' bla bla bla')
        break
    for j in range (1,3):
        print(i,j)
else:
    print('For completo com Sucesso!' )