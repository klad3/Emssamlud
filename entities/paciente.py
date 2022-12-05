class Paciente():
    def __init__(self, dni, nombres, apellido_paterno, apellido_materno, telefono, fecha_nacimiento,
                 direccion, sexo, email, observacion):
        self.__dni = dni
        self.__nombres = nombres
        self.__apellido_paterno = apellido_paterno
        self.__apellido_materno = apellido_materno
        self.__telefono = telefono
        self.__fecha_nacimiento = fecha_nacimiento
        self.__direccion = direccion
        self.__sexo = sexo
        self.__email = email
        self.__observacion = observacion

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
    def sexo(self):
        return self.__sexo

    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento

    @property
    def direccion(self):
        return self.__direccion

    @property
    def telefono(self):
        return self.__telefono

    @property
    def email(self):
        return self.__email

    @property
    def observacion(self):
        return self.__observacion