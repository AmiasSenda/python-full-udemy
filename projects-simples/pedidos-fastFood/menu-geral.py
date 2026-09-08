from bebidas import menu_bebidas
from cachorros import menu_cachorro
from extras import menu_extras
from Pizzas import menu_pizzas
from Hamburguers import menu_hamburguers
import bebidas
import os

totalBebidas= 0
totalCachorro = 0
totalExtras = 0
totalPizza = 0
totalHamburguers = 0
total =0
condicao = True
cond = 0
opcao = 0
def menu_principal():
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
    Valor = input("DIGITE A SUA OPÇÃO: ") 
    return Valor

while condicao: 

    opcao = menu_principal()
    print(opcao)
    match opcao:
        case '1':
            totalPizza += menu_pizzas()
            print(totalPizza)
        case '2':
            totalHamburguers += menu_hamburguers()
            print(totalHamburguers)
        case '3':
            totalCachorro+= menu_cachorro()
            print(totalCachorro)
            print()
        case '4':
            totalBebidas +=menu_bebidas()
            print(totalBebidas)
        case '5':
            totalExtras += menu_extras()
            print(totalExtras)
            print()

    #os.system('cls')
    cond = input("Deseja permanecer uma outra escolha ou nem por isso ? (0/1)")
    if (cond =='1'):
        break
os.system('cls') 
ftTotal= input("Deseja verificar a factura final ? (S/N)")
if (ftTotal =='1'):
    bebidas = f"{totalBebidas:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    pizza = f"{totalPizza:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    cachorro = f"{totalCachorro:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    extras = f"{totalExtras:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    hamburguers = f"{totalHamburguers:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    total = totalBebidas + totalCachorro + totalExtras + totalPizza + totalHamburguers
    totalTudo = f"{total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    os.system('cls')
    print("----------------------------------------------------")
    print("Factura Geral")
    print("_____________________________________________________")
    print('Total do menu Pizzas: ',pizza, 'KZS')
    print('Total do menu Cachorro-Quente: ',cachorro, 'KZS')
    print('Total do menu Hamburguers: ',hamburguers, 'KZS')
    print('Total do menu Bebidas: ',bebidas, 'KZS')
    print('Total de Extras solicitados: ',extras,'KZS')
    print(".......................................................")
    print()

    print("Total da Factura: ", totalTudo,'KZS')
    print("")
