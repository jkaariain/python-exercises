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
        self.__osoittaja //= gcd
        self.__nimittäjä //= gcd

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


def suurin_yhteinen_tekijä(a, b):
    """ Euklideen algoritmi kahden kokonaisluvun a ja b suurimman yhteisen
    tekijän laskemiseksi.  Kopioitu pääosiltaan internetistä. Algoritmin
    ymmärtäminen ei ole kurssilla tarpeen.
    """

    while b != 0:
        a, b = b, a % b
    return a
