import json

class JsonConfig:
    def __init__(self):
        self.json_admin = None

    def verificar_datos(self, usuario, password):
        with open('archivos_json/usuario.json') as file:
            self.datos = json.load(file)
            #print(self.datos)
        for u in self.datos['usuarios']:
            if u['usuario'] == usuario and u['password'] == password:
                print(u)
                #print('Datos correctos.')
                return True
            else:
                print(u)
                #print('Datos incorrectos.')

if __name__ == '__main__':
    config = JsonConfig()
    config.verificar_datos('Admin', '123')
    config.verificar_datos('Paciente', ':c')