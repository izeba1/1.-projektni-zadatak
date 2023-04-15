def unos_osobne(redni_broj):
    osobna = {}
    osobna['oib'] = int(input(f'Unesi OIB {redni_broj}. korisnika: '))
    osobna['prebivaliste'] = input(f'Unesite prebivalište {redni_broj}. korisnika: ')
    osobna['broj'] = int(input(f'Unesite broj osobne iskaznice {redni_broj}. korisnika: '))
    return osobna