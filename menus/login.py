from manejo_json.json_config_admin import JsonConfigAdmin
from menus.menu import Menu

class Login():
    def __init__(self):
        self.json_config = JsonConfigAdmin()

    def iniciar_sesion(self):
        self.usuario = input('Digite su usuario: ')
        self.password = input('Digite su contraseña: ')

        while not self.json_config.verificar_datos_adm(self.usuario, self.password):
            print('Usuario y/o contraseña incorrectos.')
            self.usuario = input('Digite su usuario: ')
            self.password = input('Digite su contraseña: ')

        menu = Menu()
        menu.menu_principal()