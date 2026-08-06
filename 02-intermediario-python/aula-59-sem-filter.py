


def print_iter(iterator):
    print(*list(iterator),sep='\n')
    print()


produtos= [
    {'nome':'Banana', 'preco':350.76},
    {'nome':'Laranja', 'preco':500.66},
    {'nome':'Manga', 'preco':650.70},
    {'nome':'Loengo', 'preco':540.60},
]


novos_produtos = [
    p for p in produtos
    if p['preco'] > 500
]
print()
print_iter(produtos)
print_iter(novos_produtos)