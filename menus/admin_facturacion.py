# funcionalidad implementada
from .menu_administracion import MenuAdministracion
from manejo_json.json_config_cita import JsonConfigCita
from validaciones.validaciones_adm_citas import ValidacionAdmCita
from manejo_json.json_config_factura import JsonConfigFactura

class MenuFacturacion(MenuAdministracion):
    def __init__(self):
        self.total = None
        self.area = None
        self.reporte = None
        self.json_cita = JsonConfigCita()
        self.validacion_citas = ValidacionAdmCita()
        self.json_fatura = JsonConfigFactura()

    def menu(self):
        print("\tMenu de facturacion")
        self.registrar()
        
    def registrar(self):
        dni=input("Ingrese el dni del paciente: ")
        while not self.validacion_citas.validar_dni(dni):
            dni=input("Ingrese el dni del paciente: ")
        self.reporte = self.json_cita.buscar_datos_json(dni)
        if len(self.reporte)==0:
            print("No existen citas")
            return
        self.area = self.reporte[0]["area"]
        self.costear()
    
    def costear(self):    
        if self.area == "Cardiología":
            self.total = 45
        elif self.area == "Traumatología":
            self.total = 50
        elif self.area == "Odontología":    
            self.total = 80
        self.ver_factura()
            
    def ver_factura(self):
        print("\tFacturacion")
        print("Nombre del paciente: "+self.reporte[0]["nombre"])
        print("Fecha de cita: "+self.reporte[0]["fecha_cita"])
        print("DNI: "+self.reporte[0]["dni"])
        print("Personal clinico: "+self.reporte[0]["medico"])
        print("Especialidad: "+str(self.area))
        print("Total: "+str(self.total)+" soles")
        self.lista = {"nombre":self.reporte[0]["nombre"],"fecha_cita":self.reporte[0]["fecha_cita"],"dni":self.reporte[0]["dni"],"medico":self.reporte[0]["medico"],"area":str(self.area),"total":str(self.total)}
        self.guardar_factura()

    def guardar_factura(self):
        self.json_fatura.registrar_json(self.lista)

    def modificar(self):
        pass

    def eliminar(self):
        pass
