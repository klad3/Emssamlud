from menus.menu_administracion import MenuAdministracion
import validaciones.validaciones_adm_paciente as v
import entities.paciente as p
import manejo_json.json_config_paciente as jp

class AdministracionPaciente(MenuAdministracion):
    def __init__(self):
        self.validaciones = v.ValidacionAdmPaciente()
        self.json_paciente = jp.JsonConfigPaciente()

    def menu_administracion(self):
        print('Bienvenido a la administración de pacientes')
        print('1. Registrar paciente.')
        print('2. Modificar datos del paciente.')
        print('3. Eliminar paciente.')
        self.opcion_menu_adm = input('Digite una opción: ')
        while not self.validaciones.validar_opcion_menu(self.opcion_menu_adm):
            self.opcion_menu_adm = input('Digite una opción válida: ')

        if int(self.opcion_menu_adm) == 1:
            self.registrar()
        elif int(self.opcion_menu_adm) == 2:
            self.modificar()
        else:
            self.eliminar()
    
    def registrar(self):
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
        
        self.fecha_nacimiento = input('Fecha de nacimiento (Fecha-Mes-Año): ')
        while not self.validaciones.validar_fecha_nacimiento(self.fecha_nacimiento):
            self.fecha_nacimiento = input('Ingrese su fecha de nacimiento en un formato válido (Fecha-Mes-Año): ')

        self.direccion = input('Dirección: ')
        while not self.validaciones.validar_direccion(self.direccion):
            self.direccion = input('Por favor, ingrese su dirección: ')

        self.sexo = input('Sexo (Masculino - M / Femenino - F): ')
        while not self.validaciones.validar_sexo(self.sexo):
            self.sexo = input('Escriba una opción válida (M - F): ')
        
        self.email = input('Email: ')
        while not self.validaciones.validar_email(self.email):
            self.email = input('Escriba un email válido: ')
        
        self.observacion = input('Observación: ')
        while not self.validaciones.validar_observacion(self.observacion):
                self.observacion = input('Ingrese su observación: ')

        self.paciente = p.Paciente(self.dni, self.nombres, self.apellido_paterno, self.apellido_materno,
                                    self.telefono, self.fecha_nacimiento, self.direccion,
                                    self.validaciones.sexo, self.email, self.observacion)

        datos_paciente = [{'dni': self.paciente.dni, 'nombres': self.paciente.nombres,
                        'apellido_paterno': self.paciente.apellido_paterno,
                        'apellido_materno': self.paciente.apellido_materno,
                        'telefono': self.paciente.telefono,
                        'fecha_nacimiento': self.paciente.fecha_nacimiento,
                        'direccion': self.paciente.direccion, 'sexo': self.paciente.sexo,
                        'email': self.paciente.email,
                        'observacion': self.paciente.observacion}]
        
        if self.json_paciente.registrar_json(datos_paciente):
            print('El paciente ha sido registrado correctamente.')
        else:
            print('Error, el paciente ya ha sido registrado.')

    def modificar(self):
        self.dni = input('Digite el DNI del paciente a modificar: ')
        while not self.validaciones.validar_dni(self.dni):
            self.dni = input('Ingrese un DNI válido (8 dígitos): ')

        if self.json_paciente.verificar_paciente_json(self.dni):
            print(f'El paciente de DNI {self.dni} ha sido encontrado, modifique sus datos.')
            self.telefono = input('Número telefónico: ')
            while not self.validaciones.validar_telefono(self.telefono):
                self.telefono = input('Ingrese un número telefónico válido (9 dígitos): ')

            self.direccion = input('Dirección: ')
            while not self.validaciones.validar_direccion(self.direccion):
                self.direccion = input('Por favor, ingrese su dirección: ')

            self.email = input('Email: ')
            while not self.validaciones.validar_email(self.email):
                self.email = input('Escriba un email válido: ')
            
            self.observacion = input('Observación: ')
            while not self.validaciones.validar_observacion(self.observacion):
                self.observacion = input('Ingrese su observación: ')

            self.json_paciente.modificar_json(self.dni, self.telefono, self.direccion, self.email, self.observacion)
        else:
            print('El paciente no ha sido encontrado.')

    def eliminar(self):
        self.dni = input('Digite el DNI del paciente a eliminar: ')
        while not self.validaciones.validar_dni(self.dni):
            self.dni = input('Ingrese un DNI válido (8 dígitos): ')

        if self.json_paciente.verificar_paciente_json(self.dni):
            self.json_paciente.eliminar_json(self.dni)
            print(f'El paciente de DNI {self.dni} ha sido eliminado.')
        else:
            print('El paciente no ha sido encontrado.')