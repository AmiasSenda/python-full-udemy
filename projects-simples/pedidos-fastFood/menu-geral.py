from bebidas import menu_bebidas
from cachorros import menu_cachorro
import bebidas
import os

totalBebidas= 0
totalCachorro = 0
total =0
condicao = True
cond = 0

while condicao: 
    os.system('cls')
    print("BEM-VINDO AO FASTHAPPY")
    print("______________________________")
    print("EIS OS MENUS")
    print("______________________________")
    print("1- PIZZAS")
    print("2- HAMBÚRGUERS")
    print("3- CACHORRO QUENTE")
    print("4- BEBIDAS")
    print("5- EXTRAS")
    print("")
    opcao = input("DIGITE A SUA OPÇÃO: ") 


    match opcao:
        case '1':
            print()
        case '2':
            print()
        case '3':
            totalCachorro+= menu_cachorro()
            print(totalCachorro)
            print()
        case '4':
            totalBebidas +=menu_bebidas()
            print(totalBebidas)
        case '5':
            print()
        case _:
            print("Opção inexistente...")

    #os.system('cls')
    cond = input("Deseja permanecer uma outra escolha ou nem por isso ? (0/1)")
    if (cond =='1'):
        break
os.system('cls') 
ftTotal= input("Deseja verificar a factura final ? (S/N)")
if (ftTotal =='1'):
    bebidas = f"{totalBebidas:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    cachorro = f"{totalCachorro:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    total = totalBebidas + totalCachorro
    os.system('cls')
    print("----------------------------------------------------")
    print("Factura Geral")
    print("_____________________________________________________")
    print('Total do menu Bebidas: ',bebidas)
    print('Total do menu Cachorro Quente: ',cachorro)
    print("Total da Factura: ", total,'KZS')
