def fora (x):
    a = x
    def dentro ():
        #print(locals())
        print(dentro.__code__.co_freevars)
        return a
    return dentro


dentro1 = fora(10)
dentro2 = fora(10)

print(dentro1())