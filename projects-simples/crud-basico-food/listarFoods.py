from database import conectar


def listar_foods():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM food")

    foods = cursor.fetchall()

    for food in foods:
        print(food)

    cursor.close()
    conexao.close()


listar_foods()
print("")