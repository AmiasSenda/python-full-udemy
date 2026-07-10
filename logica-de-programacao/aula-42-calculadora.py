condicao = True

while condicao:
    op = '+-*/'
    n1 = (input('digite um número: '))
    n2 = (input('digite o outro númeor: '))
    print()
    print('Qual operação que podem ser realizadas: ')
    print('+ | Adição')
    print('- | Subtração')
    print('/ | divisão')
    print('* | Multiplicação')
    print()
    operador = input('Insere o Operador: ')
    print()
    num_validos = None
    try:
        num1_float = float(n1)
        num2_float = float(n2)
        num_validos = True
        if operador not in op:
            print('Operador Inválido!')  
            continue

        if len(operador) >1:
            print("Digite apenas um operador.")
            continue 

        if operador == '+':
            print(num1_float, ' + ',num2_float, ' = ',num1_float + num2_float)
        elif operador == '-':
             print(num1_float, ' - ',num2_float, ' = ',num1_float - num2_float)
        elif operador == '*':
            print(num1_float, ' * ',num2_float, ' = ',num1_float * num2_float)
        elif operador == '/':
            print(num1_float, ' / ',num2_float, ' = ',num1_float / num2_float)
        else:
            print('Nunca deveria chegar aqui...')
        
    except:
       
        num_validos = None

        if num_validos is None:
            print("um ou ambos os números digitados são inválidos...")
            continue

        
    print()

    sair= input('Quer sair ? [y] or [n]: ')
    sair= sair.lower()
    sair = sair.startswith('y')
    if sair is True:
        break
