import os


caminho_arquivo = 'aula64.txt'

with open(caminho_arquivo,'w',encoding='utf8') as arquivo:
    arquivo.write('Teste 01 \n')
    arquivo.write('Atenção \n')
    arquivo.writelines(('Teste 02\n' ,'teste 03 \n'))



os.unlink(caminho_arquivo)


os.rename(caminho_arquivo, 'aula642.txt')