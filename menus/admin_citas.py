from menus.menu_administracion import MenuAdministracion
import menus.menu as menu
import entities.cita as c
from manejo_json.json_config_paciente import JsonConfigPaciente
from manejo_json.json_config_cita import JsonConfigCita
from manejo_json.json_config_personal import JsonConfigPersonal
from validaciones.validaciones_adm_personal import ValidacionPersonal
from validaciones.validaciones_adm_citas import ValidacionAdmCita
from menus.admin_pacientes import AdministracionPaciente

class AdministracionCita(MenuAdministracion):
    def __init__(self):
        self.json_cita = JsonConfigCita()
        self.json_paciente = JsonConfigPaciente()
        self.json_personal = JsonConfigPersonal()
        self.validaciones_cita = ValidacionAdmCita()
        self.validaciones_medico = ValidacionPersonal()
        self.menu_paciente = AdministracionPaciente()

    def menu(self):
        self.repetir_menu = True
        while self.repetir_menu:
            print('Bienvenido a la administración de citas.')
            print('1. Agendar cita médica.')
            print('2. Reprogramar cita médica.')
            print('3. Archivar cita médica.')
            print('4. Volver.')

            self.opcion_menu = input('Digite una opción: ')
            while not self.validaciones_cita.validar_opcion_menu(self.opcion_menu):
                self.opcion_menu = input('Digite una opción válida: ')

            if int(self.opcion_menu) == 1:
                self.registrar()
            elif int(self.opcion_menu) == 2:
                self.modificar()
            elif int(self.opcion_menu) == 3:
                self.eliminar()
            else:
                self.repetir_menu = False
                self.menu_anterior = menu.Menu()
                self.menu_anterior.menu_principal()

    def registrar(self):
        self.paciente = []
        print('Registro cita médica.')

        self.id = self.json_cita.asignar_id_json()

        self.dni_paciente = input('Paciente DNI: ')
        while not self.validaciones_cita.validar_dni(self.dni_paciente):
            self.dni_paciente = input('Ingrese un DNI válido (8 dígitos): ')

        self.fecha_cita = input('Ingrese fecha de la cita (Fecha-Mes-Año): ')
        while not self.validaciones_cita.validar_fecha_cita(self.fecha_cita):
            self.fecha_cita = input('Verifique la fecha ingresada (Plazo máximo = 30 días): ')

        if self.json_paciente.verificar_json(self.dni_paciente):
            self.paciente = self.json_paciente.extraer_datos_json(self.dni_paciente)
            print('Se muestran las áreas disponibles:')
            print('- Cardiología (C)')
            print('- Traumatología (T)')
            print('- Odontología (O)')
            self.area = input('Escriba el área de la cita (C - T - O): ')
            try:
                while not self.validaciones_medico.validar_especialidad(self.area):
                    self.area = input('Escriba un área disponible (C - T - O): ')

                if self.json_personal.verificar_especialidad_json(self.validaciones_medico.especialidad):
                    self.validaciones_cita.mostrar_ordenado(self.json_personal.buscar_datos_json(self.validaciones_medico.especialidad, self.fecha_cita))

                    self.dni_medico = input('Medico DNI: ')
                    while not self.validaciones_cita.validar_dni(self.dni_medico):
                        self.dni_medico = input('Ingrese un DNI válido (8 dígitos): ')

                    if self.json_personal.verificar_json(self.dni_medico):
                        if self.json_personal.verificar_especialidad_medico_json(self.dni_medico, self.validaciones_medico.especialidad):
                            self.medico = self.json_personal.extraer_datos_json(self.dni_medico)


                            self.cita = c.Cita(self.id, self.paciente, self.validaciones_medico.especialidad, self.medico, self.fecha_cita)

                            datos_cita = [{ 'id': self.cita._id, 'paciente': self.cita._paciente, 'area': self.cita._area,
                                                'medico': self.cita._medico, 'fecha_cita': self.cita._fecha_cita, 'activo': True}]

                            self.json_cita.registrar_json(datos_cita)
                            self.json_personal.modificar_citas_disponibles_json(self.dni_medico, self.fecha_cita)
                            print('La cita ha sido registrada correctamente.')
                        else:
                            print(f'El médico con DNI {self.dni_medico} no labora en el área de {self.validaciones_medico.especialidad}.')
                    else:
                        print(f'El médico con DNI {self.dni_medico} no existe.')
            except:
                print('No hay médicos disponibles en el área indicada.')
        else:
            print(f'El paciente con DNI {self.dni_paciente} no existe.')

    def modificar(self):
        self.dni = input("Ingrese el DNI del paciente para la busqueda de sus citas: ")

        if self.json_cita.verificar_json(self.dni):
            print(f'El paciente de DNI {self.dni} cuenta con lo siguiente: ')
            print(self.json_cita.buscar_datos_json(self.dni))
            self.citas = self.json_cita.buscar_datos_json(self.dni)
            self.id = input('Ingrese el ID de la cita a modificar: ')
            while not self.validaciones_cita.validar_id(self.id,self.citas):
                self.id = input('Ingrese un ID válido: ')
            self.area = self.json_cita.buscar_especialidad_json(self.id)
            self.fecha_cita = input('Nueva fecha de la cita: ')
            while not self.validaciones_cita.validar_fecha_cita(self.fecha_cita):
                self.fecha_cita = input('Verifique la fecha ingresada (Plazo máximo = 30 días): ')
            self.validaciones_cita.mostrar_ordenado(self.json_personal.buscar_datos_json(self.area, self.fecha_cita))
            self.medico_dni = input('DNI Médico: ')
            while not self.validaciones_cita.validar_dni(self.medico_dni):
                self.medico_dni = input('Ingrese un DNI válido (8 dígitos): ')
            while not self.json_personal.verificar_json(self.medico_dni):
                self.medico_dni = input('No existe un Médico con el dni escrito, Por favor ingrese un DNI válido (8 dígitos): ')

            self.json_cita.modificar_json(self.id, self.fecha_cita, self.medico_dni)
            print('La cita ha sido modificada con exito')
        else:
            print('Este paciente no tiene citas programadas.')

    def eliminar(self):
        self.dni = input("Ingrese el DNI del paciente para la busqueda de sus citas: ")

        if self.json_cita.verificar_json(self.dni):
            print(f'El paciente de DNI {self.dni} cuenta con lo siguiente: ')
            print(self.json_cita.buscar_datos_json(self.dni))
            self.id = input('Ingrese el ID de la cita a archivar: ')

            self.json_cita.eliminar_json(self.id)
        else:
            print('Este paciente no tiene citas programadas.')

