from .personal_salud import Personal

class Medico(Personal):
    def __init__(self, dni, nombres, apellido_paterno, apellido_materno,
                telefono, sexo, disponibilidad, ocupacion, especialidad, citas_disponibles):
        super().__init__(dni, nombres, apellido_paterno, apellido_materno,
                        telefono,sexo, disponibilidad, ocupacion)
        self.__especialidad = especialidad
        self.__citas_disponibles = citas_disponibles

    @property
    def especialidad(self):
        return self.__especialidad

    def atender(self, dni, disponibilidad):
        pass

    def diagnosticar(self, dni, diagnostico):
        pass

    def recetar(self, dni, medicamento):
        pass

