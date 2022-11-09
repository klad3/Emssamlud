class Paciente:
    def __init__(self, dni, nombres, apellidos, sexo, fecha_nacimiento, domicilio, telefono, email, obs) -> None:
        self.__dni = dni
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__sexo = sexo
        self.__fecha_nacimiento = fecha_nacimiento
        self.__domicilio = domicilio
        self.__telefono = telefono
        self.__email = email
        self.__obs = obs

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    @property
    def nombres(self):
        return self.__nombres

    @nombres.setter
    def nombres(self, nombres):
        self.__nombres = nombres      

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self.__apellidos = apellidos
    
    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo):
        self.__sexo = sexo

    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento

    @property
    def domicilio(self):
        return self.__domicilio

    @domicilio.setter
    def domicilio(self, domicilio):
        self.__domicilio = domicilio

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, telefono):
        self.__telefono = telefono

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def obs(self):
        return self.__obs

    @obs.setter
    def obs(self, obs):
        self.__obs = obs      