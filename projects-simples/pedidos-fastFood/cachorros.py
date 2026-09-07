import os

quantFood=0
precoFood=0
NomeFood=0
totalFood=0
idPro= 0
nomePro = ''
precoPro = ''
Op= 0


menu = {
        1: {"nome": "Cachorro Simples", "preco": 2500},
        2: {"nome": "Cachorro com Queijo", "preco": 3000},
        3: {"nome": "Cachorro com Bacon", "preco": 3500},
        4: {"nome": "Cachorro Especial", "preco": 4000},
        5: {"nome": "Cachorro Completo", "preco": 4500}
}

def menu_cachorro():
#print(menu[3]["nome"],' | ',menu[3]["preco"])
    os.system("cls")
    print("MENU FASTFOOD - CACHORRO - QUENTE")
    print("_______________________________________________")
    for index,dados in menu.items():
        idPro= index
        nomePro = dados["nome"]
        precoPro = dados["preco"]
        print(idPro, ' - ', nomePro, ' - ', precoPro)
    print("")

    Op=int(input("Digite a sua escolha: "))   

    for index,dados in menu.items():
        idA = index
        if (Op == idA):
            NomeFood = dados["nome"]
            precoFood =dados["preco"]
    quantFood = int(input("digite a quantidade: "))


    totalFood = precoFood *quantFood
    resultado = f"{totalFood:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    preco = f"{precoFood:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    os.system('cls')
    print("__________________________________________________________")
    print("FACTURA FASTFOOD - CACHORRO - QUENTE")
    print("__________________________________________________________")
    print("FASTFOOD escolhido: ",NomeFood)
    print("Preço: ",preco,' KZS')
    print("Quantidade: ",quantFood)
    print('Total: ',resultado, ' KZS')
    print("__________________________________________________________")

    return totalFood