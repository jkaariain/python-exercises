import csv


def main():
    nimi = input("Syötä luettavan tiedoston nimi: ")
    dialect_jono = input("Syötä luettavan tiedoston dialect: ")
    kirjoitus_nimi = input("Syötä kirjoitettavan tiedoston nimi: ")
    dialect_jono_kirj = input("Syötä kirjoitettavan tiedoston dialect: ")
    sisältö = []

    try:
        with open(nimi, "r", encoding="utf-8") as luettava_tiedosto:
            lukija = csv.reader(luettava_tiedosto, dialect_jono)
            for rivi in lukija:
                sisältö.append(rivi)
    except OSError:
        print()
        print("Virhe tiedoston käsittelyssä.")
        return
    except csv.Error:
        print()
        print("Virheellinen dialect-merkkijono.")
        return

    try:
        with open(kirjoitus_nimi, "w", encoding="utf-8") \
                as kirjoitettava_tiedosto:
            kirjoittaja = csv.writer(kirjoitettava_tiedosto, dialect_jono_kirj)
            kirjoittaja.writerows(sisältö)

        print()
        print("Tiedosto", nimi, "muutettu formaattiin",
              dialect_jono_kirj + ".")
    except OSError:
        print()
        print("Virhe tiedoston käsittelyssä.")
        return
    except csv.Error:
        print()
        print("Virheellinen dialect-merkkijono.")
        return

main()
