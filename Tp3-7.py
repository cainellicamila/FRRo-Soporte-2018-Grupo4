'''
Ejercicio 7
Crear un tabla relacionada con Persona para guardar su peso corporal en una
fecha , PersonaPeso IdPersona Int() , Fecha Date() , Peso Int.
'''

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='soporte')

cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS Pesos (  `id` INT NOT NULL,`Fecha` DATE NULL,`Peso` INT NULL, PRIMARY KEY (`id`, `fecha`),CONSTRAINT `id` FOREIGN KEY (`id`) REFERENCES `soporte`.`persona` (`idPersona`) ON DELETE NO ACTION ON UPDATE NO ACTION)')

i='INSERT into pesos VALUES (2, "2018-05-03", 47)'
cur.execute(i)
cur.execute('SELECT * FROM pesos')
for i in cur.fetchall():
    print(i)

conn.commit()
cur.close()
conn.close()
