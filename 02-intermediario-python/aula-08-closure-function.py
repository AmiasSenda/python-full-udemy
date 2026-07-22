def criar_saud(saudacao,nome):
    def saudar ():
        return saudacao,nome,'!'
    return saudar


s1 = criar_saud('bom dia','Maria')
s2 = criar_saud('Boa noite','Ana')

print(s1())
print(s2())