from abc import ABC, abstractmethod
class ValidacionEntities(ABC):
    @abstractmethod
    def validar_opcion_menu(self, opcion):
        pass
    
    @abstractmethod
    def validar_dni(self, dni):
        pass
    
    @abstractmethod
    def validar_nombres(self, nombres):
        pass

    @abstractmethod
    def validar_apellido(self, apellido):
        pass

    @abstractmethod
    def validar_telefono(self, telefono):
        pass

    @abstractmethod
    def validar_sexo(self, sexo):
        pass