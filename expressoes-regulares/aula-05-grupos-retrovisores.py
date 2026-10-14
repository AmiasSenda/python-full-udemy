import re
from pprint import pprint


texto = '''
<p>I'm</p> <p>Bonita com Propósito</p> <p>...</p> <div></div>
'''

print(re.findall(r'<([pdiv]{1,3})>(?:.+?)<\/\1>',texto))
tags =re.findall(r'(<([pdiv]{1,3})>(.+?)<\/\2>)',texto)
# print(re.findall(r'(bon)|(to)+',texto,flags=re.I))


for tag in tags:
    um,dois,tres = tag
    print(tres)

# print(tags)


print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)',r'\1 \3 \4',texto))