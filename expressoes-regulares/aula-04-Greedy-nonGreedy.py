import re


texto = '''
<p>I'm</p>
 <p>Bonita com Propósito</p>
<p>Texto 03</p> 
   <div></div>
'''



print(re.findall(r'<[pdiv]{1,3}>',texto)) # PEGA AS TAGS.
print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>',texto)) # PEGA TUDO.
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>',texto)) # PEGA O MÍNIMODE INFORMAÇÃO POSSÍVEL.
print(re.findall(r'<[pdiv]{1,3}>.+?<\/[pdiv]{1,3}>',texto)) # RETORNA APENAS SE TIVER UMA DETERMINADA COISA.

