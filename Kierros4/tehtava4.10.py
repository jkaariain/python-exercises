# Täydennä tähän tiedostoon kaikki kohdat, joissa lukee TODO
# TIE-02100 Johdatus ohjelmointiin, KK2016
# TODO: Ohjelmointitehtävä T3, valmis koodirunko
# TODO: Saat myös halutessasi poistaa kommentteja,
# TODO: joissa selitetään tehtävänantoa.

from math import sqrt


# Tämä on tekstikäyttöliittymämme päävalikko ja siihen liittyvä
# käyttäjän syötteiden käsittely. Sinun tulee muokata vain TODO:lla merkityt
# kohdat, joissa kutsutaan sinun itsesi toteuttamia funktioita ja
# tallennetaan funktioiden palauttamat arvot sopiviin muuttujiin.
def valikko():
    tankin_koko = lue_luku("Kuinka iso bensatankki ajoneuvossa on? ")
    bensaa = tankin_koko  # Tankki täyteen aluksi
    kulutus_satasella = lue_luku("Montako litraa bensaa ajoneuvo kuluttaa "
                                 + "sadalla kilometrillä? ")
    x = 0.0  # Auton tämänhetkinen x-koordinaatti
    y = 0.0  # Auton tämänhetkinen y-koordinaatti

    # Jos print:illä tulostaa näytölle merkkijonon, joka sisältää
    # \n -merkkiyhdistelmiä, niiden paikalle tulostuu rivinvaihto
    # (siis kursori siirtyy seuraavan rivin alkuun).
    valikkoteksti = "1) Tankkaa 2) Aja 3) Lopeta \n-> "

    while True:
        print("Koordinaatit x={:.1f}, y={:.1f}, "
              "tankissa on {:.1f} litraa polttoainetta.".format(x, y, bensaa))

        valinta = input(valikkoteksti)

        if valinta == "1":
            tankataan = lue_luku("Montako litraa tankataan: ")
            bensaa = tankkaa(tankin_koko, tankataan, bensaa)

        elif valinta == "2":
            uusi_x = lue_luku("x: ")
            uusi_y = lue_luku("y: ")
            bensaa, x, y = aja(x, y, uusi_x, uusi_y, bensaa, kulutus_satasella)

        elif valinta == "3":
            break

    print("Kiitos ja hei!")


# Tämä funktio saa parametreinaan kolme desimaalilukua (float):
#   (1) tankin koon,
#   (2) tankattavaksi halutun bensamäärän ja
#   (3) tankissa tällä hetkellä jäljellä olevan bensamäärän.
# Parametrien on oltava edellä esitetyssä järjestyksessä, muutoin ohjelma
# ei tule läpäisemään automaattisia testejä. Funktion paluuarvo on tankissa
# tankkauksen jälkeen jäljellä oleva bensamäärä desimaalilukuna (float).
# Funktio ei saa tulostaa näytölle mitään, eikä se saa lukea
# syötteitä näppäimistöltä.
def tankkaa(tankin_koko, bensamäärä, bensamäärä_tankissa):
    if bensamäärä_tankissa + bensamäärä > tankin_koko:
        return tankin_koko
    else:
        return bensamäärä_tankissa + bensamäärä

# Tämä funktio saa parametreinaan kuusi desimaalilukua (float):
#   (1) Lähtöpisteen x-koordinaatin
#   (2) Lähtöpisteen y-koordinaatin
#   (3) Päämäärän x-koordinaatin
#   (4) Päämäärän y-koordinaatin
#   (5) Tankissa lähtöhetkellä jäljellä olevan bensamäärän
#   (6) Auton kulutuksen sadalla kilometrillä
# Parametrien on jälleen oltava edellä listatussa järjestyksessä,
# koska automaattinen testiohjelma olettaa niin. Funktio palauttaa
# kolme desimaalilukuarvoa (float):
#   (1) Ajomatkan jälkeen tankissa jäljellä olevan bensamäärän
#   (2) Ajomatkan saavutetun päätepisteen x-koordinaatin
#   (3) Ajomatkan saavutetun päätepisteen y-koordinaatin
# Näiden paluuarvojen tulee olla edellisen mukaisessa järjestyksessä.
# Funktio ei saa tulostaa näytölle mitään, eikä se saa lukea
# syötteitä näppäimistöltä.


def aja(x1, y1, x2, y2, bensamäärä_tankissa, kulutus_per_sata_m):
    # Tämän funktion toteuttaminen on todennäköisesti selkeämpää, jos
    # teet sen avuksi myös joitain apufunktioita.
    if bensamäärä_tankissa == 0.0:
        return bensamäärä_tankissa, x1, y1

    etäisyys = pituus(x1, y1, x2, y2)
    kulutus = (etäisyys / 100) * kulutus_per_sata_m

    if bensamäärä_tankissa - kulutus < 0:
        delta_x = (x2 - x1) * (bensamäärä_tankissa / kulutus)
        delta_y = (y2 - y1) * (bensamäärä_tankissa / kulutus)
        bensamäärä_tankissa = 0.0
        return bensamäärä_tankissa, x1 + delta_x, y1 + delta_y
    else:
        bensamäärä_tankissa -= kulutus

    return bensamäärä_tankissa, x2, y2


# Tässä välissä sinun on määriteltävä (vähintään) tehtävänannon vaatimat
#  kaksi omaa funktiota, joista jokaisella on ainakin yksi parametri
# ja paluuarvo ja joita kutsutaan jossain toisaalla ohjelmakoodissa.
def pituus(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def lue_luku(kehote, virheilmoitus="Vääräntyyppinen syöte!"):
    # Tämä funktio lukee käyttäjältä syötettä, kunnes käyttäjän antama
    # syöte on luku. Sinun ei tarvitse muokata tätä funktiota eikä ymmärtää
    # sen toimintaa, mutta voit halutessasi tutustua siihen.
    try:
        return float(input(kehote))
    except ValueError as e:
        print(virheilmoitus)
        return lue_luku(kehote, virheilmoitus)


def main():
    valikko()


main()
