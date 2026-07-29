def divide (n,d):
    if d == 0:
        raise ZeroDivisionError ('Você não pode dividir um número por Zero!')
    else:
        return n/d

print(divide(8,0))
    