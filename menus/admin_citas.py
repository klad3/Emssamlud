from menus.menu_administracion import MenuAdministracion
import menus.menu as menu
import entities.cita as c
from manejo_json.json_config_cita import JsonConfigCita

class AdministracionCita(MenuAdministracion):
    def __init__(self):
        self.json_cita = JsonConfigCita()

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
                self.menu_anterior.menu_administracion()

    def registrar(self):
        print('Registro cita médica.')

        self.fecha_cita = input('Fecha: ')

        self.hora = input('Hora: ')

        self.area = input('Area: ')

        self.medico = input('Medico: ')

        self.consultorio = input('Consultorio: ')

        self.paciente_dni = input('Paciente DNI: ')


        self.cita = c.Cita(self.fecha_cita, self.hora, self.area, self.medico, self.consultorio, self.paciente_dni)

        datos_cita = [{ 'fecha_cita': self.cita._fecha_cita, 'hora': self.cita._hora,
                           'area': self.cita._area,
                           'medico': self.cita._medico,
                           'consultorio': self.cita._consultorio, 'paciente_dni': self.cita._paciente_dni}]


        if self.json_cita.registrar_json(datos_cita):
            print('La cita ha sido registrada correctamente.')
        else:
            print('Error, la cita ya fue registrado.')


    def modificar(self):
        pass


    def eliminar(self):
        pass
