import re
from pprint import pprint

texto = '''
ONLINE   192.168.0.1 GHIJK active
OFFLINE  192.168.0.2 GHIJK inactive
OFFLINE  192.168.0.3 GHIJK active
ONLINE   192.168.0.4 GHIJK active
ONLINE   192.168.0.5 GHIJK inactive
OFFLINE  192.168.0.6 GHIJK active
'''

positiveLOOKHEAD=(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)',texto)) # POSITIVE LOOKHEAD
NegativeLOOKHEAD=(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)',texto))
positiveLOOKHEAD1 = re.findall(r'(?=.*[^in]active).+', texto) 
# pprint(positiveLOOKHEAD1)
print()


PositiveLookBehind = re.findall(r'\w+(?<!OFFLINE)\s+\d+.\d+.\d+.\d+\s+\w+\s+\w+',texto)
PositiveLookBehind2 = re.findall(r'\w+(?<=OFFLINE)\s+\d+.\d+.\d+.\d+\s+\w+\s+\w+',texto)
pprint(PositiveLookBehind)
print()
pprint(PositiveLookBehind2)