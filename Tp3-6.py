'''Hacer un programa Python para acceder a la tabla Personas, que devuelve
todos los registros la tabla en variable JSON, mostrar el resultado.'''

import json
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='soporte')

cur = conn.cursor()

cur.execute("SELECT idPersona, Nombre, DNI, Altura  FROM persona")

for i in cur.fetchall():
    print(json.dumps(i))

cur.close()
