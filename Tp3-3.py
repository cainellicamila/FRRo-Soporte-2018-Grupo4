'''Ejercico 3
Hacer un programa Python para acceder a la tabla Personas y eliminar el
registro de una persona.'''
import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='soporte')
cur = conn.cursor()

op = ("DELETE FROM persona WHERE idPersona='4'")
cur.execute(op)


cur.execute("SELECT * FROM persona")
for row in cur.fetchall():
    print('Id:{0}, Nombre: {1}, Fecha de nacimiento: {2}, DNI: {3}, Altura: {4} '.format(row[0], row[1], row[2], row[3], row[4]))

conn.commit()
