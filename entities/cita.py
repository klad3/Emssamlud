class Cita:
    def __init__(self, id, paciente, area, medico, fecha_cita):
        self.__id = id
        self.__paciente = paciente
        self.__area = area
        self.__medico = medico
        self.__fecha_cita = fecha_cita

    @property
    def id(self):
        return self.__id

    @property
    def paciente(self):
        return self.__paciente

    @property
    def fecha_cita(self):
        return self.__fecha_cita

    @property
    def area(self):
        return self.__area

    @property
    def medico(self):
        return self.__medico

    @property
    def paciente_dni(self):
        return self.__paciente