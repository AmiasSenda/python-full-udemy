import os


palavra_secrecta = 'Amor'
letra_acertada = ''
tentativas = 0
valor = True

while valor:
    

    palavra_digitada = input('digite uma letra: ')
    tentativas +=1
    if len(palavra_digitada) > 1:
        print('digite apenas uma letra.')
        continue

    if palavra_digitada in palavra_secrecta:
        letra_acertada +=palavra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secrecta:
        if(letra_secreta in letra_acertada):
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(palavra_formada)
    

    if palavra_formada == palavra_secrecta:

        os.system('cls')
        print("VOCÊ GANHOU! PARABÉNS")
        print("A PALAVRA ERA: ",palavra_secrecta)
        print("Nº de tentativas: ",tentativas)
        print('')
        valor = False