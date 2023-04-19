class Estudiante:
    def __init__(self, nombre, identificacion):
        if not isinstance(identificacion, int):
            raise ValueError("La identificación debe ser un entero")
        if not (10000 <= identificacion <= 99999):
            raise ValueError("La identificación debe ser un entero de 5 dígitos")
        self.nombre = nombre
        self.identificacion = identificacion
        
    def __repr__(self) -> str:
        return f"{self.nombre}: {self.identificacion}"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __hash__(self) -> int:
        return hash(str(self))

class Lector:
    def __init__(self):
        self.__base_de_datos = dict()
    
    def __str__(self) -> str:
        return str(self.__base_de_datos)
    
    def buscarDato(self, dato_buscar):
        return self.__base_de_datos.get(dato_buscar)
    
    def verNombre(self):
        return list(self.__base_de_datos.keys())
    
    def verIdenti(self):
        return list(self.__base_de_datos.values())
    
    def addEstudiante(self, estudiante_nuevo):
        if self.buscarDato(estudiante_nuevo) is None or self.buscarDato(estudiante_nuevo) == set():
                self.__base_de_datos[estudiante_nuevo.nombre] = estudiante_nuevo.identificacion
        
    def añadir_persona(self, persona):
        datos = self.buscarDato(persona)
        if self.esta_vacio:
            return None
        else:
            dict[persona.nombre]=persona.identificacion
    
    # def verificar_identificacion(self, persona):
    #     for personas in self.base_de_datos():
    #     if persona.identificacion in self.base_de_datos:
    #         return True
    #     else:
    #         return False