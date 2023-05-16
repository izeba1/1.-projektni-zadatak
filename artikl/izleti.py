from .osiguranje import Osiguranje
from .artikl import Artikl
class Izleti(Artikl, Osiguranje):
    def __init__(self, naslov, opis, cijena):
        super().__init__(naslov, opis, cijena)

    def izracunaj_osiguranje(self):
        cijena = self._cijena/50
        return cijena

    def ispis(self):
        print('Informacije o izletu:')
        print(f'\tNaslov: {self.naslov}')
        print(f'\tOpis: {self.opis}')
        print(f'\tCijena: {self.izracunaj_osiguranje()}')
