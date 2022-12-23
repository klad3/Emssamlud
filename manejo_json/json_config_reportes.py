import json
from manejo_json.json_config_entities import JsonConfigEntities
import os
import ast
from manejo_json.json_config_personal import JsonConfigPersonal

class JsonConfigReportes(JsonConfigEntities):
    def __init__(self):
        super().__init__()
        self.json_reportes = 'archivos_json/reporte.json'
        self.json_personal = JsonConfigPersonal()

    def registrar_json(self, reportes):
        if os.stat(self.json_reportes).st_size == 0:
            with open(self.json_reportes, 'w', encoding='utf-8') as file:
                json.dump(reportes, file, indent=4, ensure_ascii=False)
            return True
        else:
            cita_str = str(reportes).replace('[', '').replace(']', '')
            cita_dict = ast.literal_eval(cita_str)

            with open(self.json_reportes, 'r+', encoding='utf-8') as file:
                self.reportes = json.load(file)
                self.reportes.append(cita_dict)
                file.seek(0)
                json.dump(self.reportes, file, indent=4, ensure_ascii=False)
                return True

    def asignar_id_json(self):
        contador = 100
        if os.stat(self.json_reportes).st_size != 0:
            with open(self.json_reportes, 'r', encoding='utf-8') as file:
                data = json.load(file)
                contador += len(data)
        reporte_id = 'C' + str(contador)
        return reporte_id
    
    def verificar_json(self, dni):
        if os.stat(self.json_reportes).st_size == 0:
            return False
        else:
            with open(self.json_reportes, encoding='utf-8') as file:
                self.reportes = json.load(file)
                cita_existe = False

                for p in self.reportes:
                    if p['paciente']['dni'] == dni:
                        cita_existe = True

                if cita_existe:
                    return True
                else:
                    return False


    def buscar_datos_json(self, dni):
        with open(self.json_reportes, 'r', encoding='utf-8') as file:
            data = json.load(file)
            citas = []
            for i in range(0, len(data)):
                if data[i]['paciente']['dni'] == dni and data[i]['activo'] == True:
                    id = data[i]['id']
                    fecha_cita = data[i]['fecha_cita']
                    medico = data[i]['medico']


                    reportes = {'id': id, 'fecha_cita': fecha_cita, 'medico': medico}
                    citas.append(reportes)
        return citas

    def buscar_especialidad_json(self, id):
        with open(self.json_reportes, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for i in range(0, len(data)):
                if data[i]['id'] == id:
                    area = data[i]['area']

        return area

    def modificar_json(self, id, fecha_cita, medico_dni):
        pass

    def eliminar_json(self, id):
        pass