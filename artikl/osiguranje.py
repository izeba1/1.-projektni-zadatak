from abc import ABC, abstractmethod

class Osiguranje(ABC):
    @abstractmethod
    def izracunaj_osiguranje(self):
        pass