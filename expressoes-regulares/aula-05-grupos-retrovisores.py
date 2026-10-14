import re


texto = '''
<p>I'm</p> <p>Bonita com Propósito</p> <p>...</p> <div></div>
'''

print(re.findall(r'<([pdiv]{1,3})>.+?<\/\1>',texto))
print(re.findall(r'(bon)|(def)+',texto,flags=re.I))