perguntas = [
    {
        'pergunta1': 'Quanto é 2+2 ?',
        'op': ['4','5','2','1'],
        'resposta':'4'
    },
    
    {
        'pergunta1': 'Quanto é 5*5 ?',
        'op': ['25','55','10','50'],
        'resposta':'25'
    },
       
    {
        'pergunta1': 'Quanto é 10/2 ?',
        'op': ['4','5','2','1'],
        'resposta':'5'
    }
]
total = 0

for pergunta in perguntas:
    print('Questão: ',pergunta['pergunta1'])
    print()
    for i,  opcao in enumerate(pergunta['op']):
        print(f'{i})',opcao)
    
    op = input('Escolha uma Opção: ')
    esc = None
    if op.isdigit():
        esc = op
        if (op == pergunta['resposta']):
            print('ACERTOU!')
            total+=1
        else:
            print('ERROU')
    print()


print('Você acertou',total,' de 3 perguntas.')
print()