import  copy

from exercicios_produtos import produtos

novos_produtos = [
  {**p, 'preco':round(p['preco']* 1.1,2)} 
  for p in copy.deepcopy(produtos)

                  ]
print('PRODUTOS')
print(*produtos, sep='\n')
print()
print('PRODUTOS COM VALORES ACIMA DE 10%')
print(*novos_produtos, sep='\n')

produto_ordenado_por_nome = sorted (copy.deepcopy(produtos), key=lambda p:p['nome'])
print()
print()
print('PRODUTOS ORDENADOS POE NOME')
print(*produto_ordenado_por_nome, sep='\n')

produto_ordenado_por_preco= sorted (copy.deepcopy(produtos), key=lambda p:p['preco'], reverse=True)
print()
print()
print('PRODUTOS ORDENADOS POR PREÇO')
print(*produto_ordenado_por_preco, sep='\n')