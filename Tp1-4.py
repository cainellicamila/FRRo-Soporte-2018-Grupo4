#4. Escribir una función que tome un carácter y devuelva True si es una vocal, de lo
#contrario devuelve False.

def esvoc(a):
    if a == "a" or a == "e" or a == "i" or a == "o" or a == "u":
        return True
    else:
        return False


a = "g"

print(esvoc(a))

assert esvoc(a) == False
assert esvoc(a) != True

