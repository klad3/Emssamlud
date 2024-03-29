from .validaciones_entities import ValidacionEntities
from datetime import date

class ValidacionAdmPaciente(ValidacionEntities):
    def __init__(self):
        self.sexo = None
    
    def validar_opcion_menu(self, opcion):
        try:
            int(opcion)
            if int(opcion) >= 1 and int(opcion) <= 4:
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
    
    def validar_fecha_nacimiento(self, fecha):
        try:
            fecha_nac = date(int(fecha[6] + fecha[7] + fecha[8] + fecha[9]),
                        int(fecha[3] + fecha[4]),
                        int(fecha[0] + fecha[1]))
            
            if len(fecha) == 10 and fecha_nac <= date.today():
                return True
            else:
                return False
        except:
            return False

    def validar_direccion(self, direccion):
        if len(direccion.replace(' ', '')) == 0:
            return False
        else:
            return True

    def validar_sexo(self, sexo):
        if sexo.replace(' ', '').upper() == 'M' or sexo.replace(' ', '').upper() == 'F':
            if sexo.replace(' ', '').upper() == 'M':
                self.sexo = 'Masculino'
            else:
                self.sexo = 'Femenino'
            return True
        else:
            return False

    def validar_email(self, email):
        try:
            if email.count('@') == 1:
                pass
            else:
                return False
            
            email_separado = email.split('@')
            if email_separado[0][0].replace(' ', '') == '.':
                return False

            if email_separado[1].index('.') > 0:
                indicador_punto_1 = True

            cont_puntos = 0
            for c in email_separado[1]:
                if c == '.':
                    cont_puntos += 1

            if cont_puntos >= 1:
                if len(email_separado[1].split('.')[1]) > 0:
                    indicador_punto_2 = True

            if len(email_separado[0].replace(' ', '')) > 0 and indicador_punto_1 and indicador_punto_2:
                return True
            else:
                return False
        except:
            return False
        
    def validar_observacion(self, observacion):
        if observacion == '':
            return False
        else:
            return True