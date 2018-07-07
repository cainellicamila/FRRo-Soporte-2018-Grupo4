'''Ejercicio 2
Hacer un programa Python para acceder a la tabla Personas e insertar en la
un registro de una persona.'''
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='soporte')

caux = ("INSERT INTO persona(idPersona, Nombre, FechaNacimiento, DNI, Altura) VALUES (%s,%s,%s,%s,%s)")
datos = (4, 'Maria', '19960926', '40578554', '170')

cur = conn.cursor()
cur.execute(caux, datos)

cur.execute("SELECT * FROM persona")
for row in cur.fetchall():
    print('Id:{0}, Nombre: {1}, Fecha de nacimiento: {2}, DNI: {3}, Altura: {4} '.format(row[0], row[1], row[2], row[3], row[4]))

conn.commit()
