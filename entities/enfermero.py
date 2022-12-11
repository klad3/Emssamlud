from .personal_salud import Personal

class Enfermero(Personal):
    def __init__(self, dni, nombres, apellido_paterno, apellido_materno,
                telefono, sexo, disponibilidad, ocupacion, area):
        super().__init__(dni, nombres, apellido_paterno, apellido_materno,
                        telefono,sexo, disponibilidad, ocupacion)
        self.__area = area

    @property
    def area(self):
        return self.__area

    def atender(self, dni, disponibilidad):
        pass

    def asistir_medico(self, dni_enfermero, dni_medico):
        pass