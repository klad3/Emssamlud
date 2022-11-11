class Medico(Personal):
    def __init__(self, dni, nombres, apellido_paterno, apellido_materno, telefono, ocupacion, sexo, disponibilidad, especialidad):
        super().__init__(dni, nombres, apellido_paterno, apellido_materno, telefono,
        ocupacion, sexo, disponibilidad)
        self.__especialidad = especialidad

    @property
    def especialidad(self):
        return self.__especialidad

    @especialidad.setter
    def especialidad(self, especialidad):
        self.__especialidad = especialidad

    def atender(self, dni, disponibilidad):
        pass

    def diagnosticar(self, dni, diagnostico):
        pass

    def recetar(self, dni, medicamento):
        pass

