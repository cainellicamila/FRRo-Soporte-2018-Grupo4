'''
Ejercico 8
Hacer un Progrma Python donde pueda insertar registros en PersonaPeso y
que valide que la persona existe y que no existe de esa persona un registro de fecha
posterior al que queremos ingresar.
'''

import pymysql
import datetime
import calendar

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='soporte')

cur = conn.cursor()

idi= int(input('Ingresar id de la persona'))
esta=0

año=int(input('Ingresar año'))
mes=int(input('Ingresar mes'))
dia=int(input('Ingresar día'))
fecha=datetime.date(año,mes,dia)
errorf=0

peso=int(input('Ingresar peso'))

cur.execute('SELECT idPersona FROM persona')

for i in cur.fetchall():
    if idi == i[0]:
        esta=1

if esta==0:
    print('Ese número no correspode a un id existente')

cur.execute('SELECT fecha FROM pesos WHERE id=%s',idi)

for j in cur.fetchall():
    if j[0]>fecha:
        errorf=1

if errorf==1:
    print('La fecha es posterior a una fecha ya ingresada')

if esta==1 and errorf==0:
    f = "insert into pesos values('%d','%s','%d')"
    cur.execute(f%(idi,fecha,peso))

cur.execute ('SELECT * FROM pesos')

conn.commit()
cur.close()
conn.close()

