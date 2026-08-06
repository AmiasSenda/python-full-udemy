from itertools import product


def print_iter (iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = [
    'António', 'Saniela','Gabriela','Leonard'
]

camisetas = [
    ['branca', 'Castanha'],
    [
        'p','m','g'
    ],
    ['Masculino','Femenino','UniSex'],
    [
        'algodão','Jeans','linho'
    ]
]


print_iter (product(*camisetas))