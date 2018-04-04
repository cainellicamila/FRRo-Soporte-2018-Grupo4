#7. Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras
#que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar")
#tendría que devolver True.

def es_palindromo(c):
    if (c==c[::-1]):
        return True
    else:
        return False


a="radar"
print (es_palindromo(a))

assert (es_palindromo(a)== True)
assert (es_palindromo(a)!= False)

b="hola"
print (es_palindromo(b))

assert (es_palindromo(b)!= True)
assert (es_palindromo(b)== False)
