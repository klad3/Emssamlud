import json
from manejo_json.json_config_entities import JsonConfigEntities
import os
import ast
from manejo_json.json_config_personal import JsonConfigPersonal

class JsonConfigCita(JsonConfigEntities):
    def __init__(self):
        super().__init__()
        self.json_cita = 'archivos_json/cita.json'
        self.json_personal = JsonConfigPersonal()

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
                self.cita.append(cita_dict)
                file.seek(0)
                json.dump(self.cita, file, indent=4, ensure_ascii=False)
                return True

    def verificar_json(self, dni):
        if os.stat(self.json_cita).st_size == 0:
            return False
        else:
            with open(self.json_cita, encoding='utf-8') as file:
                self.cita = json.load(file)
                cita_existe = False

                for p in self.cita:
                    if p['paciente']['dni'] == dni:
                        cita_existe = True

                if cita_existe:
                    return True
                else:
                    return False

    def asignar_id_json(self):
        contador = 100
        if os.stat(self.json_cita).st_size != 0:
            with open(self.json_cita, 'r', encoding='utf-8') as file:
                data = json.load(file)
                contador += len(data)
        cita_id = 'C' + str(contador)
        return cita_id

    def buscar_datos_json(self, dni):
        with open(self.json_cita, 'r', encoding='utf-8') as file:
            data = json.load(file)
            citas = []
            for i in range(0, len(data)):
                if data[i]['paciente']['dni'] == dni:
                    id = data[i]['id']
                    fecha_cita = data[i]['fecha_cita']
                    medico = data[i]['medico']


                    cita = {'id': id, 'fecha_cita': fecha_cita, 'medico': medico}
                    citas.append(cita)
        return citas

    def buscar_especialidad_json(self, id):
        with open(self.json_cita, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for i in range(0, len(data)):
                if data[i]['id'] == id:
                    area = data[i]['area']

        return area

    def modificar_json(self, id, fecha_cita, medico_dni):
        self.cita_act = []
        medico = self.json_personal.extraer_datos_json(medico_dni)
        with open(self.json_cita, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for i in range(0, len(data)):
            if id == data[i]['id']:
                data[i]['fecha_cita'] = fecha_cita
                data[i]['medico'] = medico
                self.cita_act.append(data[i])
            else:
                self.cita_act.append(data[i])

            with open(self.json_cita, 'w', encoding='utf-8') as file:
                json.dump(self.cita_act, file, indent=4, ensure_ascii=False)

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