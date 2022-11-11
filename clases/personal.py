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
