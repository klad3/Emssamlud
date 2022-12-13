import json
from manejo_json.json_config_entities import JsonConfigEntities
import os
import ast


class JsonConfigCita(JsonConfigEntities):
    def __init__(self):
        super().__init__()
        self.json_cita = 'archivos_json/cita.json'

    def registrar_json(self, cita):
        if os.stat(self.json_cita).st_size == 0:
            with open(self.json_cita, 'w', encoding='utf-8') as file:
                json.dump(cita, file, indent=4, ensure_ascii=False)
            return True
        else:
            cita_str = str(cita).replace('[', '').replace(']', '')
            cita_dict = ast.literal_eval(cita_str)

            with open(self.json_cita, 'r+', encoding='utf-8') as file:
                self.cita = json.load(file)
                cita_existe = False

                for p in self.cita:
                    if p['id'] == cita_dict['id']:
                        print(p)
                        cita_existe = True
                        return False

                if not cita_existe:
                    self.cita.append(cita_dict)
                    file.seek(0)
                    json.dump(self.cita, file, indent=4, ensure_ascii=False)
                    return True

    def verificar_cita_json(self, id):
        if os.stat(self.json_cita).st_size == 0:
            return False
        else:
            with open(self.json_cita, encoding='utf-8') as file:
                self.cita = json.load(file)
                cita_existe = False

                for p in self.cita:
                    if p['id'] == id:
                        cita_existe = True

                if cita_existe:
                    return True
                else:
                    return False

    def modificar_json(self, id, fecha_cita, hora):
        with open(self.json_cita, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for i in range(0, len(data)):
            if id == data[i]['id']:
                data[i]['fecha'] = fecha_cita
                data[i]['hora'] = hora

        with open(self.json_cita, 'r+', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def eliminar_json(self, id):
        self.cita_act = []

        with open(self.json_cita, 'r', encoding='utf-8') as file:
            self.cita = json.load(file)

            for p in self.cita:
                if p['id'] == id:
                    pass
                else:
                    self.cita_act.append(p)

        with open(self.json_cita, 'w', encoding='utf-8') as file:
            json.dump(self.cita_act, file, indent=4, ensure_ascii=False)