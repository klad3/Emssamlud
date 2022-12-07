import validaciones.validaciones as v
class Menu:
    def __init__(self):
        self.validaciones = v.Validacion()
    
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
    
    def menu_administracion(self):
        print('Bienvenido a la administración general.')
        print('1. Adminitrar pacientes.')
        print('2. Administrar personal de salud.')
        self.opcion_admin = input('Digite una opción: ')
        while not self.validaciones.validar_opcion_admin(self.opcion_admin):
            self.opcion_admin = input('Digite una opción válida: ')
        

if __name__ == '__main__':
    menu = Menu()
    menu.menu_principal()