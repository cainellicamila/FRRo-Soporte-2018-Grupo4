'''Escribir una clase llamada Persona que cumpla las siguientes condiciones:
 Atributos: nombre, edad, sexo (H hombre, M mujer), peso, altura.
 Métodos:
o es_mayor_edad(): indica si es mayor de edad, devuelve un booleano.
o print_data(): imprime por pantalla toda la información del objeto.
o generar_dni(): genera un número aleatorio de 8 cifras y lo guarda dentro del
atributo DNI. Llamar desde el método __init__, solo una vez.
'''

from random import randint

class Persona :

    def es_mayor_edad(self):
        if self.edad < 18:
            self.mayor = False
        else:
            self.mayor = True
        return self.mayor


    def print_data(self):
        print('Nombre: ', self.nombre)
        print('Sexo: ', self.sexo)
        print('Edad: ', self.edad)
        print('Peso: ', self.peso)
        print('Altura(cm): ', self.altura)
        print('DNI:', self.dni)


    def generar_dni(self):
        self.dni=randint(00000000,99999999)


    def __init__(self, nomb, ed, sex, pe, alt):
        self.nombre=nomb
        self.edad=ed
        self.sexo=sex
        self.peso=pe
        self.altura=alt
        self.generar_dni ()



per = Persona('Facundo', 24, 'M', '88', '194')
print('Esta persona es mayor de edad?:', per.es_mayor_edad())
per.print_data()
assert per.es_mayor_edad()==True
assert per.es_mayor_edad()!= False
