from .json_config_entities import JsonConfigEntities
import os
import json
import ast

class JsonConfigFactura(JsonConfigEntities):
    def __init__(self):
        super().__init__()
        self.json_factura = 'archivos_json/factura.json'

    def registrar_json(self, factura):
        if os.stat(self.json_factura).st_size == 0:
            with open(self.json_factura, 'w', encoding='utf-8') as file:
                json.dump(factura, file, indent=4, ensure_ascii=False)
            return True
        else:
            factura_str = str(factura).replace('[', '').replace(']', '')
            factura_dict = ast.literal_eval(factura_str)

            with open(self.json_factura, 'r+', encoding='utf-8') as file:
                self.factura = json.load(file)
                self.factura.append(factura_dict)
                file.seek(0)
                json.dump(self.factura, file, indent=4, ensure_ascii=False)

    def verificar_json(self, id):
        pass

    def modificar_json(self, **kwargs):
        pass

    def eliminar_json(self, id):
        pass
    