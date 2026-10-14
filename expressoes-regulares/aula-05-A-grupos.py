import re 
nif = '''
005559939LA048
'''


print(re.findall(r'[0-9]{3}',nif))