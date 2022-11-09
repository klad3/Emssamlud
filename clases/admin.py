class Admin:
    def __init__(self, nombre, password) -> None:
        self.__nombre = nombre
        self.__password = password

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    #Permite acceder al programa
    def login(self, usuario, password):
        pass
    
    # Se registra al medico en la base de datos
    def registrar_med(self, medico):
        pass

    # Se accede a la base de datos para modificar los datos del medico
    def modificar_med(self, medico):
        pass
    
    # Se accede a la base de datos para eliminar medico
    def eliminar_med(self, medico):
        pass

    # Se registra al enfermero en la base de datos
    def registrar_enf(self, enfermero):
        pass    
    
    # Se accede a la base de datos para modificar los datos del enfermero
    def modificar_enf(self, enfermero):
        pass

    # Se accede a la base de datos para eliminar enfermero
    def eliminar_enf(self, enfermero):
        pass

    # Se registra pacientes en la base de datos
    def registrar_paciente(self, paciente):
        pass    
    
    # Se accede a la base de datos para modificar los datos de los pacientes
    def modificar_paciente(self, paciente):
        pass

    # Se accede a la base de datos para eliminar paciente
    def eliminar_paciente(self, paciente):
        pass
