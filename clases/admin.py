from tkinter import messagebox
from tkinter import *

class Admin:
    def __init__(self):
        self.__usuario = 'Admin'
        self.__password = '123'

    def login(self, usuario, password):
        self.accede_sistema = False
        if usuario == self.__usuario and password == self.__password:
            self.accede_sistema = True
        else:
            messagebox.showwarning('Advertencia', 'Usuario y/o contraseña incorrectos')
    
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