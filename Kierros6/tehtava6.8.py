def tee_akronyymi(nimi):
    akronyymi = ""
    sanat = str.split(nimi, " ")
    for sana in sanat:
        akronyymi += sana[0].upper()

    return akronyymi
