class Murtoluku:
    """ Kuvaa yhtä murtolukua, joka koostuu osoittajasta ja nimittäjästä."""

    def __init__(self, osoittaja, nimittäjä):
        """
        Luokan rakentaja. Tarkastaa että osoittaja ja nimittäjä ovat
        kokonaislukuja ja alustaa ne annettuihin arvoihin.

        :param osoittaja: murtoluvun osoittaja
        :param nimittäjä: murtoluvun nimittäjä
        """

        if not isinstance(osoittaja, int) or not isinstance(nimittäjä, int):
            raise TypeError
        elif nimittäjä == 0:
            raise ValueError

        self.__osoittaja = osoittaja
        self.__nimittäjä = nimittäjä

        if self.__nimittäjä < 0 or \
                (self.__osoittaja < 0 and self.__nimittäjä < 0):
            self.__nimittäjä *= -1
            self.__osoittaja *= -1

    def tulosta(self):
        """ Tulostaa murtoluvun muodossa osoittaja/nimittäjä. """

        if self.__osoittaja * self.__nimittäjä < 0:
            etumerkki = "-"
        else:
            etumerkki = ""
        return "{:s}{:d}/{:d}".format(etumerkki, abs(self.__osoittaja),
                                     abs(self.__nimittäjä))

    def sievenna(self):
        gcd = suurin_yhteinen_tekijä(self.__osoittaja, self.__nimittäjä)
        a1 = self.__osoittaja // gcd
        a2 = self.__nimittäjä // gcd
        if a2 < 0 or (a1 < 0 and a2 < 0):
            a2 *= -1
            a1 *= -1

        return Murtoluku(a1, a2)

    def vastaluku(self):
        return Murtoluku(-self.__osoittaja, self.__nimittäjä)

    def kaanteisluku(self):
        return Murtoluku(self.__nimittäjä, self.__osoittaja)

    def lue_osoittaja(self):
        return self.__osoittaja

    def lue_nimittäjä(self):
        return self.__nimittäjä

    def kerro(self, kert_mluku):
        os = self.__osoittaja * kert_mluku.lue_osoittaja()
        nim = self.__nimittäjä * kert_mluku.lue_nimittäjä()
        return Murtoluku(os, nim)

    def jaa(self, jak_mluku):
        os = self.__osoittaja * jak_mluku.lue_nimittäjä()
        nim = self.__nimittäjä * jak_mluku.lue_osoittaja()
        return Murtoluku(os, nim)

    def summaa(self, sum_mluku):
        os = (self.__osoittaja * sum_mluku.lue_nimittäjä()) + \
             (sum_mluku.lue_osoittaja() * self.__nimittäjä)
        nim = self.__nimittäjä * sum_mluku.lue_nimittäjä()
        return Murtoluku(os, nim)

    def erota(self, erot_mluku):
        os = (self.__osoittaja * erot_mluku.lue_nimittäjä()) - \
             (erot_mluku.lue_osoittaja() * self.__nimittäjä)
        nim = self.__nimittäjä * erot_mluku.lue_nimittäjä()
        return Murtoluku(os, nim)

    def __lt__(self, toinen_mluku):
        a1 = self.__osoittaja / self.__nimittäjä
        a2 = toinen_mluku.lue_osoittaja() / toinen_mluku.lue_nimittäjä()

        if a1 < a2:
            return True
        else:
            return False

    def __le__(self, toinen_mluku):
        a1 = self.__osoittaja / self.__nimittäjä
        a2 = toinen_mluku.lue_osoittaja() / toinen_mluku.lue_nimittäjä()

        if a1 > a2:
            return True
        else:
            return False

    def __str__(self):
        return str(self.__osoittaja) + "/" + str(self.__nimittäjä)


def suurin_yhteinen_tekijä(a, b):
    """ Euklideen algoritmi kahden kokonaisluvun a ja b suurimman yhteisen
    tekijän laskemiseksi.  Kopioitu pääosiltaan internetistä. Algoritmin
    ymmärtäminen ei ole kurssilla tarpeen.
    """

    while b != 0:
        a, b = b, a % b
    return a


def lue_murtoluvut():
    print("Syötä murtolukuja muodossa kokonaisluku/kokonaisluku")
    print("Yksi murtoluku yhdelle riville. Lopeta syöttämällä tyhjä rivi.")
    murtoluvut = []
    lista = []
    murtoluku = input()

    while 1:
        if murtoluku == '':
            break
        murtoluvut.append(murtoluku)
        murtoluku = input()

    for x in murtoluvut:
        s = x.split('/')
        lista.append(Murtoluku(int(s[0]), int(s[1])))

    return lista


def lue_murtoluku():
    luku = input("Syötä murtoluku muodossa kokonaisluku/kokonaisluku: ")
    if luku == "":
        return
    tunniste = input("Syötä nimi: ")

    luku = luku.split('/')
    murtoluku = Murtoluku(int(luku[0]), int(luku[1]))

    return tunniste, murtoluku


def tulosta(sanakirja):
    avain = input("Syötä nimi: ")

    if avain in sanakirja:
        print(avain, "=", sanakirja[avain])
    else:
        print("Nimeä {:s} ei ole olemassa".format(avain))


def listaa(sanakirja):
    if len(sanakirja) > 0:
        for x in sorted(sanakirja):
            print(x, "=", sanakirja[x])


def main():
    murtoluvut = {}
    laskuoperaatiot = {}

    laskuoperaatiot["+"] = (lambda a, b: a.summaa(b))
    laskuoperaatiot["-"] = (lambda a, b: a.erota(b))
    laskuoperaatiot["*"] = (lambda a, b: a.kerro(b))
    laskuoperaatiot["/"] = (lambda a, b: a.jaa(b))

    while 1:
        komento = input("> ")

        if komento == "lisää":
            avain, murtoluku = lue_murtoluku()
            murtoluvut[avain] = murtoluku
        elif komento == "tulosta":
            tulosta(murtoluvut)
        elif komento == "listaa":
            listaa(murtoluvut)
        elif komento in laskuoperaatiot:
            a1 = input("Syötä 1. operandin nimi: ")
            if a1 not in murtoluvut:
                print("Nimeä {:s} ei ole olemassa".format(a1))
                continue
            a2 = input("Syötä 2. operandin nimi: ")
            if a2 not in murtoluvut:
                print("Nimeä {:s} ei ole olemassa".format(a2))
                continue
            eka = murtoluvut[a1]
            toka = murtoluvut[a2]
            a3 = laskuoperaatiot[komento](eka, toka)
            print(murtoluvut[a1], komento, murtoluvut[a2], "=", a3)
            print("eli sievennettynä", a3.sievenna())
        elif komento == "lopeta":
            break
        else:
            print("Tuntematon komento!")

    print("Hei hei!")

main()
