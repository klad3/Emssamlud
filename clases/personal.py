from abc import ABC, abstractmethod
class Personal(ABC):
    def __init__(self, dni, nombres, apellidos, sexo, fecha_nacimiento, domicilio, telefono, email, disponibilidad):
        self._dni = dni
        self._nombres = nombres
        self._apellidos = apellidos
        self._sexo = sexo
        self._fecha_nacimiento = fecha_nacimiento
        self._domicilio = domicilio
        self._telefono = telefono
        self._email = email
        self._disponibilidad = disponibilidad

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        self._dni = dni

    @property
    def nombres(self):
        return self._nombres

    @nombres.setter
    def nombres(self, nombres):
        self._nombres = nombres

    @property
    def apellidos(self):
        return self._apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self._apellidos = apellidos
    
    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, sexo):
        self._sexo = sexo

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    @property
    def domicilio(self):
        return self._domicilio

    @domicilio.setter
    def domicilio(self, domicilio):
        self._domicilio = domicilio

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def disponibilidad(self):
        return self._disponibilidad

    @disponibilidad.setter
    def disponibilidad(self, disponibilidad):
        self._disponibilidad = disponibilidad

    @abstractmethod
    def atender(self, dni, disponibilidad):
        pass

class Medico(Personal):
    def __init__(self, dni, nombres, apellidos, sexo, fecha_nacimiento, domicilio, telefono, email, disponibilidad, especialidad):
        super().__init__(dni, nombres, apellidos, sexo, fecha_nacimiento, domicilio, telefono, email, disponibilidad)
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
    def __init__(self, dni, nombres, apellidos, sexo, fecha_nacimiento, domicilio, telefono, email, disponibilidad, area):
        super().__init__(dni, nombres, apellidos, sexo, fecha_nacimiento, domicilio, telefono, email, disponibilidad)
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