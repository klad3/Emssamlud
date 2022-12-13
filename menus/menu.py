import validaciones.validaciones_main as v
from menus.admin_pacientes import AdministracionPaciente
from menus.admin_personal import AdministracionPersonal
from menus.admin_citas import AdministracionCita

class Menu:
    def __init__(self):
        self.validaciones = v.ValidacionMain()
        self.admin_pacientes = AdministracionPaciente()
        self.admin_personal = AdministracionPersonal()
        self.admin_citas = AdministracionCita()
    
    def menu_principal(self):
        print('-----------------Sistemas de citas médicas - Emssamlud-----------------')
        print('Bienvenido, administrador.')
        print('1. Administración general.')
        print('2. Agendar cita.')
        print('3. Atender cita.')
        print('4. Reportes.')

        self.opcion_princ = input('Digite una opción: ')
        while not self.validaciones.validar_opcion_princ(self.opcion_princ):
            self.opcion_princ = input('Digite una opción válida: ')

        if int(self.opcion_princ) == 1:
            self.menu_administracion()
        if int(self.opcion_princ) == 2:
            self.admin_citas.menu()

    
    def menu_administracion(self):
        print('Bienvenido a la administración general.')
        print('1. Administrar pacientes.')
        print('2. Administrar personal de salud.')
        self.opcion_admin = input('Digite una opción: ')
        while not self.validaciones.validar_opcion_admin(self.opcion_admin):
            self.opcion_admin = input('Digite una opción válida: ')
        
        if int(self.opcion_admin) == 1:
            self.admin_pacientes.menu()
        elif int(self.opcion_admin) == 2:
            self.admin_personal.menu()