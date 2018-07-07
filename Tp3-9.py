'''Ejercicio 9
Hacer un programa Python para acceder a la tabla Personas y PersonaPeso y
buscar el registro de una persona identificada por su DNI, mostrar los datos de la
persona y de su historial de peso.'''

import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='soporte')

cur = conn.cursor()

dnip= int(input('Ingresar dni de la persona'))

cur.execute('SELECT * FROM persona per inner join pesos pes on per.idPersona=pes.id HAVING dni=%s', dnip)

per=cur.fetchall()

print('Nombre:',per[0][1], '\n Fecha de nacimiento:' ,per[0][2], '\n DNI:',per[0][3], '\n Altura:',per[0][4])
print('Historial de peso:')

for i in per:
    print('\n Fecha:',i[6], '\n Peso:', i[7])
