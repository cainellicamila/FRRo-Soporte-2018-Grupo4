# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from Tp2_4 import Estudiante

def organizar_estudiantes(estu):

    dic = {}
    for e in estu:
        dic[e] = estu.count(e)

    return(dic)

camila = Estudiante ('Camila', 20, 'F', 48,162, 'ISI', 2015, 41, 24)
carolina = Estudiante('Carolina', 21, 'F', 48,162, 'ISI', 2015, 41, 24)
carolina.carrera = 'ISI'
facundo = Estudiante('Facundo', 24, 'M', 88,194, 'ISI', 2012, 41, 15)
victoria = Estudiante('Victoria', 20, 'F', 48,162, 'IQ', 2015, 41, 10)
sofia = Estudiante('Sofia', 26, 'F', 48,162, 'IQ', 2015, 41, 5)
sofia.carrera = 'IQ'

estu = [camila.carrera, carolina.carrera, facundo.carrera, victoria.carrera, sofia.carrera]

d= organizar_estudiantes(estu)

assert d['ISI'] == 3
assert d['IQ'] ==2
assert d['ISI'] != 5
assert d['IQ'] != 3
