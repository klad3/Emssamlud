from menus.menu_administracion import MenuAdministracion
import menus.menu as menu
import validaciones.validaciones_adm_personal as v
import entities.medico as m
import entities.enfermero as e
from manejo_json.json_config_personal import JsonConfigPersonal

class AdministracionPersonal(MenuAdministracion):
    def __init__(self):
        self.validaciones = v.ValidacionPersonal()
        self.json_personal = JsonConfigPersonal()

    def menu(self):
        self.repetir_menu = True
        while self.repetir_menu:
            print('Bienvenido a la administración del personal.')
            print('1. Registrar personal de salud.')
            print('2. Modificar personal de salud.')
            print('3. Eliminar personal de salud.')
            print('4. Volver.')
            
            self.opcion_menu = input('Digite una opción: ')
            while not self.validaciones.validar_opcion_menu(self.opcion_menu):
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
                self.menu_anterior.menu_administracion()

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
            self.citas_disponibles = {"1": 5, "2": 5, "3": 5, "4": 5, "5": 5, "6": 5, "7": 5, "8": 5, "9": 5, "10": 5,
                                      "11": 5, "12": 5, "13": 5, "14": 5, "15": 5, "16": 5, "17": 5, "18": 5, "19": 5,
                                      "20": 5, "21": 5, "22": 5, "23": 5, "24": 5, "25": 5, "26": 5, "27": 5, "28": 5,
                                      "29": 5, "30": 5, "31": 5}
            self.personal = m.Medico(self.dni, self.nombres, self.apellido_paterno,
                                     self.apellido_materno, self.telefono, self.validaciones.sexo,
                                     self.validaciones.disponibilidad, self.validaciones.ocupacion,
                                     self.validaciones.especialidad,self.citas_disponibles)
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
            datos_personal[0].update(especialidad=self.personal.especialidad,citas_disponibles=self.citas_disponibles)
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

        if self.json_personal.verificar_json(self.dni):
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

        if self.json_personal.verificar_json(self.dni):
            self.json_personal.eliminar_json(self.dni)
            print(f'El personal de salud de DNI {self.dni} ha sido eliminado.')
        else:
            print('El personal de salud no ha sido encontrado.')
        pass
