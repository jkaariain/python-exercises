# TIE-02100 Johdatus ohjelmointiin
# Graafisen käyttöliittymän suunnitteleminen ja toteuttaminen - Ristinolla
# Jaakko Kääriäinen

"""
Ristinolla - versio 1.0
Grafiikka, ohjelmointi: Jaakko Kääriäinen

Pelin kuvaus:

Ristinolla on kahden pelaajan peli, jossa pelaajat piirtävät vuorotellen
oman merkkinsä: ristin tai ympyrän. Tavoitteena on saada kolme omaa merkkiä
joko pysty, rivi tai diagonaaliselle riville. Pelin voittaja on se, joka
toteuttaa ensimmäisenä tämän tavoitteen. Jos lauta on täynnä eikä kumpikaan
pelaaja ole muodostanut riviä, jossa on kolme samaa merkkiä, kyseessä on
tasapeli.

Toteutus:

Ohjelman käyttöliittymä koostuu seuraavista käyttöliittymäkomponenteista:
Canvas, Label, TopLevel, Menu, MessageBox

Pelilauta on toteutettu käyttäen Tkinterin Canvas käyttöliittymäkomponenttia,
jonka avulla pelilaudan grafiikan piirtäminen onnistuu. Grafiikan piirtämisen
lisäksi Canvas-komponentti ottaa vastaan hiiren vasemman painikkeen klikkauksia
ja numeronäppäinten painalluksia. Nämä käsitellään ns. callback-funktioilla,
joilla peli varsinaisesti toimii. Kun peli on pelattu loppuun, peli julistaa
voittajan tai tasapelin MessageBox-komponentilla (Huom. tilannepalkissa ei ole
tekstiä, jossa mainitaan pelaajan vuoro.). Sen jälkeen ohjelma kysyy
käyttäjältä, että haluaako hän aloittaa uuden pelin. Vastaamalla 'Kyllä'
ohjelma korvaa laudalla olevat merkit tyhjillä ja tilannepalkista voi nähdä
jälleen pelaajan vuoron.

Pelilaudan yläpuolella oleva tilannepalkki on Label-komponentti, joka sisältää
tekstinä pelaajan vuoron ja pistetilaston pelatuista peleistä. Pelaajan vuoroa
ei näy silloin, kun peli on ohi.

Ikkunan ylävalikko on toteutettu Menu-komponentilla.

Valikon hierarkia on seuraavanlainen:

* Peli
    - Uusi peli
    - Nolla pistetilasto
    - Lopeta
* Ohje
    - Pelin säännöt
    - Ohjauskomennot
    - Tietoja Ristinollasta

Peli-valikon toiminnot vaikuttavat sekä pelilautaan että tilannepalkkiin.
Lopeta tominto toimii samalla tavalla kuin ikkunan X-painike.

Jokainen Ohje-valikon toiminto avaa erillisen ikkunan, joka sisältää sille
tarkoitetun tekstin (Huom. ohjelma luo vain yhden ikkunan per toiminto.) Pelin
säännöt sisältää samanlaisen kuvauksen kuin tässä tiedostossa. Ohjauskomennot
kertoo, mitkä näppäimet toimivat tässä ohjelmassa (Hiiren vasen painike
ja numeronäppäimet 1-9). Lisäksi Tietoja Ristinollasta sisältää ohjelmaversion
sekä tekijän nimen. Ikkunat kehitetään Toplevel-komponentilla. Toplevel avaa
uuden ikkunan, jolla on samanlaiset ominaisuudet kuin tavallisella ikkunalla.
Eli siihen voi lisätä samanlaisia komponentteja kuin pääikkunaan. Tässä
projektissa ne kuitenkin sisältävät vain yhden Label-komponentin ja painikkeen.

Ikkunoiden olemassaolo käsitellään niille tarkoitetuilla totuusarvoilla, jotka
määrittelevät, onko ikkuna auki vai ei. Lisäksi, ikkunoiden X painikkeisiin on
kytketty funktiot, jotka suoritetaan silloin, kun ohjelma vastaanottaa
tapahtuman WM_DELETE_WINDOW. WM_DELETE_WINDOW tapahtuu silloin, kun käyttäjä
klikkaa ikkunan X painiketta. Jokainen funktio asettaa sille kuuluvan
totuusarvon arvoon False ja ikkuna suljetaan. Funktio suoritetaan myös silloin,
kun käyttäjä klikkaa ikkunan OK painiketta.

Tekijä tähtäsi skaalautuvaan versioon projektista.
"""

from tkinter import *
from tkinter import messagebox

# Pelin asetukset
LAATAN_SIVUN_PITUUS = 128
LAUDAN_LEVEYS = 3  # Älä muuta
LAUDAN_KORKEUS = 3  # Älä muuta

PELAAJA_X = "X"
PELAAJA_O = "O"
TYHJÄ = " "
VIIVALEVEYS = 10  # Viivojen leveys piirtämisessä

# Koordinaatit numeronäppäimille. Älä muuta
# Koordinaatit vastaavat numeronäppäimistön painikkeita alla olevan kuvan
# mukaisesti.
#
# 7|8|9
# -+-+-
# 4|5|6
# -+-+-
# 1|2|3
NÄPPÄIN_KOORDINAATIT = {1: (2, 0), 2: (2, 1), 3: (2, 2), 4: (1, 0), 5: (1, 1),
                        6: (1, 2), 7: (0, 0), 8: (0, 1), 9: (0, 2)}

# Kuvion etäisyys ristikon reunoista
OFFSET = 16


class Tilannepalkki:
    """
    Tämä olio ylläpitää tilannepalkin tekstiä, joka sijaitsee pelilaudan
    yläpuolella
    """

    def __init__(self, pisteet, vuoro, käli):
        if vuoro != "":
            pelaajan_vuoro_teksti = "Pelaajan " + vuoro + " vuoro | "
        else:
            pelaajan_vuoro_teksti = ""

        teksti = "{0}Pisteet: {1}: {2} {3}: {4} Tasapeli: {5}".format(
            pelaajan_vuoro_teksti, PELAAJA_X, str(pisteet[PELAAJA_X]),
            PELAAJA_O, str(pisteet[PELAAJA_O]), str(pisteet["tasapeli"]))

        self.__tilannepalkki = Label(käli, text=teksti, font=('Arial', 12))
        self.__tilannepalkki.pack()

    def päivitä(self, pisteet, vuoro):
        """
        Päivittää tilannepalkin tekstin. Jos vuoro on tyhjä merkkijono,
        kirjoita pelkästään pisteet tilannepalkkiin
        :param pisteet: Pistetilasto
        :param vuoro: Pelaajan vuoro
        :return:
        """
        if vuoro != "":
            pelaajan_vuoro_teksti = "Pelaajan " + vuoro + " vuoro | "
        else:
            pelaajan_vuoro_teksti = ""

        teksti = "{0}Pisteet: {1}: {2} {3}: {4} Tasapeli: {5}".format(
            pelaajan_vuoro_teksti, PELAAJA_X, str(pisteet[PELAAJA_X]),
            PELAAJA_O, str(pisteet[PELAAJA_O]), str(pisteet["tasapeli"]))

        self.__tilannepalkki.config(text=teksti)


class Laatta:
    def __init__(self, merkki, rivi, sarake):
        self.__merkki = str(merkki)

        # Laatan koordinaatit
        self.__rivi = rivi
        self.__sarake = sarake

    def aseta_merkki(self, merkki):
        self.__merkki = merkki

    def piirrä(self, piirtoalue):
        """
        Piirtää laatalle asetetun merkin ikkunaan
        :param piirtoalue: Pelilaudan piirtoalue
        :return:
        """
        # Piirrä risti
        if self.__merkki == PELAAJA_X:
            piirtoalue.create_line(
                self.__sarake * LAATAN_SIVUN_PITUUS + OFFSET,
                self.__rivi * LAATAN_SIVUN_PITUUS + OFFSET,
                self.__sarake * LAATAN_SIVUN_PITUUS
                + LAATAN_SIVUN_PITUUS - OFFSET,
                self.__rivi * LAATAN_SIVUN_PITUUS
                + LAATAN_SIVUN_PITUUS - OFFSET,
                width=VIIVALEVEYS)

            piirtoalue.create_line(
                self.__sarake * LAATAN_SIVUN_PITUUS + OFFSET,
                self.__rivi * LAATAN_SIVUN_PITUUS +
                LAATAN_SIVUN_PITUUS - OFFSET,
                self.__sarake * LAATAN_SIVUN_PITUUS
                + LAATAN_SIVUN_PITUUS - OFFSET,
                self.__rivi * LAATAN_SIVUN_PITUUS + OFFSET, width=VIIVALEVEYS)

        # Piirrä ympyrä
        elif self.__merkki == PELAAJA_O:
            piirtoalue.create_oval(
                self.__sarake * LAATAN_SIVUN_PITUUS + OFFSET,
                self.__rivi * LAATAN_SIVUN_PITUUS + OFFSET,
                self.__sarake * LAATAN_SIVUN_PITUUS
                + LAATAN_SIVUN_PITUUS - OFFSET,
                self.__rivi * LAATAN_SIVUN_PITUUS
                + LAATAN_SIVUN_PITUUS - OFFSET,
                width=VIIVALEVEYS)

    def __str__(self):
        return self.__merkki


class Pelilauta:
    """
    Ohjelman ydinolio
    """

    def __init__(self, käli):
        """
        Pelin rakentajafunktio.
        :param käli: Käyttöliittymä, johon pelilauta liitetään
        """
        self.__laatat = []
        self.alusta_lauta()

        # Laudan piirtoalue
        self.__piirtoalue = Canvas(käli,
                                   width=LAUDAN_LEVEYS * LAATAN_SIVUN_PITUUS,
                                   height=LAUDAN_KORKEUS * LAATAN_SIVUN_PITUUS,
                                   highlightthickness=0, bd=0, relief='ridge')
        self.__piirtoalue.focus_set()
        self.__pelaajan_vuoro = PELAAJA_X
        self.__peli_ohi = False
        self.__voittaja = ""
        self.__pisteet = {PELAAJA_X: 0, PELAAJA_O: 0, "tasapeli": 0}
        self.__tilannepalkki = Tilannepalkki(self.__pisteet,
                                             self.__pelaajan_vuoro, käli)

        def näppäin_tapahtuma(event):
            """
            Tämä funktio käsittelee kaikki käyttäjän antamat
            näppäinpainallukset. Kun käyttäjä painaa numeronäppäintä, funktio
            asettaa vuorossa olevan merkin numeron koordinaattien paikalle.
            Esim. 1 on koordinaateissa (2, 0)
            :param event:
            :return:
            """

            # Jos peli on ohi, lopeta metodin toiminta
            if self.__peli_ohi:
                return

            # Tallenna näppäin-muuttujaan painettu näppäin
            näppäin = event.char

            # Jos näppäin ei ole numero, lopeta metodin toiminta
            try:
                numero = int(näppäin)
            except ValueError:
                return

            # Numerolla 0 ei ole omia koordinaatteja
            if numero == 0:
                return

            # Aseta käsiteltävä laatta painettu_laatta muuttujaan
            # näppäinkoordinaattien perusteella
            laatta_y, laatta_x = NÄPPÄIN_KOORDINAATIT[numero]
            painettu_laatta = self.__laatat[laatta_y][laatta_x]

            # Jos klikattu laatta on tyhjä, aseta vuorossa olevan pelaajan
            # merkki.
            if str(painettu_laatta) == TYHJÄ:
                self.__laatat[laatta_y][laatta_x].aseta_merkki \
                    (self.__pelaajan_vuoro)

                # Vaihda pelaajaa
                if self.__pelaajan_vuoro == PELAAJA_X:
                    self.__pelaajan_vuoro = PELAAJA_O
                else:
                    self.__pelaajan_vuoro = PELAAJA_X

                # Päivitä lauta
                self.piirrä()

            self.tarkista_lauta(laatta_x, laatta_y)
            self.päivitä_tilannepalkki()

            if self.__peli_ohi:
                self.julista_voittaja()

        def klikkaus_tapahtuma(event):
            """
            Tämä funktio käsittelee kaikki käyttäjän antamat klikkaukset.
            Kun käyttäjä klikkaa tyhjää laattaa, funktio asettaa vuorossa
            olevan merkin tyhjän paikalle.
            :param event:
            :return:
            """
            # Jos peli on ohi, lopeta metodin toiminta
            if self.__peli_ohi:
                return

            # Aseta klikatun laatan koordinaatit
            laatta_x = event.x // LAATAN_SIVUN_PITUUS
            laatta_y = event.y // LAATAN_SIVUN_PITUUS

            # Jos pelaaja onnistuu klikkamaan sitä laattaa, jonka ei pitäisi
            # olla olemassa, lopeta metodin toiminta.
            try:
                klikattu_laatta = self.__laatat[laatta_y][laatta_x]
            except IndexError:
                return

            # Jos klikattu laatta on tyhjä, aseta vuorossa olevan pelaajan
            # merkki.
            if str(klikattu_laatta) == TYHJÄ:
                self.__laatat[laatta_y][laatta_x].aseta_merkki \
                    (self.__pelaajan_vuoro)

                # Vaihda pelaajaa
                if self.__pelaajan_vuoro == PELAAJA_X:
                    self.__pelaajan_vuoro = PELAAJA_O
                else:
                    self.__pelaajan_vuoro = PELAAJA_X

                # Päivitä lauta
                self.piirrä()

            # Tarkista voittotilanne ja päivitä tilannepalkki
            self.tarkista_lauta(laatta_x, laatta_y)
            self.päivitä_tilannepalkki()

            # Jos peli on ohi, julista voittaja
            if self.__peli_ohi:
                self.julista_voittaja()

        # <Button-1> == Hiiren vasen painike.
        # <Key> == Mikä tahansa näppäimistön painike.
        self.__piirtoalue.bind("<Button-1>", klikkaus_tapahtuma)
        self.__piirtoalue.bind("<Key>", näppäin_tapahtuma)
        self.__piirtoalue.pack()

    def alusta_lauta(self):
        """
        Korvaa kaikki laatat tyhjillä laatoilla ja aloittaa uuden pelin
        :return:
        """
        self.__peli_ohi = False
        self.__voittaja = ""
        self.__laatat = []  # Tyhjennä asetetut laatat
        temp = []  # Varastoi sarakkeissa olevat laatat per rivi

        for rivi in range(0, LAUDAN_KORKEUS):
            for sarake in range(0, LAUDAN_LEVEYS):
                temp.append(Laatta(TYHJÄ, rivi, sarake))
            self.__laatat.append(temp)
            temp = []

    def päivitä_tilannepalkki(self):
        """
        Päivittää tilannepalkin tekstin.
        :return:
        """
        if self.__peli_ohi:
            self.__tilannepalkki.päivitä(self.__pisteet, "")
        else:
            self.__tilannepalkki.päivitä(self.__pisteet, self.__pelaajan_vuoro)

    def nollaa_pisteet(self):
        """
        Resetoi pisteet nolliin.
        :return:
        """
        self.__pisteet = {PELAAJA_X: 0, PELAAJA_O: 0, "tasapeli": 0}
        self.päivitä_tilannepalkki()

    def onko_lauta_täynnä(self):
        """
        Apumetodi tarkista_lauta-metodille.
        Palauttaa totuusarvon, joka kertoo, onko pelilauta täynnä vai ei.
        :return: Onko pelilauta täynnä?
        """
        for rivi in range(0, LAUDAN_KORKEUS):
            for sarake in range(0, LAUDAN_LEVEYS):
                if str(self.__laatat[rivi][sarake]) != TYHJÄ:
                    continue
                else:
                    return False

        return True

    def julista_voittaja(self):
        """
        Julistaa pelin voittajan tai tasapelin näyttämällä erillisen ikkunan.
        Onnittelun jälkeen, ohjelma kysyy käyttäjältä, että haluaako hän
        aloittaa uuden pelin.
        :return:
        """

        # Julista voittaja tai tasapeli
        if self.__voittaja != "":
            viesti = "Pelaaja " + self.__voittaja + " voitti!"
            self.__pisteet[self.__voittaja] += 1
            self.__tilannepalkki.päivitä(self.__pisteet, "")
            messagebox.showinfo("Peli ohi!", viesti)
        else:
            viesti = "Tasapeli!"
            self.__pisteet["tasapeli"] += 1
            self.__tilannepalkki.päivitä(self.__pisteet, "")
            messagebox.showinfo("Peli ohi!", viesti)

        # Haluaako käyttäjä aloittaa uuden pelin?
        valinta = messagebox.askyesno("Uudestaan?",
                                      "Haluatko aloittaa uuden pelin?")

        # Jos käyttäjä valitsee 'Kyllä', aloita uusi peli
        # Jos käyttäjä valitsee 'Ei', älä tee mitään
        if valinta:
            self.alusta_lauta()
            self.päivitä_tilannepalkki()
            self.piirrä()

    def tarkista_lauta(self, x, y):
        """
        Tarkastaa onko laudalla riviä, jossa on kolme samaa merkkiä.
        Tämä metodi siis määrää milloin peli on päättynyt.
        :param x: Asetetun laatan x-koordinaatti
        :param y: Asetetun laatan y-koordinaatti
        :return:
        """

        # Tarkista pystyrivi
        if str(self.__laatat[0][x]) == \
                str(self.__laatat[1][x]) == \
                str(self.__laatat[2][x]):
            self.__voittaja = str(self.__laatat[0][x])
            self.__peli_ohi = True

        # Tarkista vaakarivi
        if str(self.__laatat[y][0]) == \
                str(self.__laatat[y][1]) == \
                str(self.__laatat[y][2]):
            self.__voittaja = str(self.__laatat[y][0])
            self.__peli_ohi = True

        # Tarkista diagonaalirivi (Vasen yläkulma-Oikea alakulma)
        if x == y and str(self.__laatat[0][0]) == \
                str(self.__laatat[1][1]) == \
                str(self.__laatat[2][2]):
            self.__voittaja = str(self.__laatat[0][0])
            self.__peli_ohi = True

        # Tarkista diagonaalirivi (Oikea yläkulma-Vasen alakulma)
        if x + y == 2 and str(self.__laatat[0][2]) == \
                str(self.__laatat[1][1]) == \
                str(self.__laatat[2][0]):
            self.__voittaja = str(self.__laatat[0][2])
            self.__peli_ohi = True

        # Julista peli päättyneeksi, jos lauta on täynnä eikä laudalla ole
        # yhtään riviä, jossa on kolme samaa merkkiä
        if self.onko_lauta_täynnä():
            self.__peli_ohi = True

    def piirrä(self):
        """
        Piirtää pelilaudan. Ensin metodi tyhjentää piirtoalueen, jotta
        vältytään muistivuodolta. Sitten se piirtää ristikon, jonka jälkeen
        piirretään jokainen pelilaudan laatta.
        :return:
        """
        # Tyhjennä piirtoalue
        self.__piirtoalue.delete(ALL)

        # Piirrä ristikko
        self.__piirtoalue.create_line(0, LAATAN_SIVUN_PITUUS,
                                      LAATAN_SIVUN_PITUUS * LAUDAN_LEVEYS,
                                      LAATAN_SIVUN_PITUUS, width=VIIVALEVEYS)
        self.__piirtoalue.create_line(0, LAATAN_SIVUN_PITUUS * 2,
                                      LAATAN_SIVUN_PITUUS * LAUDAN_LEVEYS,
                                      LAATAN_SIVUN_PITUUS * 2,
                                      width=VIIVALEVEYS)
        self.__piirtoalue.create_line(LAATAN_SIVUN_PITUUS, 0,
                                      LAATAN_SIVUN_PITUUS,
                                      LAATAN_SIVUN_PITUUS * LAUDAN_KORKEUS,
                                      width=VIIVALEVEYS)
        self.__piirtoalue.create_line(LAATAN_SIVUN_PITUUS * 2, 0,
                                      LAATAN_SIVUN_PITUUS * 2,
                                      LAATAN_SIVUN_PITUUS * LAUDAN_KORKEUS,
                                      width=VIIVALEVEYS)

        # Piirrä laatat
        for rivi in range(0, LAUDAN_KORKEUS):
            for sarake in range(0, LAUDAN_LEVEYS):
                self.__laatat[rivi][sarake].piirrä(self.__piirtoalue)


class Käyttöliittymä:
    def __init__(self):
        """
        Käyttöliittymän rakentajametodi.

        Kun käyttöliittymä olio on luotu, se konfiguroi ikkunan asetukset ja
        yhdistää jokaisen valikon toiminnot funktioihin.

        Tämän jälkeen pelilauta piirretään.
        """
        self.__säännöt_ikkuna_avoin = False
        self.__tiedot_ikkuna_avoin = False
        self.__ohjauskomennot_ikkuna_avoin = False

        self.__ikkuna = Tk()
        self.__ikkuna.title("Ristinolla")

        # Poista käytöstä ikkunan koon muuttaminen
        self.__ikkuna.resizable(0, 0)

        self.__pelilauta = Pelilauta(self.__ikkuna)

        # Valikkopalkki
        self.__päävalikko = Menu(self.__ikkuna, tearoff=0)

        # Pelivalikko
        self.__pelivalikko = Menu(self.__päävalikko, tearoff=0)
        self.__pelivalikko.add_command(label="Uusi peli",
                                       command=self.uusi_peli)
        self.__pelivalikko.add_command(label="Nollaa pistetilasto",
                                       command=self.__pelilauta.nollaa_pisteet)
        self.__pelivalikko.add_separator()
        self.__pelivalikko.add_command(label="Lopeta", command=self.lopeta)
        self.__päävalikko.add_cascade(label="Peli", menu=self.__pelivalikko)

        # Ohjevalikko
        self.__ohjevalikko = Menu(self.__päävalikko, tearoff=0)
        self.__ohjevalikko.add_command(label="Pelin säännöt",
                                       command=self.näytä_säännöt)
        self.__ohjevalikko.add_command(label="Ohjauskomennot",
                                       command=self.näytä_ohjauskomennot)
        self.__ohjevalikko.add_separator()
        self.__ohjevalikko.add_command(label="Tietoja Ristinollasta",
                                       command=self.näytä_tiedot)
        self.__päävalikko.add_cascade(label="Ohje", menu=self.__ohjevalikko)

        # Pelilauta
        self.__pelilauta.piirrä()

    def uusi_peli(self):
        """
        Aloittaa uuden pelin tyhjentämällä laudan sekä päivittää tilannepalkin.
        Tyhjentämisen jälkeen lauta on tyhjä ja tilannepalkissa näkyy pelaajan
        vuoro.
        :return:
        """
        self.__pelilauta.alusta_lauta()
        self.__pelilauta.päivitä_tilannepalkki()
        self.__pelilauta.piirrä()

    def näytä_säännöt(self):
        """
        Näyttää erillisen ikkunan, jossa lukee pelin säännöt.
        Metodi sallii vain yhden ikkunan olla näkyvissä
        :return:
        """
        if self.__säännöt_ikkuna_avoin:
            return

        def sulje():
            self.__säännöt_ikkuna_avoin = False
            ikkuna.destroy()

        ikkuna = Toplevel()
        ikkuna.resizable(0, 0)
        ikkuna.protocol('WM_DELETE_WINDOW', sulje)

        self.__säännöt_ikkuna_avoin = True

        ikkuna.title("Pelin säännöt")
        teksti = "Ristinolla on kahden pelaajan peli, jossa pelaajat\n" \
                 "piirtävät vuorotellen oman merkkinsä: ristin tai ympyrän.\n" \
                 "Tavoitteena on saada kolme omaa merkkiä joko pysty, rivi\n" \
                 "tai diagonaaliselle riville. Pelin voittaja on se, joka\n" \
                 "toteuttaa ensimmäisenä tämän tavoitteen. Jos lauta on\n" \
                 "täynnä eikä kumpikaan pelaaja ole muodostanut riviä,\n" \
                 "jossa on kolme samaa merkkiä, kyseessä on tasapeli."
        Label(ikkuna, text=teksti).pack()
        Button(ikkuna, text="OK", command=sulje).pack()

    def näytä_tiedot(self):
        """
        Näyttää ohjelman tiedot omassa ikkunassaan.
        Metodi sallii vain yhden ikkunan olla näkyvissä
        :return:
        """
        if self.__tiedot_ikkuna_avoin:
            return

        def sulje():
            self.__tiedot_ikkuna_avoin = False
            ikkuna.destroy()

        ikkuna = Toplevel()
        ikkuna.resizable(0, 0)
        ikkuna.protocol('WM_DESTROY_WINDOW', sulje)
        self.__tiedot_ikkuna_avoin = True

        ikkuna.title("Tietoja: Ristinolla")
        teksti = "Ristinolla - versio 1.0\nGrafiikka, ohjelmointi: " \
                 "Jaakko Kääriäinen"
        Label(ikkuna, text=teksti).pack()
        Button(ikkuna, text="OK", command=sulje).pack()

    def näytä_ohjauskomennot(self):
        """
        Näyttää ohjelman tiedot omassa ikkunassaan.
        Metodi sallii vain yhden ikkunan olla näkyvissä
        :return:
        """
        if self.__ohjauskomennot_ikkuna_avoin:
            return

        def sulje():
            self.__ohjauskomennot_ikkuna_avoin = False
            ikkuna.destroy()

        ikkuna = Toplevel()
        ikkuna.resizable(0, 0)
        ikkuna.protocol('WM_DESTROY_WINDOW', sulje)
        self.__ohjauskomennot_ikkuna_avoin = True

        ikkuna.title("Ohjauskomennot")
        teksti = "Hiiren vasen painike sekä numeronäppäimet 1-9"
        Label(ikkuna, text=teksti).pack()
        Button(ikkuna, text="OK", command=sulje).pack()

    def käynnistä(self):
        """
        Käynnistää ohjelman
        :return:
        """
        self.__ikkuna.config(menu=self.__päävalikko)
        self.__ikkuna.mainloop()

    def lopeta(self):
        self.__ikkuna.destroy()


def main():
    """
    Main-funktio
    :return:
    """
    käli = Käyttöliittymä()
    käli.käynnistä()


main()
