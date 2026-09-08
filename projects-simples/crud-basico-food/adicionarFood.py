from database import conectar
print("REGISTO DE UM NOVO FOOD: ")
print("------------------------------------------")
nome = input("Digite o nome do Food: ")
preco =int(input("Digite o preço: "))
quant = int (input("Digite a quantidade: "))

def add_foods():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute( 
        """ 
        INSERT INTO food (descricao,preco,quantidade)
        VALUES (%s,%s,%s) 
        """,
     (nome,preco,quant),
    
                )

    conexao.commit()

    cursor.close()
    conexao.close()


add_foods()
print("Registado com sucesso!")