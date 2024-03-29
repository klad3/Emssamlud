from abc import ABC, abstractmethod
class MenuAdministracion(ABC):
    @abstractmethod
    def menu(self):
        pass
    
    @abstractmethod
    def registrar(self):
        pass

    @abstractmethod
    def modificar(self):
        pass

    @abstractmethod
    def eliminar(self):
        pass