# TIE-02100 Johdatus ohjelmointiin 
# Tehtävän 9.4. koodipohja

def lue_tiedosto(tiedoston_nimi):
    """Lukee tiedostosta pelaajien pelaamat biisit ja saadut tulokset.""" 
    try:
        tiedosto = open(tiedoston_nimi, "r")

        pelaajat = {}

        # Käydään tiedosto riveittäin läpi, rivi sisältää pelaajan tiedot
        for rivi in tiedosto:
            osat = rivi.strip().split(";")
            pelaaja = osat[0] # sisältää pelaajan nimen
            biisit = osat[1:] # jokainen listan alkio sisältää yhden biisin

            pelaajat[pelaaja] = {}

            # Käydään läpi pelaajan pelaamat kappaleet yksi kerrallaan
            for biisi in biisit:
                osat = biisi.split(":")
                tulokset = osat[1].split(",")
                # Sisältää kappaleen nimen
                nimi = osat[0]
                # Sisältää listan kappaleen painalluksista (int)
                tulokset = [int(luku) for luku in tulokset]

                pelaajat[pelaaja][nimi] = tulokset

            # pelaajat sisältävään tietorakenteeseen.

        tiedosto.close()
        return pelaajat
    except IOError:
        print("Virhe: tiedostoa ei saatu luettua.")
        return None


def laske_prosenttiosuus(pisteet):
    pelaajatulos = pisteet[0]*5 + pisteet[1]*4 + pisteet[2]*2 + \
                   pisteet[3]*0 + pisteet[4]*-6 + pisteet[5]*-12
    maksimitulos = sum(pisteet)*5

    prosenttiosuus = (pelaajatulos / maksimitulos) * 100

    return prosenttiosuus


def main():

    kertoimet = [5, 4, 2, 0, -6, -12]

    tiedoston_nimi = input("Anna tiedoston nimi: ")
    pelaajalista = lue_tiedosto(tiedoston_nimi)

    for x in sorted(pelaajalista.keys()):
        print(x, ':', sep='')
        for y in sorted(pelaajalista[x]):
            print('-', y + ': ', end='')
            print("{:.2f}".format(laske_prosenttiosuus(pelaajalista[x][y]))
                  + '%')


main()
