class Enfermero(Personal):
    def __init__(self, dni, nombres, apellido_paterno, apellido_materno, telefono, ocupacion, sexo, disponibilidad, area):
        super().__init__(dni, nombres, apellido_paterno, apellido_materno, telefono, ocupacion, sexo, disponibilidad)
        self.__area = area

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area):
        self.__area = area

    def atender(self, dni, disponibilidad):
        pass

    def asistir_medico(self, dni_enfermero, dni_medico):
        pass

