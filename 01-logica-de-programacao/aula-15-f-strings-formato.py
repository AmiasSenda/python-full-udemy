a = 'AXXXXXXXXXX'
b = 'BGGGGGGGGGG'
c = 1.1

string = 'a={} b={} c={:.2f}'
formato = string.format(a, b, c)

#Ao utilizar o índice do farmat, dá um erro.

print(formato)