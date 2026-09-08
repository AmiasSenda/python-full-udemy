from database import conectar
id= 2

def listar_foods():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM food where id =%s ",(id,))

    foods = cursor.fetchall()

    for food in foods:
        print(food)

    cursor.close()
    conexao.close()


listar_foods()
print("")