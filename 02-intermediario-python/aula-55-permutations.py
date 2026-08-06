from itertools import combinations, permutations

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = [
    'Paulinha','Leonel','Isalino','Daniel'
]

camisetas = [
    'Branca','Azul'
]

print('COMBINAÇÕES')
print_iter(combinations(pessoas,2))
print('PERMUTAÇÕES')
print_iter(permutations(pessoas,2))


