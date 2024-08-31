from abc import ABC, abstractmethod

# Observer - Para manejar notificaciones

class Subject(ABC):
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, mensaje):
        for observer in self._observers:
            observer.update(mensaje)