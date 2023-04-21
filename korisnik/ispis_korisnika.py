from osobna import ispis_osobne


def ispis_korisnika(korisnik):
    print('Informacije o korisniku: ')
    print(f'\t Ime: {korisnik["ime"]}')
    print(f'\t Prezime: {korisnik["prezime"]}')
    print(f'\t Telefon: {korisnik["tel"]}')
    print(f'\t Email: {korisnik["email"]}')
    #ispis_osobne(korisnik['osobna'])


def get_korisnik(redni_broj, korisnik):
    return f"{redni_broj}. {korisnik['ime']} {korisnik['prezime']}"

def ispis_svih_korisnika(korisnici):
    print('Ispis svih korisnika: ')
    for korisnik in korisnici:
        ispis_korisnika(korisnik)