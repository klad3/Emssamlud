from manejo_json.json_config_paciente import JsonConfigPaciente
from manejo_json.json_config_cita import JsonConfigCita
from manejo_json.json_config_personal import JsonConfigPersonal
from manejo_json.json_config_paciente import JsonConfigPaciente
from manejo_json.json_config_reportes import JsonConfigReportes
import entities.reportes as r

class administrar_reportes:
    def __init__(self):
        self.json_cita = JsonConfigCita()
        self.json_paciente = JsonConfigPaciente()
        self.json_personal = JsonConfigPersonal()
        self.json_reporte = JsonConfigReportes()
        
    def atencion_cita(self):
        self.paciente = []
        print("\n-------------Bienvenido a atencion de la cita------------------")
        self.paciente_dni = input("Digite el dni del paciente: ")
        
        if self.json_cita.verificar_json(self.paciente_dni):
            
            self.id = self.json_reporte.asignar_id_json()
            
            print("*****************************************")
            print('Datos: ')
            print(self.mostrar_datos(self.json_paciente.extraer_datos_json(self.paciente_dni)))
            self.peso = input("Ingrese el peso del paciente: ")
            self.talla = input("Ingrese la talla: ")
            self.motivo_cita=input("Motivo de la cita: ")
            self.diagnostico = input("Diagnostico: ")
            
            self.paciente = self.json_paciente.extraer_datos_json(self.paciente_dni)
            self.reporte = r.Reportes(self.id,self.paciente,self.peso,self.talla,self.motivo_cita,self.diagnostico)
            campos_reporte = [{'id':self.reporte.id ,'paciente':self.reporte.paciente, 'peso' :self.peso, 'talla' :self.talla,'motivo_cita': self.motivo_cita,
                        'diagnostico': self.diagnostico}]
        
            if self.json_reporte.registrar_json(campos_reporte):
                print('La cita se atendió correctamente.')
            else:
                print('Error, el paciente ya ha sido registrado.')
            
        else:
            print("No se encontró cita")
            
    def mostrar_datos(self,diccionario):
        for llave, valor in diccionario.items():
            print(llave,":",valor)  