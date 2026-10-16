import re
from pprint import pprint

regex = re.compile (r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[\u0020-\u002F\u003A-\u0040\u005B-\u0060\u007B-\u007E]).{12,}$')
regex1 =re.compile (
    r'^'
    r'(?=.*[a-z])'
    r'(?=.*[A-Z])'
    r'(?=.*[0-9])'
    r'(?=.*[ -\/:-@[-`-~])'
    r'.{12,}'
    r'$'
    , flags=re.MULTILINE)

senhas = '''
R7!kP2@vL9#q
123456789012
Mundo@2026Xy
cK5^J8&nD1*F
password1234
H3@mX9#rV2!p
Casa12345678
zT8$wN4!bQ6&
qwerty123456
Teste#2026Ab
amias2026abc
Angola2026Ab
P@ssw0rd1234
'''

pprint (regex1.findall(senhas))