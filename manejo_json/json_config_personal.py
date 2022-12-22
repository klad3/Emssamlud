import json
from manejo_json.json_config_entities import JsonConfigEntities
import os
import ast

class JsonConfigPersonal(JsonConfigEntities):
    def __init__(self):
        super().__init__()
        self.json_personal = 'archivos_json/personal.json'

    def registrar_json(self, personal):
        if os.stat(self.json_personal).st_size == 0:
            with open(self.json_personal, 'w', encoding='utf-8') as file:
                json.dump(personal, file, indent=4, ensure_ascii=False)
            return True
        else:
            personal_str = str(personal).replace('[', '').replace(']', '')
            personal_dict = ast.literal_eval(personal_str)

            with open(self.json_personal, 'r+', encoding='utf-8') as file:
                self.personal = json.load(file)
                personal_existe = False

                for p in self.personal:
                    if p['dni'] == personal_dict['dni']:
                        print(p)
                        personal_existe = True
                        return False

                if not personal_existe:
                    self.personal.append(personal_dict)
                    file.seek(0)
                    json.dump(self.personal, file, indent=4, ensure_ascii=False)
                    return True

    def verificar_json(self, dni):
        if os.stat(self.json_personal).st_size == 0:
            return False
        else:
            with open(self.json_personal, encoding='utf-8') as file:
                self.personal = json.load(file)
                personal_existe = False

                for p in self.personal:
                    if p['dni'] == dni:
                        personal_existe = True

                if personal_existe:
                    return True
                else:
                    return False
        
    def verificar_especialidad_json(self, especialidad):
        with open(self.json_personal, 'r', encoding='utf-8') as file:
            data = json.load(file)
        for i in range(0, len(data)):
            if data[i]['especialidad'] == especialidad:
                return True

    def verificar_especialidad_medico_json(self, dni, especialidad):
        with open(self.json_personal, 'r', encoding='utf-8') as file:
            data = json.load(file)
        for i in range(0, len(data)):
            if data[i]['dni'] == dni and data[i]['especialidad'] == especialidad:
                return True

    def extraer_datos_json(self, dni):
        with open(self.json_personal, 'r', encoding='utf-8') as file:
            data = json.load(file)

            for i in range(0, len(data)):
                if dni == data[i]['dni']:
                    nombres = data[i]['apellido_paterno'] +' '+data[i]['apellido_materno'] +', '+data[i]['nombres']

        return nombres

    def buscar_datos_json(self, especialidad, fecha):
        with open(self.json_personal, 'r', encoding='utf-8') as file:
            data = json.load(file)
            medicos = []
            fecha_dia = str(fecha)[0] + str(fecha)[1]
            for i in range(0, len(data)):
                if data[i]['especialidad'] == especialidad and data[i]['ocupacion'] == 'Médico' and int(data[i]['citas_disponibles'][fecha_dia]) >= 1 :
                    dni = data[i]['dni']
                    nombres = data[i]['apellido_paterno'] +' '+data[i]['apellido_materno'] +', '+data[i]['nombres']
                    disponibilidad = data[i]['disponibilidad']

                    medico = {'dni': dni, 'medico': nombres, 'disponibilidad': disponibilidad}
                    medicos.append(medico)
        return medicos

    def modificar_citas_disponibles_json(self, dni, fecha):
        fecha_dia = str(fecha)[0] + str(fecha)[1]
        with open(self.json_personal, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for i in range(0, len(data)):
            if dni == data[i]['dni']:
                citas_disponibles = data[i]['citas_disponibles'][fecha_dia]
                data[i]['citas_disponibles'][fecha_dia] = citas_disponibles - 1

        with open(self.json_personal, 'r+', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def modificar_json(self, dni, telefono, disponibilidad):
        with open(self.json_personal, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for i in range(0, len(data)):
            if dni == data[i]['dni']:
                data[i]['telefono'] = telefono
                data[i]['disponibilidad'] = disponibilidad

        with open(self.json_personal, 'r+', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def eliminar_json(self, dni):
        self.personal_act = []

        with open(self.json_personal, 'r', encoding='utf-8') as file:
            self.personal = json.load(file)

            for p in self.personal:
                if p['dni'] == dni:
                    pass
                else:
                    self.personal_act.append(p)

        with open(self.json_personal, 'w', encoding='utf-8') as file:
            json.dump(self.personal_act, file, indent=4, ensure_ascii=False)