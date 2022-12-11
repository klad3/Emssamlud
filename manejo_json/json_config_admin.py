import json

class JsonConfigAdmin:
    def verificar_datos_adm(self, usuario, password):
        with open('archivos_json/usuario.json') as file:
            self.datos = json.load(file)
        
        for u in self.datos:
            if u['usuario'] == usuario and u['password'] == password:
                return True
            else:
                return False