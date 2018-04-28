'''
15. Reescribe el programa que pide al usuario una lista de números e
imprime en pantalla el máximo y mínimo de los números introducidos al final,
cuando el usuario introduce “fin”. Escribe ahora el programa de modo que almacene
los números que el usuario introduzca en una lista y usa las funciones Max ()
y min () para calcular los números máximo y mínimo después de que el bucle
termine.
Introduzca un número: 6
Introduzca un número: 2
Introduzca un número: 9
Introduzca un número: 3
Introduzca un número: 5
Introduzca un número: fin
Maximo: 9.0
Mínimo: 2.
'''


list = []
a = input('Ingrese valor o \'fin\' para finalizar')
while a != 'fin':
    list.append(float (a))
    a=input('Ingrese valor o \'fin\' para finalizar');
print(list)
print('El maximo es', max(list))
print('El minimo es', min(list))
