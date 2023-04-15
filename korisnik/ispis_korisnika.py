def ispis_korisnika(korisnik):
    print('Informacije o korisniku: ')
    print(f'\t Ime: {korisnik["ime"]}')
    print(f'\t Prezime: {korisnik["prezime"]}')
    # print(f'\t Telefon: {korisnik["tel"]["broj"]}')
    print(f'\t Email: {korisnik["email"]}')

def get_korisnik(redni_broj, korisnik):
    return f"{redni_broj}. {korisnik['ime']} {korisnik['prezime']}"