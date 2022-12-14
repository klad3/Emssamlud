from menus.menu_administracion import MenuAdministracion
import menus.menu as menu
import entities.cita as c
from manejo_json.json_config_paciente import JsonConfigPaciente
from manejo_json.json_config_cita import JsonConfigCita
from manejo_json.json_config_personal import JsonConfigPersonal

class AdministracionCita(MenuAdministracion):
    def __init__(self):
        self.json_cita = JsonConfigCita()
        self.json_paciente = JsonConfigPaciente()
        self.json_personal = JsonConfigPersonal()

    def menu(self):
        self.repetir_menu = True
        while self.repetir_menu:
            print('Bienvenido a la administración de citas.')
            print('1. Registrar cita médica.')
            print('2. Modificar cita médica.')
            print('3. Eliminar cita médica.')
            print('4. Volver.')

            self.opcion_menu = input('Digite una opción: ')
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

        self.dni = input('Paciente DNI: ')

        self.paciente = self.json_paciente.extraer_datos_json(self.dni)

        self.area = input('Area: ')

        print(self.json_personal.buscar_datos_json(self.area))

        self.medico_dni = input('Medico DNI: ')

        self.medico = self.json_personal.extraer_datos_json(self.medico_dni)

        self.fecha_cita = input('Fecha: ')


        self.cita = c.Cita(self.id, self.paciente, self.area, self.medico, self.fecha_cita)



        datos_cita = [{ 'id': self.cita._id, 'paciente': self.cita._paciente, 'area': self.cita._area,
                           'medico': self.cita._medico, 'fecha_cita': self.cita._fecha_cita}]


        self.json_cita.registrar_json(datos_cita)
        print('La cita ha sido registrada correctamente.')


    def modificar(self):
        pass

    def eliminar(self):
        pass
