from bebidas import menu_bebidas
from facturaGeral import total

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
        print()
    case '4':
        print(menu_bebidas())
    case '5':
        print()
    case _:
        print("Opção inexistente...")


ftTotal= input("Deseja verificar a factura final ? (S/N)")
if (ftTotal =='1'):
    print(total())
