
entrada =input('Digite o número: ')
print()

if entrada.isdigit():
    num = int(entrada)
    if num : 
        par = (num %2) == 0

    if par:
        print(num, ' É um número Par!')
    else:
        print(num,' É um número impar!')


else:
    print('Você não digitou um número inteiro...')

print()