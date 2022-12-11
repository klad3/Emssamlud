from validaciones.validaciones_entities import ValidacionEntities


class ValidacionPersonal(ValidacionEntities):
    def __init__(self) -> None:
        self.sexo = None
        self.disponibilidad = None
        self.ocupacion = None
        self.especialidad = None
        self.area = None

    def validar_opcion_menu(self, opcion):
        try:
            int(opcion)
            if int(opcion) >= 1 and int(opcion) <= 3:
                return True
        except:
            return False

    def validar_dni(self, dni):
        try:
            int(dni)
            if len(dni.replace(' ', '')) == 8:
                return True
        except:
            return False

    def validar_nombres(self, nombres):
        if nombres.replace(' ', '').isalnum() and not any(caracter.isdigit() for caracter in nombres):
            return True
        else:
            return False

    def validar_apellido(self, apellido):
        if apellido.replace(' ', '').isalnum() and not any(caracter.isdigit() for caracter in apellido):
            return True
        else:
            return False

    def validar_telefono(self, telefono):
        try:
            int(telefono)
            if len(telefono.replace(' ', '')) == 9:
                return True
        except:
            return False

    def validar_sexo(self, sexo):
        if sexo.replace(' ', '').upper() == 'M' or sexo.replace(' ', '').upper() == 'F':
            if sexo.replace(' ', '').lower() == 'm':
                self.sexo = 'Masculino'
            else:
                self.sexo = 'Femenino'
            return True
        else:
            return False

    def validar_disponibilidad(self, disponibilidad):
        if disponibilidad.replace(' ', '').lower() == 'm' or disponibilidad.replace(' ',
                                                                                    '').lower() == 't' or disponibilidad.replace(
                ' ', '').lower() == 'n':
            if disponibilidad.replace(' ', '').lower() == 'm':
                self.disponibilidad = 'Mañana'
            elif disponibilidad.replace(' ', '').lower() == 't':
                self.disponibilidad = 'Tarde'
            else:
                self.disponibilidad = 'Noche'
            return True
        else:
            return False

    def validar_ocupacion(self, ocupacion):
        if ocupacion.replace(' ', '').lower() == 'm' or ocupacion.replace(' ', '').lower() == 'e':
            if ocupacion.replace(' ', '').lower() == 'm':
                self.ocupacion = 'Médico'
            else:
                self.ocupacion = 'Enfermero'
            return True
        else:
            return False

    def validar_especialidad(self, especialidad):
        if especialidad.replace(' ', '').lower() == 'c' or especialidad.replace(' ',
                                                                                '').lower() == 't' or especialidad.replace(
                ' ', '').lower() == 'o':
            if especialidad.replace(' ', '').lower() == 'c':
                self.especialidad = 'Cardiología'
            elif especialidad.replace(' ', '').lower() == 't':
                self.especialidad = 'Traumatología'
            else:
                self.especialidad = 'Odontología'
            return True
        else:
            return False

    def validar_area(self, area):
        if area.replace(' ', '').lower() == 'p' or area.replace(' ', '').lower() == 's' or area.replace(' ',
                                                                                                        '').lower() == 'e':
            if area.replace(' ', '').lower() == 'p':
                self.area = 'Pediatría'
            elif area.replace(' ', '').lower() == 's':
                self.area = 'Salud Mental'
            else:
                self.area = 'Emergencias'
            return True
        else:
            return False