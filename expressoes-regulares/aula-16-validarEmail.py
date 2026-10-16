import re
from pprint import pprint

regexEmail = re.compile(r'^\w+(?:[.\-+!%]\w+)*@\w+(?:[.\-]\w+)+$', flags=re.MULTILINE) #Básica

regexEmail1 = re.compile(r'^[^\s@<>\(\)[\]]+(\.[^\s@<>\(\)[\]+)*@\w+(?:[\.\-_]\w+)*$', flags=re.MULTILINE)


emails = '''
amias.senda@gmail.com
joao.silva123@outlook.com
maria.costa@empresa.co.ao
pedro_2026@yahoo.com
ana.santos@dominio.org
ana+1b.santos@dominio.org
lucas.mendes@faci.ao
carla.silva99@hotmail.com
teste.email+python@gmail.com

amias.senda@
joao.silva.com
maria@@gmail.com
pedro silva@gmail.com
ana..silva@gmail.com
joao@dominio..com
'''


pprint(regexEmail.findall(emails))