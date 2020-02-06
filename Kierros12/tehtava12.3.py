# TIE-02100 Johdanto Ohjelmointiin
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

        self.__tunniste = tunniste
        self.__nimi = nimi
        self.__kulkualueet = []

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

        kulkualueet = ','.join(self.__kulkualueet)
        print(self.__tunniste + ", " + self.__nimi + ", " + "kulkualueet: "
              + kulkualueet)

    def anna_nimi(self):
        """
        :return: Palauttaa kulkukortille talletetun henkilön nimen.
        """

        return self.__nimi

    def anna_tunniste(self):
        """
        :return: Palauttaa kulkukortin tunnisteen.
        """
        return self.__tunniste

    def anna_kulkualuelista(self):
        """
        :return: Palauttaa listan kulkukortille valtuutetuista alueista.
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

        pass  # TODO: Toteuta tämäkin metodi

    def lisää_kulkualue(self, uusi_alue):
        """
        Funktio lisää uuden alueen kulkukortin oikeuksiin tehtävänannossa
        määritellyn säännön mukaisesti. Funktio ei saa tulostaa näytölle mitään.

        TÄMÄN METODIN TOIMINTA TESTATAAN ERIKSEEN AUTOMAATTITESTISSÄ.
        MIKÄLI SE EI TOIMI MÄÄRITTELYN MUKAISESTI, TESTIT EPÄONNISTUVAT.
        MYÖS PARAMETRIEN MUUTTAMINEN JOHTAA AUTOMAATTITESTIEN
        EPÄONNISTUMISEEN.

        :param uusi_alue: Lisättävä kulkualue
        """

        self.__kulkualueet = \
            sievennä_kulkuoikeuslista(uusi_alue, self.__kulkualueet)

    def yhdistä_kulkukortti(self, toinen_kortti):
        """
        Yhdistää toinen_kortti-parametrin sisältämät kulkuoikeudet
        käsiteltävänä olevalle kortille. Toimintalogiikka määritelty
        tehtävänannossa.

        :param toinen_kortti: Kulkukortti, jonka kanssa oikeudet yhdistetään
        """

        pass  # TODO: Toteuta tämäkin metodi



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

    if kulkuoikeus in tutkittava_alue:
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
    Lukee rivi riviltä tiedoston sisällön ja palauttaa sen sanakirjana, jossa
    jokainen luettu tunniste määrittelee kortin käyttäjän ja kulkuoikeudet.
    :return: Tiedoston sisältö sanakirjana, jossa tunniste on avain.
             ja sen arvona on lista, jossa on käyttäjän nimi ja kulkuoikeudet.
    """
    sanakirja = {}

    try:
        tiedosto = open(tiedoston_nimi, "r", encoding="utf-8")

        for rivi in tiedosto:
            rivi = rivi.rstrip()  # Poista rivinvaihtomerkit

            # [0] = tunniste, [1] = nimi, [2] = kulkuoikeudet
            tiedosto_rivi = rivi.split(";")
            tunniste = tiedosto_rivi[0]
            nimi = tiedosto_rivi[1]

            # Suodata tyhjät merkkijonot kulkuoikeudet listasta.
            kulkualueet = sorted(
                list(filter(None, tiedosto_rivi[2].split(","))))

            # Jos ainakin yksi rivin sarakkeista on tyhjä, jatka seuraavaan.
            if tunniste == '' or nimi == '':
                continue

            # Lisää sanakirjaan tunniste ja sen tiedot
            sanakirja[tunniste] = [nimi, kulkualueet]

        tiedosto.close()
    except OSError:
        print("Virhe: tiedostoa ei saa luettua.")

    return sanakirja


def tiedot(tunniste, lista):
    """
    Tulostaa kulkukortin tiedot, jos käyttäjän antama tunniste löytyy.
    Muussa tapauksessa tulostaa virheilmoituksen.

    :param tunniste: Käyttäjän antama tunniste
    :param lista: Lista kulkukorttiolioista.
    :return:
    """
    löytynyt = False
    löydetty = None

    for x in lista:
        if x.anna_tunniste() != tunniste:
            continue
        else:
            löytynyt = True
            löydetty = x
            break

    if not löytynyt:
        print("Virhe: tuntematon tunniste.")
    else:
        löydetty.tulosta_tiedot()


def kulku(tunniste, alue, lista):
    löytynyt = False
    on_pääsy = False
    löydetty_tunniste = None

    for x in lista:
        if x.anna_tunniste() != tunniste:
            continue
        else:
            löytynyt = True
            löydetty_tunniste = x
            break

    if not löytynyt:
        print("Virhe: tuntematon tunniste.")
        return

    kulkualueet = löydetty_tunniste.anna_kulkualuelista()

    for x in kulkualueet:
        if pääsytesti(alue, x):
            on_pääsy = True
            break
        else:
            continue

    if on_pääsy:
        print("Kortilla " + tunniste +
              " ( " + löydetty_tunniste.anna_nimi()
              + " ) on kulkuoikeus huoneeseen " + alue)
    else:
        print("Kortilla " + tunniste +
              " ( " + löydetty_tunniste.anna_nimi()
              + " ) ei kulkuoikeutta huoneeseen " + alue)

def main():
    kulkutiedot_tiedosto = lue_tiedosto("kulkutiedot.txt")
    kulkutiedot_lista = []  # Lista kulkukorttiolioille
    idx = 0  # Listaindeksi

    # Lisää kulkutiedot_listaan kulkukorttioliot
    for x in sorted(kulkutiedot_tiedosto):
        kulkutiedot_lista.append(Kulkukortti(x, kulkutiedot_tiedosto[x][0]))

        for y in kulkutiedot_tiedosto[x][1]:
            kulkutiedot_lista[idx].lisää_kulkualue(y)

        idx += 1

    while True:
        rivi = input("komento> ")

        if rivi == "":
            break

        osat = rivi.split()
        käsky = osat[0]

        if käsky == "lista" and len(osat) == 1:
            for x in kulkutiedot_lista:
                x.tulosta_tiedot()

        elif käsky == "tiedot" and len(osat) == 2:
            tunniste = osat[1]
            tiedot(tunniste, kulkutiedot_lista)

        elif käsky == "kulku" and len(osat) == 3:
            tunniste = osat[1]
            alue = osat[2]
            kulku(tunniste, alue, kulkutiedot_lista)

        elif käsky == "lisää" and len(osat) == 3:
            tunniste = osat[1]
            alue = osat[2]
            # TODO: Suorita tässä käsky lisää

        elif käsky == "yhdistä" and len(osat) == 3:
            kohdekortti = osat[1]
            lähdekortti = osat[2]
            # TODO: Suorita tässä käsky yhdistä

        else:
            print("Virhe: Väärä syöte, yritä uudelleen")


main()
