import psycopg2


def conectar():

    conexao = psycopg2.connect(
        host="localhost",
        database="fastfood",
        user="postgres",
        password="123",
        port="5432"
    )

    print("Conexão realizada com sucesso!")

    return conexao
