# Ratsia koulun nurkalla - Jaakko Kääriäinen
#
# Tämä ohjelma vastaanottaa käyttäjältä mittauspaikan nopeusrajoituksen sekä
# annetun määrän mittaustuloksia. Jos käyttäjä syöttää tyhjän rivin,
# ohjelma lopettaa tulosten vastaanottamisen. Mittaustulokset,
# jotka ovat alle 20 km/h jätetään pois.
#
# Mittaustuloksilla ohjelma laskee tilastotiedot ja tulostaa tulokset
# ruudulle.


def laske_tilastotiedot(lista, nopeusrajoitus):
    """
    Laskee ja tulostaa tilastotiedot
    :param lista:
    :param nopeusrajoitus:
    :return:
    """
    vaihteluväli = max(lista) - min(lista)
    rikesakko_lkm = 0
    sakko_lkm = 0
    RIKESAKKO_RAJA = 8
    SAKKO_RAJA = 20

    if len(lista) % 2 != 0:  # Pariton määrä alkioita
        lista.sort()
        mediaani = lista[len(lista)//2]
    elif len(lista) == 2:  # Vain 2 alkiota
        mediaani = (lista[0] + lista[1]) / 2
    else:  # Parillinen määrä alkioita
        lista.sort()
        mediaani = (lista[len(lista) // 2 + 1] + lista[len(lista) // 2]) / 2

    for i in lista:
        if i >= (nopeusrajoitus + RIKESAKKO_RAJA):  # Rikesakko
            rikesakko_lkm += 1

    for i in lista:
        if i >= (nopeusrajoitus + SAKKO_RAJA):  # Sakko
            sakko_lkm += 1

    rikesakko_lkm -= sakko_lkm

    print("Vaihteluväli: {:d}".format(vaihteluväli))
    print("Mediaani: {:.1f}".format(mediaani))

    if rikesakko_lkm > 0:
        print("Rikesakon ylinopeudesta olisi saanut {:d} kuljettajaa".format
              (rikesakko_lkm))

    if sakko_lkm > 0:
        print("Sakon ylinopeudesta olisi saanut {:d} kuljettajaa".format
              (sakko_lkm))


def get_mittaustulokset():
    """
    Vastaanottaa käyttäjältä mittaustulokset kunnes syötteenä annetaan tyhjä
    rivi.
    :return: lista mittaustuloksista
    """
    tulokset = []
    print("Syötä nopeusmittauksen tulokset, lopeta tyhjällä rivillä:")

    while 1:  # Ääretön silmukka
        rivi = input()
        if rivi == "":
            return tulokset
        else:
            tulokset.append(int(rivi))


def get_ylinopeudet(lista, nopeusrajoitus):
    """
    Suodata ylinopeudet mittaustuloksista
    :param lista:
    :param nopeusrajoitus:
    :return:
    """
    a = []
    for i in lista:
        if i >= (nopeusrajoitus + 8):
            a.append(i)

    return a


def poista_mittaustulokset(lista):
    """
    Poistaa listasta mittaustulokset, jotka ovat alle 20 km/h.
    :param lista: Muokattava lista
    :return: Palauttaa poistettujen tulosten lukumäärän sekä muokatun listan
    """
    poistetut_tulokset_lkm = 0
    for i in lista:
        if i < 20:
            poistetut_tulokset_lkm += 1

    # Luo lista, johon sisältyy vain ne mittaustulokset, jotka ovat yli 20 km/h
    a = [i for i in lista if i > 20]

    return a, poistetut_tulokset_lkm


def graafinen_esitys(lista):
    """
    Tulostaa graafisen esityksen nopeuksien jakaumasta.
    :param lista:
    :return:
    """
    frekvenssi = []
    rivi = ""
    idx = 0  # Listaindeksi
    JAKOVÄLI = 5

    # Luo graafi
    for i in range(min(lista), max(lista) + 1, JAKOVÄLI):
        for j in range(i, i+JAKOVÄLI):
            rivi += lista.count(j) * "#"
        frekvenssi.append(rivi)
        rivi = ""  # Tyhjennä rivi

    # Tulosta graafi
    for i in range(min(lista), max(lista) + 1, JAKOVÄLI):
        print("{:d} {:s}".format(i, frekvenssi[idx]))
        idx += 1


def main():
    """
    Ohjelman pääfunktio
    :return:
    """
    rajoitus = int(input("Syötä mittauspaikan nopeusrajoitus: "))

    # Lopeta ohjelma, jos nopeusrajoitus on negatiivinen tai yhtä kuin nolla.
    if rajoitus <= 0:
        print("Nopeusrajoituksen tulee olla positiivinen kokonaisluku.")
        return

    # Vastaanota mittaustulokset ja samalla tee lista tuloksista, jotka
    # ylittävät nopeusrajoituksen.
    mittaustulokset = get_mittaustulokset()
    ylinopeudet = get_ylinopeudet(mittaustulokset, rajoitus)
    mittaustulokset, poistetut = \
        poista_mittaustulokset(mittaustulokset)

    if poistetut > 0:
        print("Poistettiin {:d} kpl mittaustuloksia, "
              "joiden suuruus oli alle 20 km/h"
              .format(poistetut))

    if len(mittaustulokset) != 0:  # Onko listassa elementtejä?
        laske_tilastotiedot(mittaustulokset, rajoitus)

        # Tulosta lista sekä jakauma ylinopeuksista, jos niitä on.
        if len(ylinopeudet) != 0:
            print("Ylinopeudet mittausjärjestyksessä:")
            for i in ylinopeudet:
                print(i)

        print()

        print("Graafinen esitys aineistosta:")
        graafinen_esitys(mittaustulokset)

main()
