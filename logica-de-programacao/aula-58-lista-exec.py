import os
valor = True
opcao = ''
lista = []
valorApagar = 0

while valor: 
    print ('Selecione uma opção:')
    opcao= input('[i]nserir [a]pagar [l]istar: ')
    if opcao == 'l':
        os.system('cls')
        if (len(lista)) == 0:
            print('Não temos valores na lista')
       
        else:
            for i in range(len(lista)):
                print(i,'',lista[i])
    elif opcao == 'i':
        novo = input('digite o novo item: ')
        lista.append(novo)
        os.system('cls')
        print("Item Adicionado!")
       

    elif opcao == 'a':
        if (len(lista)) == 0:
            os.system('cls')
            print('Não temos valores na lista para poder eliminar.')
        else:
            try:
                indice =int(input('Insira  o índice: '))
                avaliacao = 0
            except ValueError:
                print('índices são do tipo Inteiro...')
            except IndexError:
                print("Esse índice não existe na lista...")
            for i in range(len(lista)):
                if(indice == i):
                    del lista[indice]
                    os.system('cls')
                    print('Valor Eliminado!')
                    
                else:
                    avaliacao += 1
        
            if avaliacao != 0:
                os.system('cls')
                print('Este índice não pertence a nenhum índice')
    else:
        os.system('cls')
        print("Desculpe, mas não temos nenhuma dessas opções disponíveis.")
                


    
    



