from main import * 

base_datos = Lector()
estudiante1 = Estudiante("Elian",67872)
estudiante2 = Estudiante("Willy",65488)
estudiante3 = Estudiante("Dluz",65147)
estudiante4 = Estudiante("David",60244)

base_datos.addEstudiante(estudiante1)
base_datos.addEstudiante(estudiante2)
base_datos.addEstudiante(estudiante3)
base_datos.addEstudiante(estudiante4)

print(base_datos)