def mult (*args):
    total = 1
    for num in args:
        total *=num
    print('Total: ',total)
    print()


def par_impar(num):
    if num % 2 == 0:
        print(num,' é um número par!')
        print()
    else:
        print(num,' é um número ímpar!')
        print()


num =int(input('Digite um número: '))
par_impar(num)

mult(3,3,3)