"""
Refatorar: editar o seu código.

Ao definir uma função, os parâmetros podem ter valores padrão.
Caso não for enviado nenhum valor ao parâmetro, o valor padrão vai ser o valor a ser utilizado.
"""

def soma (a,b,c = None):
    if c is not None:
        print(a+b+c)
    else:
        print(a+b)

soma(2,2)
soma(3,2,3)
