class Cita:
    def __init__(self, paciente, area, medico, fecha_cita) -> None:
        self._fecha_cita = fecha_cita
        self._area = area
        self._medico = medico
        self._paciente = paciente


    @property
    def fecha_cita(self):
        return self.__fecha_cita

    @fecha_cita.setter
    def fecha_cita(self, fecha_cita):
        self.__fecha_cita = fecha_cita

    @property
    def hora(self):
            return self.__hora

    @hora.setter
    def hora(self, hora):
        self.__hora = hora

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area):
        self.__area = area

    @property
    def medico(self):
        return self.__medico

    @medico.setter
    def medico(self, medico):
        self.__medico = medico

    @property
    def consultorio(self):
        return self.__consultorio

    @consultorio.setter
    def consultorio(self, consultorio):
        self.__consultorio = consultorio

    @property
    def paciente_dni(self):
        return self.__paciente

    @paciente_dni.setter
    def paciente_dni(self, paciente):
        self.__paciente = paciente



    # Se agenda la cita
    def agendar_cita(self, fecha_cita, precio, estado):
        pass
    # Se efectuara el pago de la cita agendada
    
    # Se archiva la cita
    def archivar_cita(self, estado):
        pass