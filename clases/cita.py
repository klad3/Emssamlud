class Cita:
    def __init__(self, fecha_cita, precio, estado) -> None:
        self.__fecha_cita = fecha_cita
        self.__precio = precio
        self.__estado = estado

    @property
    def fecha_cita(self):
        return self.__fecha_cita

    @fecha_cita.setter
    def fecha_cita(self, fecha_cita):
        self.__fecha_cita = fecha_cita

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    # Se agenda la cita
    def agendar_cita(self, fecha_cita, precio, estado):
        pass
    # Se efectuara el pago de la cita agendada
    def pagar_cita(self, fecha_cita, precio):
        pass
    
    # Se archiva la cita
    def archivar_cita(self, estado):
        pass