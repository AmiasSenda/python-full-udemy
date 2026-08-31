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
    1: {"nome": "Queijo Extra", "preco": 500},
    2: {"nome": "Bacon Extra", "preco": 800},
    3: {"nome": "Carne Extra", "preco": 1500},
    4: {"nome": "Frango Extra", "preco": 1200},
    5: {"nome": "Salsicha Extra", "preco": 700},
    6: {"nome": "Azeitonas", "preco": 400},
    7: {"nome": "Batata Frita", "preco": 1500},
    8: {"nome": "Nuggets", "preco": 2000}
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