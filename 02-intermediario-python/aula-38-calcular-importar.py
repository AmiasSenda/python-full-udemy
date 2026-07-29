import aula37calcular

print('a) - Adição')
print('b) - Subtração')
print('c)- Multiplicação')
print('d) - Divisão')
opcao = input('digite a operacao: ')

if opcao == 'a':
    print('Soma: ',aula37calcular.soma(5,2))
elif opcao == 'b':
    print('Subtração: ',aula37calcular.sub(5,2))
elif opcao == 'c':
    print('Multiplicação: ',aula37calcular.mult(5,2))
elif opcao == 'd':
    print('Divisão: ',aula37calcular.divisao(5,2))

else:
    print('Opção Inexistente...')