def get_korisnik(redni_broj, korisnik):
    return f"{redni_broj}. {korisnik.email} {korisnik.telefon}"

def ispis_svih_korisnika(korisnici):
    print('Ispis svih korisnika: ')
    for korisnik in korisnici:
        korisnik.ispis()