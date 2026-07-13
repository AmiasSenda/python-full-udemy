senha_correcta= '123456'
senha_digitada = ' '
repeticoes = 0


while senha_correcta != senha_digitada:
    senha_digitada = input(f'sua senha ({repeticoes}x): ')

    repeticoes += 1

print()
print('Total de tentativas: ',repeticoes)