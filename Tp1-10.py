#Escribir una función mas_larga() que tome una lista de palabras y devuelva la más
#larga.

def mas_larga (*palabras):
    cant=0
    palmax = ' '
    for n in palabras:

        c=0
        for i in n:
            c = c + 1
        if c > cant:
            cant=c
            palmax=n
    return palmax

print( mas_larga('la', 'palabra', 'más', 'larga') )

assert mas_larga('la', 'palabra', 'más', 'larga') == 'palabra'
assert mas_larga('la', 'palabra', 'más', 'larga') != 'la'
