from abc import ABC, abstractmethod

class JsonConfigEntities(ABC):
    @abstractmethod
    def registrar_json(self):
        pass

    @abstractmethod
    def modificar_json(self):
        pass

    @abstractmethod
    def eliminar_json(self):
        pass