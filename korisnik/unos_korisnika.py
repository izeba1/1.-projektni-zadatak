def unos_korisnika(redni_broj):
    korisnik = {}
    korisnik['ime'] = input(f'Unesite ime {redni_broj}. korisnika: ').capitalize()
    korisnik['prezime'] = input(f'Unesite prezime {redni_broj}. korisnika: ').capitalize()
#   korisnik['tel'] = int(input(f'Unesite broj telefona {redni_broj}. korisnika: '))
    korisnik['email'] = input(f'Unesite email {redni_broj}. korisnika: ').strip()
    return korisnik
