from abc import ABC, abstractmethod

class JsonConfigEntities(ABC):
    @abstractmethod
    def registrar_json(self, lista):
        pass

    @abstractmethod
    def verificar_json(self, id):
        pass

    @abstractmethod
    def modificar_json(self, **kwargs):
        pass

    @abstractmethod
    def eliminar_json(self, id):
        pass