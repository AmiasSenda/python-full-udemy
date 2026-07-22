s1 = {1,2,3}
s2 = {2, 4,8,12}
s3 = s1 | s2 #vai unir os dois sets
s4 = s1 & s2 # vai pegar apenas os valores que estão nos dois sets
s5 = s1 ^ s2

print('sets normais: ')
print('set A: ',s1)
print('set B: ',s2)
print()
print("Operadores")
print('set A + set B: ',s3)
print('valores que estão nos dois sets: ',s4)
print(s5)
