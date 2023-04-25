from osobna import unos_osobne
from utilities import unos_telefona, unos_mail, unos_mail_m, unos_godina


def unos_korisnika(redni_broj):
    korisnik = {}
    korisnik['ime'] = input(f'Unesite ime {redni_broj}. korisnika: ').capitalize()
    korisnik['prezime'] = input(f'Unesite prezime {redni_broj}. korisnika: ').capitalize()
    korisnik['godine'] = unos_godina(f'Unesite broj godina {redni_broj}. korisnika: ')
    korisnik['tel'] = unos_telefona(f'Unesite telefon {redni_broj}. korisnika: ')
    korisnik['email'] = unos_mail_m(f'Unesite email {redni_broj}. korisnika: ').strip()
    #korisnik['osobna'] = unos_osobne(redni_broj)
    return korisnik
