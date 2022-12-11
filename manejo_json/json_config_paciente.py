import json
from .json_config_entities import JsonConfigEntities
import os
import ast

class JsonConfigPaciente(JsonConfigEntities):
    def __init__(self):
        self.json_paciente = 'archivos_json/paciente.json'

    def registrar_json(self, paciente):
        if os.stat(self.json_paciente).st_size == 0:
            with open(self.json_paciente, 'w', encoding='utf-8') as file:
                json.dump(paciente, file, indent=4, ensure_ascii=False)
            return True
        else:
            paciente_str = str(paciente).replace('[', '').replace(']', '')
            paciente_dict = ast.literal_eval(paciente_str)
            
            with open(self.json_paciente, 'r+', encoding='utf-8') as file:
                self.pacientes = json.load(file)
                paciente_existe = False

                for p in self.pacientes:
                    if p['dni'] == paciente_dict['dni']:
                        paciente_existe = True
                        return False
                
                if not paciente_existe:
                    self.pacientes.append(paciente_dict)
                    file.seek(0)
                    json.dump(self.pacientes, file, indent=4, ensure_ascii=False)
                    return True

    def verificar_paciente_json(self, dni):
        if os.stat(self.json_paciente).st_size == 0:
            return False
        else:
            with open(self.json_paciente, encoding='utf-8') as file:
                self.pacientes = json.load(file)
                paciente_existe = False

                for p in self.pacientes:
                    if p['dni'] == dni:
                        paciente_existe = True
                if paciente_existe:
                    return True
                else:
                    return False

    def modificar_json(self, dni, telefono, direccion, email, observacion):
        with open(self.json_paciente, 'r', encoding='utf-8') as file:
            self.pacientes = json.load(file)

            i = 0
            for p in self.pacientes:
                if p['dni'] == dni:
                    self.pacientes[i]['telefono'] = telefono
                    self.pacientes[i]['direccion'] = direccion
                    self.pacientes[i]['email'] = email
                    self.pacientes[i]['observacion'] = observacion
                i += 1
        
        with open(self.json_paciente, 'r+', encoding='utf-8') as file:
            json.dump(self.pacientes, file, indent=4, ensure_ascii=False)

    def eliminar_json(self, dni):
        self.pacientes_act = []

        with open(self.json_paciente, 'r', encoding='utf-8') as file:
            self.pacientes = json.load(file)

            for p in self.pacientes:
                if p['dni'] == dni:
                    pass
                else:
                    self.pacientes_act.append(p)
        
        with open(self.json_paciente, 'w', encoding='utf-8') as file:
            json.dump(self.pacientes_act, file, indent=4, ensure_ascii=False)