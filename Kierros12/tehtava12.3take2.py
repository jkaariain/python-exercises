# TIE-02100 Johdatus ohjelmointiin
# Kulunvalvonta
# Jaakko Kääriäinen


class Kulkukortti:
    def __init__(self, tunniste, nimi):
        """
        Luokan rakentaja, eli metodi, joka antaa uuden olion
        luomisvaiheessa sille alkuarvon.

        :param tunniste: henkilön tunniste (str)
        :param nimi: henkilön nimi (str)

        TÄMÄN METODIN TOIMINTA TESTATAAN ERIKSEEN AUTOMAATTITESTISSÄ,
        JOTEN PARAMETRIEN MUUTTAMINEN JOHTAA TESTIEN EPÄONNISTUMISEEN.
        """

        self.__tunniste = tunniste  # Kortin tunniste
        self.__nimi = nimi  # Kortin käyttäjän nimi
        self.__kulkualueet = []  # Kortille valtuutetut aluekoodit

    def tulosta_tiedot(self):
        """
        Funktiolla ei ole paluuarvoa. Se tulostaa kulkukortin
        tiedot näytölle täsmälleen seuraavassa muodossa:
        tunniste, nimi, kulkualueet: ka1,ka2,...,kaN eli esimerkiksi:

           567890, Siiri Siivooja, kulkualueet: F,K,P,R,S,T

        Huomaa, että pilkkujen ja kaksoispisteen perässä
        tulevien välilyöntien on oltava tulosteessa juuri
        saman logiikan mukaisesti kuin edellä ja kulkualueiden
        on tulostuttava tehtävänannon määräämässä järjestyksessä.

        TÄMÄN METODIN TOIMINTA TESTATAAN ERIKSEEN AUTOMAATTITESTISSÄ,
        JOTEN PARAMETRIEN TAI TULOSTUSASUN MUUTTAMINEN JOHTAA TESTIEN
        EPÄONNISTUMISEEN.
        """

        # Muuta lista kulkualuekoodeja merkkijonoksi
        kulkualueet = ','.join(self.__kulkualueet)

        # Tulosta tiedot metodin kuvauksen mukaisesti.
        print(self.__tunniste + ", " + self.__nimi + ", " + "kulkualueet: "
              + kulkualueet)

    def anna_nimi(self):
        """
        :return: Palauttaa kulkukortille talletetun henkilön nimen.
        """

        return self.__nimi

    def anna_kulkualuekoodit(self):
        """
        :return: Palauttaa kulkukortille valtuutetut kulkualuekoodit
        """

        return self.__kulkualueet

    def tarkista_pääsy(self, kulkualuekoodi):
        """
        Tarkastaa pääseeko kulkukortilla halutulle kulkualueelle.

        TÄMÄN METODIN TOIMINTA TESTATAAN ERIKSEEN AUTOMAATTITESTISSÄ,
        JOTEN PALUUARVOJEN TAI PARAMETRIEN MUUTTAMINEN JOHTAA
        TESTIEN EPÄONNISTUMISEEN.

        :param kulkualuekoodi: alue, jolle kortilla halutaan päästä
        :return: True: ovi avautuu kulkukortille tallennetuilla oikeuksilla.
                 False: ovi ei avaudu kulkukortin oikeuksilla
        """
        # Käy läpi kortin kulkualuekoodit.
        # Jos yksi kortin koodeista toteuttaa pääsytestin,
        # kortilla on kulkuoikeus.
        for x in self.__kulkualueet:
            if pääsytesti(x, kulkualuekoodi):
                return True
            else:
                continue

        return False

    def lisää_kulkualue(self, uusi_alue):
        """
        Funktio lisää uuden alueen kulkukortin oikeuksiin tehtävänannossa
        määritellyn säännön mukaisesti. Funktio ei saa tulostaa näytölle
        mitään.

        TÄMÄN METODIN TOIMINTA TESTATAAN ERIKSEEN AUTOMAATTITESTISSÄ.
        MIKÄLI SE EI TOIMI MÄÄRITTELYN MUKAISESTI, TESTIT EPÄONNISTUVAT.
        MYÖS PARAMETRIEN MUUTTAMINEN JOHTAA AUTOMAATTITESTIEN
        EPÄONNISTUMISEEN.

        :param uusi_alue: Lisättävä kulkualue
        """

        # Jos kortilla on olemassa laajempi alue, älä lisää sitä.
        for x in self.__kulkualueet:
            if uusi_alue.startswith(x) and len(uusi_alue) >= len(x):
                return
            else:
                continue

        # Suodata lista
        self.__kulkualueet = \
            sievennä_kulkuoikeuslista(uusi_alue, self.__kulkualueet)

        self.__kulkualueet.sort()  # Järjesta koodit aakkosjärjestykseen

    def yhdistä_kulkukortti(self, toinen_kortti):
        """
        Yhdistää toinen_kortti-parametrin sisältämät kulkuoikeudet
        käsiteltävänä olevalle kortille. Toimintalogiikka määritelty
        tehtävänannossa.

        :param toinen_kortti: Kulkukortti, jonka kanssa oikeudet yhdistetään
        """

        skip = False
        # Lisää toisen kortin kulkualuekoodit.
        for x in toinen_kortti.anna_kulkualuekoodit():
            # Jos kortissa on jo toisen kortin aluekoodi.

            for y in self.__kulkualueet:
                if x.startswith(y) and len(x) > len(y):
                    skip = True
                    break
                else:
                    continue

            # Siirry seuraavaan koodiin, jos kortissa on jo laajempi aluekoodi.
            if skip:
                skip = False
                continue

            self.__kulkualueet = \
                sievennä_kulkuoikeuslista(x, self.__kulkualueet)

        self.__kulkualueet.sort()  # Järjesta koodit aakkosjärjestykseen


def pääsytesti(kulkuoikeus, tutkittava_alue):
    """
    Funktio tutkii oikeuttaako tietty kulkuoikeus pääsyn
    tutkittavana olevaan huoneeseen/alueelle.

    :param kulkuoikeus: Kulkuoikeus, jonka perusteella halutaan testata,
                       onko tutkittavalle_alueelle pääsyä.
    :param tutkittava_alue: Oikeuttaako parametri kulkuoikeus
                       pääsyyn tutkittavalle alueelle.
    :return: True, jos pääsy on sallittu, False muussa tapauksessa.
    """

    pituus = len(kulkuoikeus)
    tutkittava = kulkuoikeus

    if tutkittava != tutkittava_alue[0:pituus]:
        return False
    else:
        if tutkittava == tutkittava_alue[0:pituus]:
            if pituus <= len(tutkittava_alue):
                return True
        else:
            return False


def sievennä_kulkuoikeuslista(lisättävä_kulkualue, vanha_kulkuoikeuslista):
    """
    Kun vanhaan_kulkuoikeuslistaan halutaan lisätä uusi kulkualue,
    on syntyvä kulkukoikeuslista sievennettävä siten, että kaikki
    lisättyä kulkualuetta suppeammat alueet poistetaan listalta
    (tehtävänannon esimerkki 5.2).  Koska tämä toimenpide on
    edellisellä toteutuskerralla osoittautunut kovin haastavaksi,
    tämä funktio hoitaa sen nyt kuntoon ilman ongelmia.

    Huomaa aivan erityisesti, että tätä funktiota on tarkoitus kutsua vain,
    kun jo tiedetään, että uusi kulkualue halutaan lisätä kulkukortille.

    Jos esimerkiksi lisättävä_kulkualue on "TE" ja
    vanha_kulkuoikeuslista on [ "S", "TE-110", "K2110", "TE-210" ]
    Funktio palauttaa listan [ "S", "K2110", "TE" ]

    :param lisättävä_kulkualue: Lisättäväksi haluttu kulkualue.
    :param vanha_kulkuoikeuslista: Tämänhetkiset kulkuoikeudet.
    :return: Kulkualuelista, joka saadaan kun vanhasta kulkukoikeuslistasta
             on poistettu kaikki lisättävää kulkualuetta suppeammat (ja saman-
             laajuiset kulkualueet), minkä jälkeen lisättävä_kulkualue on
             liitetty saadun supistetun listan loppuun.
    """

    suodatetut = []

    for alue in vanha_kulkuoikeuslista:
        if not pääsytesti(lisättävä_kulkualue, alue):
            suodatetut.append(alue)

    suodatetut.append(lisättävä_kulkualue)

    return suodatetut


def lue_tiedosto(tiedoston_nimi):
    """
    Lukee tiedoston sisällön ja tallentaa sen ohjelman muistiin listana.
    Jos tiedostoa ei löydy, ohjelma antaa virheilmoituksen.

    :param tiedoston_nimi: Luettavan tiedoston nimi
    :return: Tiedoston sisältö listana riveittäin.
    """
    tiedoston_sisältö = []

    try:
        tiedosto = open(tiedoston_nimi, "r", encoding="utf-8")

        for rivi in tiedosto:
            rivi = rivi.rstrip()
            tiedoston_sisältö.append(rivi)

        tiedosto.close()
    except OSError:
        print("Virhe: tiedostoa ei saa luettua.")

    return tiedoston_sisältö


def main():
    kulkutiedot_sanakirja = {}  # Luo sanakirja kulkukorttiolioille
    kulkutiedot_tiedosto = lue_tiedosto("kulkutiedot.txt")

    for rivi in kulkutiedot_tiedosto:
        # Jaa rivi kolmeen osaan: tunniste;nimi;kulkualuekoodit
        tiedot = rivi.split(";")
        tunniste = tiedot[0]  # Kortin tunniste
        nimi = tiedot[1]  # Kortin käyttäjän nimi

        # Tee kulkualuekoodeista lista, josta tyhjät koodit on suodatettu
        kulkualueet = sorted(list(filter(None, tiedot[2].split(","))))

        # Luo kulkukorttiolio
        kulkutiedot_sanakirja[tunniste] = Kulkukortti(tunniste, nimi)

        # Lisää kulkukorttiolioon kulkualuekoodit.
        for alue in kulkualueet:
            kulkutiedot_sanakirja[tunniste].lisää_kulkualue(alue)

    while True:
        rivi = input("komento> ")

        if rivi == "":
            break

        osat = rivi.split()
        käsky = osat[0]

        # Listaa kaikki kulkukortit kulkukorttisanakirjasta.
        if käsky == "lista" and len(osat) == 1:
            for x in sorted(kulkutiedot_sanakirja):
                kulkutiedot_sanakirja[x].tulosta_tiedot()

        # Listaa yksittäisen kortin tiedot.
        elif käsky == "tiedot" and len(osat) == 2:
            tunniste = osat[1]
            if tunniste in kulkutiedot_sanakirja:
                kulkutiedot_sanakirja[tunniste].tulosta_tiedot()
            else:
                print("Virhe: tuntematon tunniste.")

        # Tarkista onko kortilla pääsy alueelle.
        elif käsky == "kulku" and len(osat) == 3:
            tunniste = osat[1]
            alue = osat[2]

            # Onko tunniste olemassa?
            if tunniste in kulkutiedot_sanakirja:
                on_pääsy = kulkutiedot_sanakirja[tunniste].tarkista_pääsy(alue)

                if on_pääsy:
                    print("Kortilla " + tunniste + " ( " +
                          kulkutiedot_sanakirja[tunniste].anna_nimi() + " ) "
                          + "on kulkuoikeus huoneeseen " + alue)
                else:
                    print("Kortilla " + tunniste + " ( " +
                          kulkutiedot_sanakirja[tunniste].anna_nimi() + " ) "
                          + "ei kulkuoikeutta huoneeseen " + alue)

            else:
                print("Virhe: tuntematon tunniste.")

        # Lisää korttiin kulkualuekoodi.
        elif käsky == "lisää" and len(osat) == 3:
            tunniste = osat[1]
            alue = osat[2]

            # Onko tunniste olemassa?
            if tunniste in kulkutiedot_sanakirja:
                kulkutiedot_sanakirja[tunniste].lisää_kulkualue(alue)
            else:
                print("Virhe: tuntematon tunniste.")

        # Lisää kohdekorttiin lähdekortin kulkualuekoodit.
        elif käsky == "yhdistä" and len(osat) == 3:
            kohdekortti = osat[1]
            lähdekortti = osat[2]

            # Onko tunnisteet olemassa?
            if kohdekortti in kulkutiedot_sanakirja \
                    and lähdekortti in kulkutiedot_sanakirja:
                kulkutiedot_sanakirja[kohdekortti]. \
                    yhdistä_kulkukortti(kulkutiedot_sanakirja[lähdekortti])
            else:
                print("Virhe: tuntematon tunniste.")

        else:
            print("Virhe: Väärä syöte, yritä uudelleen")


main()
