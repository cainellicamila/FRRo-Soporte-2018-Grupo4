'''
Programe una clase ejercicio que tiene los siguientes metodos:
inicio: se le pasa una fecha y devuelve el primero de julio anterior
fin: se le pasa una fecha y devuelve el 30 de junio proximo
semana: devuelve el numero de semana contando a partir del 1 de julio anterior
'''

import datetime
import calendar

class Ejercicio:

    def __init__(self, fecha):
        self.fecha=fecha

    def inicio (self):
        if (self.fecha.month < 7):
            año= (self.fecha.year - 1)
        else:
            año = (self.fecha.year)

        fsalida= datetime.datetime(año,7,1)
        print('1 de julio anterior: %s/%s/%s' %(fsalida.day, fsalida.month, fsalida.year))

    def fin (self):
        if self.fecha.month>6:
            año= (self.fecha.year + 1)
        else:
            año= (self.fecha.year)

        fsalida= datetime.datetime(año,6,30)

        print ('30 de junio próximo: %s/%s/%s' %(fsalida.day, fsalida.month, fsalida.year))

    def semana (self):

       if self.fecha.month < 7:
            año=(self.fecha.year - 1)

            f1= (self.fecha.isocalendar()) #numero de semana actual
            ffinaño= datetime.datetime(año,1,1)
            f3= (ffinaño.isocalendar())  #fin de año
            fsalida = datetime.datetime(año,7,1)
            f2= (fsalida.isocalendar()) #numero de semana 1 julio anterior
            #print(f1[1], f2[1], f3[1])
            cantsem= ((f3[1]-f2[1])+(f1[1]))

       else:
            año = (self.fecha.year)
            fsalida = datetime.datetime(año,7,1)
            f1= (self.fecha.isocalendar()) #numero de semana actual
            f2= (fsalida.isocalendar()) #numero de semana 1 julio anterior
            #print(f1[1], f2[1])
            cantsem= (f1[1]-f2[1])

       print('Numero de semana contando a partir del 1 de julio anterior:', cantsem)

ej = Ejercicio(datetime.datetime(2017,2,1))
eje= Ejercicio(datetime.datetime(2017,11,22))

ej.inicio()
ej.fin()
ej.semana()

eje.inicio()
eje.fin()
eje.semana()

