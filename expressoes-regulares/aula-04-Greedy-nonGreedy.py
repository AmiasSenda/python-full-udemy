import re


texto = '''
<p>I'm</p> <p>Bonita com Propósito</p> <p>...</p> <div></div>
'''

print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>',texto))
print(re.findall(r'<[pdiv]{1,3}>.+?<\/[pdiv]{1,3}>',texto)) #SÓ RETORNA COISA COM VALOR.
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>',texto))