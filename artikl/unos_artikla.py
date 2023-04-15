def unos_artikla(redni_broj):
    artikl = {}
    artikl['naslov'] = input(f'Unesite naslov {redni_broj}. artikla: ').capitalize()
    artikl['opis'] = input(f'Unesite opis {redni_broj}. artikla: ').capitalize()
    artikl['cijena'] = float(input(f'Unesite cijenu {redni_broj}. artikla: '))
    return artikl