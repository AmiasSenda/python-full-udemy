#Funções recursivas: são funções que podem se chamar de volta.
#Uteis para dividir problemas grandes em partes menores.


#Toda função recursiva deve ter:
"""
- Um problema a ser dividido em pequenos programas
- Um caso recursivo que resolve um pequeno problema.
- Um caso base que para a recursão
"""


def recursiva (inicio = 0, fim = 10):

    if inicio >= fim:
        return fim
    print(inicio,fim)
    inicio +=1
    return recursiva(inicio,fim)


print(recursiva())