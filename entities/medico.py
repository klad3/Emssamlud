class Medico:
    def __init__(self, dni, nombres, apellido_paterno, apellido_materno,
                telefono, sexo, disponibilidad, especialidad, citas_disponibles):
        self.__dni = dni
        self.__nombres = nombres
        self.__apellido_paterno = apellido_paterno
        self.__apellido_materno = apellido_materno
        self.__telefono = telefono
        self.__sexo = sexo
        self.__disponibilidad = disponibilidad
        self.__especialidad = especialidad
        self.__citas_disponibles = citas_disponibles

    @property
    def dni(self):
        return self.__dni
    
    @property
    def nombres(self):
        return self.__nombres
    
    @property
    def apellido_paterno(self):
        return self.__apellido_paterno
    
    @property
    def apellido_materno(self):
        return self.__apellido_materno

    @property
    def telefono(self):
        return self.__telefono
    
    @property
    def sexo(self):
        return self.__sexo

    @property
    def disponibilidad(self):
        return self.__disponibilidad

    @property
    def especialidad(self):
        return self.__especialidad
    
    @property
    def citas_disponibles(self):
        return self.__citas_disponibles