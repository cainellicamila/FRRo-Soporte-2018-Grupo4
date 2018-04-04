#9. Definir una función generar_n_caracteres() que tome un entero n y devuelva el
#caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería
#devolver "xxxxx".


def generar_n_caracteres(n, c):
    nueva=c*n
    return nueva

a="x"
b=5
print(generar_n_caracteres(b,a))

assert (generar_n_caracteres(a,b) == "xxxxx")
assert (generar_n_caracteres(a,b) != "x")
