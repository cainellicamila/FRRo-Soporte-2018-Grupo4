'''Ejercicio 4
Hacer un programa Python para acceder a la tabla Personas y buscar el
registro de una persona identificada por su DNI, mostrar los datos de la persona.'''
import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='soporte')
cur = conn.cursor()


op = ("SELECT * FROM persona WHERE DNI = '37573101'")
cur.execute(op)

row=cur.fetchone()
print('Id:{0}\nNombre:{1}\nFecha Nacimiento:{2}\nDNI:{3}\nAltura:{4}'.format(row[0], row[1], row[2], row[3], row[4]))
cur.close()
