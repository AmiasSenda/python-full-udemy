from database import conectar
print("REGISTO DE UM NOVO FOOD: ")
print("------------------------------------------")
nome = input("Digite o nome do Food: ")
preco =int(input("Digite o preço: "))
quant = int (input("Digite a quantidade: "))
id = int (input("Digite o id do Food: "))

def add_foods():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute( 
        """ 
        UPDATE  food set descricao = %s  ,preco = %s,quantidade= %s
        where id =%s
        """,
     (nome,preco,quant,id),
    
                )

    conexao.commit()

    cursor.close()
    conexao.close()


add_foods()
print("FastFood alterado com Sucesso!")