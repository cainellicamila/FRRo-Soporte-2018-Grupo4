#6. Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la
#cadena "estoy probando" debería devolver la cadena "odnaborp yotse".

def invertir(a):
       return a[::-1]



a = "estoy probando"
print(invertir(a))

assert (invertir(a) == "odnaborp yotse")
assert (invertir(a)!= "estoy probando")
