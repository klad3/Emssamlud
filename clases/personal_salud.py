from abc import ABC, abstractmethod
class Personal(ABC):
    def __init__(self, dni, nombres, apellido_paterno, apellido_materno, telefono,
    ocupacion, sexo, disponibilidad):
        self._dni = dni
        self._nombres = nombres
        self._apellido_paterno = apellido_paterno
        self._apellido_materno = apellido_materno
        self._telefono = telefono
        self._ocupacion = ocupacion
        self._sexo = sexo
        self._disponibilidad = disponibilidad

    @abstractmethod
    def atender(self, dni, disponibilidad):
        pass

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