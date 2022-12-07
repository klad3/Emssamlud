from manejo_json.json_config import JsonConfig
from menu import Menu

class Login():
    def __init__(self):
        self.json_config = JsonConfig()

    def iniciar_sesion(self):
        self.usuario = input('Digite su usuario: ')
        self.password = input('Digite su contraseña: ')

        while not self.json_config.verificar_datos(self.usuario, self.password):
            print('Usuario y/o contraseña incorrectos.')
            self.usuario = input('Digite su usuario: ')
            self.password = input('Digite su contraseña: ')

        menu = Menu()
        menu.menu_principal()

if __name__=='__main__':
    login = Login()
    login.iniciar_sesion()