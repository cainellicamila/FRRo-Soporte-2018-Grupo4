'''Ejercicio 5
Hacer un programa Python para acceder a la tabla Personas y actualizar los
datos de una persona identificada, mostrar los datos de la persona.
'''

import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='soporte')

cur = conn.cursor()
cur.execute("UPDATE persona SET nombre='Camila Belen' WHERE DNI=%s", 40119128)
cur.execute ("SELECT * FROM persona WHERE DNI=%s", 40119128)
row=cur.fetchone()
print('Id:{0}\nNombre:{1}\nFecha Nacimiento:{2}\nDNI:{3}\nAltura:{4}'.format(row[0], row[1], row[2], row[3], row[4]))
conn.commit()
cur.close()
