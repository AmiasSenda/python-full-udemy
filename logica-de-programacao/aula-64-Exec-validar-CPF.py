cpf =  '74682489070'
nove_digitos = cpf [:9]
contado_regressivo = 10
resultado = 0
for digito in nove_digitos:
    resultado += (int(digito) * contado_regressivo)
    contado_regressivo -=1

digito = ((resultado * 10) % 11)

digito = digito if digito <= 9 else 0

print(digito)
#SEGUNDA PARTE

deis_digitos = nove_digitos + str(digito)
contador_regressivo1 = 11
resultado2 = 0

for digito2  in deis_digitos:

    resultado2+= int(digito2) +contador_regressivo1
    contador_regressivo1 -= 1

digitoA = ((resultado2 * 10)%11)
digitoA = digitoA if digitoA <= 9 else 0

novo_cpf = f'{nove_digitos}{digito}{digitoA}'
print(novo_cpf)



