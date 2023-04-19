import csv
files = r"app/files/base_de_datos.csv"

@staticmethod
def buscar_persona(id_buscar):
    with open(files) as file:
        read = csv.DictReader(file, delimiter='\t')
        id_estudiantes = []
        names_estudiantes = []
        contador = 0
        for row in read:
            id_estudiantes.append(row["id"])
            names_estudiantes.append(row["name"])
        for ides in id_estudiantes:
            if id_buscar == ides:
                return names_estudiantes[contador]
            contador += 1
        return False
