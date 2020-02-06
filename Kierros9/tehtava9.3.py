# TIE-02100 Johdatus ohjelmointiin
# Tehtävä 9.2. koodipohja


def lue_tiedosto(tiedoston_nimi):
    """Lukee ja tallentaa tiedostossa olevat sarjat ja niiden genret."""

    genre_sanakirja = {}

    try:
        tiedosto = open(tiedoston_nimi, "r")

        for rivi in tiedosto:
            # Erotellaan nimi ja genret erilleen
            # nimi on merkkijono ja genret lista
            nimi, genret = rivi.rstrip().split(";")
            genret = genret.split(",")

            for genre in genret:
                if genre not in genre_sanakirja:
                    genre_sanakirja[genre] = []
                    genre_sanakirja[genre].append(nimi)
                else:
                    genre_sanakirja[genre].append(nimi)

        tiedosto.close()
        return genre_sanakirja

    except ValueError:
        print("Virhe: rivi ei ole muotoa nimi;genret.")
        return None

    except IOError:
        print("Virhe: tiedostoa ei saada luettua.")
        return None


def main():

    tiedoston_nimi = input("Anna tiedoston nimi: ")
    sanakirja = lue_tiedosto(tiedoston_nimi)

    print("Valittavia genrejä ovat:", ', '.join(sorted(sanakirja.keys())))

    while True:
        genre = input("> ")

        if genre == "lopeta":
            return

        if genre in sanakirja:
            for x in sorted(sanakirja[genre]):
                print(x)


main()
