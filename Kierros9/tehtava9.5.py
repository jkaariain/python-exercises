# TIE-02100 Johdatus ohjelmointiin
# Kauppakori
# Jaakko Kääriäinen


def lue_tiedosto(tiedostonimi):
    """Lukee tiedostosta kauppojen nimet, tuotteet ja niiden hinnat ja
    tallentaa ne sopivaan tietorakenteeseen"""
    kaupat = {}

    try:
        tiedosto = open(tiedostonimi, 'r', encoding='utf-8')

        for rivi in tiedosto:
            osat = rivi.rstrip().split(":")
            kaupan_nimi = osat[0]
            tuote = osat[1]
            hinta = osat[2]

            if kaupan_nimi not in kaupat:
                kaupat[kaupan_nimi] = {}
                kaupat[kaupan_nimi][tuote] = float(hinta)
            else:
                kaupat[kaupan_nimi][tuote] = float(hinta)

        tiedosto.close()
    except OSError:
        print("Virhe: tiedostoa ei saatu luettua.")
        return None

    return kaupat


def tulosta_tiedot(tuotetiedot):
    """Tulostaa kauppojen nimet ja niiden tuotelistat"""
    for x in sorted(tuotetiedot):
        print(x)
        for y in sorted(tuotetiedot[x]):
            print("\t{:<15}{:>10.2f}".format(y, tuotetiedot[x][y]), end='')
            print(' e')


def tulosta_saatavilla(tuotetiedot):
    """Tulostaa saatavilla olevat tuotteet ja niiden alhaisimmat hinnat"""
    # Luo uusi sanakirja, jossa avaimina ovat kaikki eri tuotteet
    sanakirja = {}

    for x in sorted(tuotetiedot):  # x: tuote, tuotetiedot: Kaupan nimi
        for y in sorted(tuotetiedot[x]):  # y: hinta tuotetiedot[x]: tuote
            if y not in sanakirja:
                sanakirja[y] = tuotetiedot[x][y]
            else:
                if sanakirja[y] > tuotetiedot[x][y]:
                    sanakirja[y] = tuotetiedot[x][y]

    print("Saatavilla olevat eri tuotteet:")
    for x in sorted(sanakirja):
        print("\t{:<15}{:>10.2f}".format(x, sanakirja[x]), end='')
        print(' e')


def kauppakori(tuotetiedot):
    """Pyytää käyttäjältä listan tuotteista ja palauttaa halvimman
    kauppakorin"""
    tuotteet = input("Anna tuotteet eroteltuna välilyönneillä:\n").split(' ')
    kaupat = {}
    lista_halvimmista = []  # Lista kaupoista, joilla on halvin hinta

    # Luo sellainen kauppasanakirja, joka sisältää ne kaupat, jotka
    # tarjoavat kaikki käyttäjän listaamat tuotteet
    for x in tuotetiedot:
        hinta = 0.0
        on_kaupassa = True  # Onko tuote kaupassa?
        for y in tuotteet:
            if y in tuotetiedot[x]:
                hinta += tuotetiedot[x][y]
            else:
                on_kaupassa = False  # Jos tuotetta ei ole kaupassa
                break
        if not on_kaupassa:  # Älä lisää kauppaa kauppasanakirjaan,
            # jos tuotetta ei löydy kaupasta, vaan siirry toiseen kauppaan.
            continue
        else:
            kaupat[x] = hinta
            pass

    # Jos on kauppoja, jotka tarjoavat käyttäjän listaamat tuotteet
    if len(kaupat) > 0:
        halvin = min(kaupat.values())
        for x in kaupat:
            if kaupat[x] == halvin:
                lista_halvimmista.append(x)
    else:
        print("Yksikään kauppa ei myy kaikkia kauppakorin tuotteita!")
        return

    if len(lista_halvimmista) == 1:  # Jos on vain yksi kauppa.
        print("Halvin kauppa tälle korille on {:s} {:.2f} e hinnallaan!".format
              (lista_halvimmista[0], halvin))
    else:  # Jos on useampi kuin yksi kauppa.
        print("Seuraavat kaupat myyvät yhtä halvalla {:.2f} e hinnalla:"
              .format(halvin), end=' ')
        print(', '.join(sorted(lista_halvimmista)))


def main():
    """Pääfunktio"""
    tuotetiedot = lue_tiedosto('tuotetiedot.txt')

    print("Tervetuloa kauppakorisovellukseen!\n"
          "Käytettävissä olevat komennot:\n"
          " T ulosta kaupat tuotteineen\n"
          " S aatavilla olevien tuotteiden listaus\n"
          " K auppakorin halvin myyjä\n"
          " Q uit\n")

    syöte = ""
    while syöte != "Q":
        syöte = input("\nAnna komento (T, S, K, Q): ").upper()

        if syöte == "T":
            tulosta_tiedot(tuotetiedot)

        elif syöte == "S":
            tulosta_saatavilla(tuotetiedot)

        elif syöte == "K":
            kauppakori(tuotetiedot)

        elif syöte == "Q":
            print("Hei hei!")
            return

        else:
            print("Virheellinen komento!")

main()
