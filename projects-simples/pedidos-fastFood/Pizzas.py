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
    1: {"nome": "Pizza Margherita", "preco": 4500},
    2: {"nome": "Pizza de Frango", "preco": 5000},
    3: {"nome": "Pizza de Calabresa", "preco": 5500},
    4: {"nome": "Pizza de Presunto e Queijo", "preco": 5000},
    5: {"nome": "Pizza 4 Queijos", "preco": 6000},
    6: {"nome": "Pizza de Pepperoni", "preco": 6000},
    7: {"nome": "Pizza de Atum", "preco": 5500},
    8: {"nome": "Pizza Vegetariana", "preco": 5000}
}


#print(menu[3]["nome"],' | ',menu[3]["preco"])
print("MENU FASTFOOD")
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
print("__________________________________________________________")
print("FACTURA FASTFOOD")
print("__________________________________________________________")

print("FASTFOOD escolhido: ",NomeFood)
print("Preço: ",preco,' KZS')
print("Quantidade: ",quantFood)
print('Total: ',resultado, ' KZS')
print("__________________________________________________________")
print("")