salas = [
    ['Amias', 'Daniel','Madalena','Ramos','Emery'],
    ['Eliane','Maria','Ricarda'],
    ['Redwane','Leonel','Isalino',(0,10,20,30,40)]
]

print(salas[2][3][2]) #AQUI CONSIGO PEGAR O NÚMERO 20.

print('Alunos')
for sala in salas:
    for aluno in sala:
        print(aluno)