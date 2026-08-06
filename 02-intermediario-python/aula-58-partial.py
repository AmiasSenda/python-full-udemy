from functools import partial

def print_iter(iterator):
    print(*list(iterator),sep='\n')
    print()


def aumentar_porcentagem(valor,porcentagem):
    return round(valor*porcentagem,2)

aumentar_10_porcento = partial(aumentar_porcentagem, porcentagem = 1.1)

produtos= [
    {'nome':'Banana', 'preco':350.76},
    {'nome':'Laranja', 'preco':500.66},
    {'nome':'Manga', 'preco':650.70},
    {'nome':'Loengo', 'preco':540.60},
]
novos_produtos = [
    {**p,'preco':aumentar_10_porcento(p['preco'])}
      for p in produtos
]
print()
print_iter(produtos)
print_iter(novos_produtos)