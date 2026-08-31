
import os

quantBebida=0
precoBebida=0
NomeBebida=0
totalBebida=1

def menu_bebidas():
    os.system('cls')
    print("MENU DE BEBIDAS")
    print("________________________________")
    print("1- Bebidas Alcoolicas")
    print('2- Sumos naturais')
    print('3- Refrigerantes')
    print('4- Água')
    print()
    op  =input("digite  o seu  tipo de bebida: ")

    if (op == '1'):
        os.system('cls')
        print("BEBIDAS ALCOOLICAS")
        print("1- Fino | 500,00 kzs")
        print("2- Vinho Tinto | 800,00 kzs")
        print("3- Vinho Branco | 1.050,00 kzs")
        print()
        op01 = input("digite a Bebida: ")
        quantBebida =int(input("Digite a quantidade: "))
        match op01:
            case '1':
                precoBebida = 500
                NomeBebida="Fino"
            case '2':
                precoBebida = 800
                NomeBebida="Vinho Tinto"
            case '3':
                precoBebida = 1050
                NomeBebida="Vinho Branco"
            case _:
                print('Opção inválida')
        print("")

    elif (op == '2'):
        os.system('cls')
        print("SUMOS NATURAIS")
        print("1- Ananás Simples | 500,00 kzs")
        print("2- Laranja e Maracujá | 955,00 kzs")
        print("3- Manga e Laranja | 659,00 kzs")
        print()
        op01 = input("digite a Bebida: ")
        quantBebida =int(input("Digite a quantidade: "))
        match op01:
            case '1':
                precoBebida = 500
                NomeBebida="Ananás Simples"
            case '2':
                precoBebida = 955
                NomeBebida="Laranja e Maracujá"
            case '3':
                precoBebida = 659
                NomeBebida="Manga e Laranja"
            case _:
                print('Opção inválida')
        print("")

    elif (op == '3'):
        os.system('cls')
        print("REFRIGERANTES")
        print("1- Coca-cola | 500,00 kzs")
        print("2- Fanta | 560,00 kzs")
        print("3- Sumol de Ananás | 700,00 kzs")
        print()
        op01 = input("digite a Bebida: ")
        quantBebida =int(input("Digite a quantidade: "))
        match op01:
            case '1':
                precoBebida = 500
                NomeBebida="Coca-cola"
            case '2':
                precoBebida = 560
                NomeBebida="Fanta"
            case '3':
                precoBebida = 700
                NomeBebida="Sumol de Ananás"
            case _:
                print('Opção inválida')

    elif (op == '4'):
        os.system('cls')
        print("ÁGUA")
        print("1- Água com Gás | 980,00 kzs")
        print("2- Água sem Gás | 500,00 kzs")
        print()
        op01 = input("digite a Bebida: ")
        quantBebida =int(input("Digite a quantidade: "))
        match op01:
            case '1':
                precoBebida = 980
                NomeBebida="Água com Gás"
            case '2':
                precoBebida = 500
                NomeBebida="Água sem Gás"
            case _:
                print('Opção inválida')
        print("")



    totalBebida = precoBebida *quantBebida
    resultado = f"{totalBebida:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    preco = f"{precoBebida:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    print("__________________________________________________________")
    print("FACTURA BEBIDA")
    print("__________________________________________________________")

    print("Bebida escolhida: ",NomeBebida)
    print("Preço: ",preco,' KZS')   
    print("Quantidade: ",quantBebida)
    print('Total: ',resultado, ' KZS')
    print("__________________________________________________________")
    print("")
