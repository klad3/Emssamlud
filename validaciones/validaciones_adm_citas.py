from datetime import date, timedelta

class ValidacionAdmCita:
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

    def mostrar_ordenado(self, lista):
        if lista is not None:
            print(len(lista), " médico(s) disponible(s):")
            for i in lista:
                print("\t________________________________________________________________________________________________")
                print(f"\t DNI: {i['dni']}    |\t Médico: {i['medico']}       |\t Disponibilidad: {i['disponibilidad']}")
        else:
            print('No hay médicos disponibles en el área mencionada.')

    def validar_fecha_cita(self, fecha):
        try:
            fecha_cita = date(int(fecha[6] + fecha[7] + fecha[8] + fecha[9]),
                        int(fecha[3] + fecha[4]),
                        int(fecha[0] + fecha[1]))

            if len(fecha) == 10 and (date.today() < fecha_cita <= (date.today() + timedelta(days=30))):
                return True
            else:
                return False
        except:
            return False

    def validar_id(self, id, citas):
        lista_id = []
        for i in citas:
            lista_id.append(i['id'])
        if id in lista_id:
            return True
        else:
            return False