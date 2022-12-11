from menus.menu_administracion import MenuAdministracion
import validaciones.validaciones_adm_personal as v
import entities.medico as m
import entities.enfermero as e
from manejo_json.json_config_personal import JsonConfigPersonal


class AdministracionPersonal(MenuAdministracion):
    def __init__(self):
        self.validaciones = v.ValidacionPersonal()
        self.json_personal = JsonConfigPersonal()

    def menu(self):
        print('Bienvenido a la administración del personal.')
        print('1. Registrar personal de salud.')
        print('2. Modificar personal de salud.')
        print('3. Eliminar personal de salud.')
        self.opcion_menu = int(input('Digite una opción: '))
        while not self.validaciones.validar_opcion_menu(self.opcion_menu):
            self.opcion_menu = int(input('Digite una opción válida: '))
        if self.opcion_menu == 1:
            self.registrar()
        elif self.opcion_menu == 2:
            self.modificar()
        else:
            self.eliminar()


    def registrar(self):
        print('Registro del personal de salud.')
        self.dni = input('DNI: ')
        while not self.validaciones.validar_dni(self.dni):
            self.dni = input('Ingrese un DNI válido (8 dígitos): ')

        self.nombres = input('Nombres: ')
        while not self.validaciones.validar_nombres(self.nombres):
            self.nombres = input('Caracteres inválidos, escriba sus nombres: ')

        self.apellido_paterno = input('Apellido paterno: ')
        while not self.validaciones.validar_apellido(self.apellido_paterno):
            self.apellido_paterno = input('Caracteres inválidos, escriba su apellido: ')

        self.apellido_materno = input('Apellido materno: ')
        while not self.validaciones.validar_apellido(self.apellido_materno):
            self.apellido_materno = input('Caracteres inválidos, escriba su apellido: ')

        self.telefono = input('Número telefónico: ')
        while not self.validaciones.validar_telefono(self.telefono):
            self.telefono = input('Ingrese un número telefónico válido (9 dígitos): ')

        self.sexo = input('Sexo (Masculino - M / Femenino - F): ')
        while not self.validaciones.validar_sexo(self.sexo):
            self.sexo = input('Escriba una opción válida (M - F): ')

        self.disponibilidad = input('Disponibilidad (Mañana (M) / Tarde (T) / Noche (N): ')
        while not self.validaciones.validar_disponibilidad(self.disponibilidad):
            self.disponibilidad = input('Escriba una opción válida (M - T - N): ')

        self.ocupacion = input('Ocupacion (Medico (M) / Enfermero (E)): ')
        while not self.validaciones.validar_ocupacion(self.ocupacion):
            self.ocupacion = input('Escriba su ocupacion correctamente (M - E): ')

        if self.ocupacion.replace(' ', '').lower() == 'm':
            self.es_medico = True
            print('Se muestran las especialidades disponibles:')
            print('- Cardiología (C)')
            print('- Traumatología (T)')
            print('- Odontología (O)')
            self.especialidad = input('Escriba su especialidad (C - T - O): ')
            while not self.validaciones.validar_especialidad(self.especialidad):
                self.especialidad = input('Escriba una especialidad disponible (C - T - O): ')

            self.personal = m.Medico(self.dni, self.nombres, self.apellido_paterno,
                                     self.apellido_materno, self.telefono, self.validaciones.sexo,
                                     self.validaciones.disponibilidad, self.validaciones.ocupacion,
                                     self.validaciones.especialidad)
        else:
            self.es_medico = False
            print('Se muestran las áreas de enfermería disponibles:')
            print('- Pediatría (P)')
            print('- Salud Mental (S)')
            print('- Emergencias (E)')
            self.area = input('Escriba el área al que pertenece (P - S - E): ')
            while not self.validaciones.validar_area(self.area):
                self.area = input('Escriba un área disponible (P - S - E): ')

            self.personal = e.Enfermero(self.dni, self.nombres, self.apellido_paterno,
                                        self.apellido_materno, self.telefono, self.validaciones.sexo,
                                        self.validaciones.disponibilidad, self.validaciones.ocupacion,
                                        self.validaciones.area)

        datos_personal = [{'dni': self.personal._dni, 'nombres': self.personal._nombres,
                           'apellido_paterno': self.personal._apellido_paterno,
                           'apellido_materno': self.personal._apellido_materno,
                           'telefono': self.personal._telefono, 'sexo': self.personal._sexo,
                           'disponibilidad': self.personal._disponibilidad,
                           'ocupacion': self.personal._ocupacion}]

        if self.es_medico:
            datos_personal[0].update(especialidad=self.personal.especialidad)
        else:
            datos_personal[0].update(area=self.personal.area)

        if self.json_personal.registrar_json(datos_personal):
            print('El personal de salud ha sido registrado correctamente.')
        else:
            print('Error, el personal de salud ya ha sido registrado.')


    def modificar(self):
        self.dni = input("Ingrese el DNI para la busqueda: ")
        while not self.validaciones.validar_dni(self.dni):
            self.dni = input('Ingrese un DNI válido (8 dígitos): ')

        if self.json_personal.verificar_personal_json(self.dni):
            print(f'El personal de salud de DNI {self.dni} ha sido encontrado, modifique sus datos.')
            self.telefono = input('Número telefónico: ')
            while not self.validaciones.validar_telefono(self.telefono):
                self.telefono = input('Ingrese un número telefónico válido (9 dígitos): ')

            self.disponibilidad = input('Disponibilidad (Mañana (M) / Tarde (T) / Noche (N): ')
            while not self.validaciones.validar_disponibilidad(self.disponibilidad):
                self.disponibilidad = input('Escriba una opción válida (M - T - N): ')

            self.json_personal.modificar_json(self.dni, self.telefono, self.validaciones.disponibilidad)
        else:
            print('El personal de salud no ha sido encontrado.')


    def eliminar(self):
        self.dni = input('Digite el DNI del paciente a eliminar: ')
        while not self.validaciones.validar_dni(self.dni):
            self.dni = input('Ingrese un DNI válido (8 dígitos): ')

        if self.json_personal.verificar_personal_json(self.dni):
            self.json_personal.eliminar_json(self.dni)
            print(f'El personal de salud de DNI {self.dni} ha sido eliminado.')
        else:
            print('El personal de salud no ha sido encontrado.')
        pass
