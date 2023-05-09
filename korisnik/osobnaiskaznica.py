class OsobnaIskaznica:
    def __init__(self, broj, prebivaliste, oib):
        self.__broj = broj
        self.__prebivaliste = prebivaliste
        self.__oib = oib

    @property
    def broj(self):
        return self.__broj


    @broj.setter
    def broj(self, broj):
        self.__broj = broj

    @property
    def oib(self):
        return self.__oib

    @oib.setter
    def oib(self, oib):
        self.__oib = oib


    def ispis(self):
        print('Podatci sa osobne iskaznice: ')
        print(f"\tOIB: {self.__oib}")
        print(f"\tPrebivalište: {self.__prebivaliste}")
        print(f"\tBroj osobne: {self.__broj}")

