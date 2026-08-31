import os

quantBebida=0
precoBebida=0
totalBebida=0


print("EIS As opções de Bebidos da casa")
print("________________________________")
print("1- Bebidas Alcoolicas")
print('2- Sumos naturais')
print('3- Refrigerantes')
print("4- Bebidas energéticas")
print("5- Água")
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
    
#if(op == '2'):


"""

print("SUMOS NATURAIS")
print("1- Ananás Simples | 500,00 kzs")
print("2- Laranja e Maracujá | 955,55 kzs")
print("3- Manga e Laranja | 659,00 kzs")

print("REFRIGERANTES")
print("1- Coca-cola | 500,00 kzs")
print("2- Fanta | 560,00 kzs")
print("3- Sumol de Ananás | 700,00 kzs")

print("BEBIDAS ENERGÉTICAS")
print("1- RedBull | 1.500,00 kzs")

"""
