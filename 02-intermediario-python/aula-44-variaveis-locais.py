def concatenar (string_inicial):
    valor_f = string_inicial


    def interna (valor_a_concatenar):
        nonlocal valor_f
        valor_f +=valor_a_concatenar 
        return valor_f
    return interna


c = concatenar ('a')

print(c('b'))
print(c('c'))
print(c('d'))


