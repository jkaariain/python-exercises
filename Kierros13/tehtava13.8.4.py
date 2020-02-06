from tkinter import *
import random
import time

NOPPAKUVAT = ["1.gif", "2.gif", "3.gif", "4.gif", "5.gif", "6.gif"]

PELAAJIEN_LKM = 2
NOPPIEN_LKM = 3
HEITTOVUOROJA = 2


class Noppapeli:
    def __init__(self):
        self.__ikkuna = Tk()
        self.__ikkuna.title("Noppapeli")

        self.__pelivuoro = 0
        self.__pelaajien_pisteet = [0] * PELAAJIEN_LKM

        self.__noppakuvat = []
        for kuvatiedosto in NOPPAKUVAT:
            kuva = PhotoImage(file=kuvatiedosto)
            self.__noppakuvat.append(kuva)

        # Nämä tekstit vain asetetaan käyttöliittymään. Niitä ei tarvitse
        # muokata pelin aikana, joten ei talleteta olion kenttiin.
        for i in range(PELAAJIEN_LKM):
            Label(self.__ikkuna,
                  text="Pelaajan " + str(i + 1) + " pistetilanne:") \
                .grid(row=i + 1, column=0, sticky=E)

        self.__infoLabel = Label(self.__ikkuna)
        self.__infoLabel.grid(row=PELAAJIEN_LKM + 1, column=0, columnspan=2)

        self.__pistelabelit = []
        for i in range(PELAAJIEN_LKM):
            uusi_label = Label(self.__ikkuna)
            uusi_label.grid(row=i + 1, column=1, sticky=W)
            self.__pistelabelit.append(uusi_label)

        self.__noppakuvalabelit = []
        for i in range(NOPPIEN_LKM):
            uusi_label = Label(self.__ikkuna)
            uusi_label.grid(row=0, column=2 + i)
            self.__noppakuvalabelit.append(uusi_label)

        self.__lukitusbuttonit = []
        for i in range(NOPPIEN_LKM):
            uusi_button = Button(self.__ikkuna,
                                 command=lambda x=i: self.muuta_nopan_tila(x))
            uusi_button.grid(row=1, column=2 + i)
            self.__lukitusbuttonit.append(uusi_button)

        self.__heitäButton = Button(self.__ikkuna, text="heitä",
                                    command=self.heitä)
        self.__heitäButton.grid(row=0, column=NOPPIEN_LKM + 2, sticky=W + E)
        self.__lopetavuoroButton = Button(self.__ikkuna, text="lopeta vuoro",
                                          command=self.lopeta_vuoro)
        self.__lopetavuoroButton.grid(row=1, column=NOPPIEN_LKM + 2,
                                      sticky=W + E)

        Button(self.__ikkuna, text="uusi peli", command=self.alusta_peli) \
            .grid(row=2, column=NOPPIEN_LKM + 2, sticky=W + E + N)
        Button(self.__ikkuna, text="lopeta", command=self.__ikkuna.destroy) \
            .grid(row=4, column=NOPPIEN_LKM + 2, sticky=W + E + S)

        self.alusta_peli()

    def alusta_peli(self):
        self.__pelivuoro = 0
        self.__heittokertoja = HEITTOVUOROJA
        self.__pelaajien_pisteet = [0] * PELAAJIEN_LKM
        self.__pelitilanneteksti = "Vuorossa pelaaja " + str(
            self.__pelivuoro + 1)

        # Talletetaan tieto, että noppia ei ole lukittu
        self.__nopat_käytössä = [True] * NOPPIEN_LKM

        # Tallennetaan myös noppien silmäluvut ohjelman laskentaa varten
        self.__silmäluvut = [1] * NOPPIEN_LKM

        # Asetetaan kaikkien noppakuvien kohdalle ykkönen
        for label in self.__noppakuvalabelit:
            label.configure(image=self.__noppakuvat[0])

        self.nollaa_lukitusnapit()

        self.päivitä_käyttöliittymän_tekstit()

    def nollaa_lukitusnapit(self):
        # Asetetaan lukitusnappulat alkutilaan
        for button in self.__lukitusbuttonit:
            button.configure(text="vapaa")  # Asetetaan nappulan teksti...
            button.configure(background="green")  # ... ja väri ...
            button.configure(state=NORMAL)  # ... ja aktivoidaan se.

        #self.__nopat_käytössä = [True] * NOPPIEN_LKM

    def päivitä_käyttöliittymän_tekstit(self):
        # Päivitetään kaikkien pelaajien pistemäärät näytölle
        for i in range(len(self.__pistelabelit)):
            self.__pistelabelit[i].configure(text=self.__pelaajien_pisteet[i])

        # Päivitetään pelitilanneteksti näytölle
        self.__infoLabel.configure(text=self.__pelitilanneteksti)

    def lopeta_vuoro(self):
        if self.__pelivuoro == 0:
            self.__pelivuoro = 1
        else:
            self.__pelivuoro = 0

        self.__pelitilanneteksti = "Vuorossa pelaaja " + str(
            self.__pelivuoro + 1)

        self.päivitä_käyttöliittymän_tekstit()

    def muuta_nopan_tila(self, nopan_indeksi):
        if self.__nopat_käytössä[nopan_indeksi]:
            self.__nopat_käytössä[nopan_indeksi] = False
            self.__lukitusbuttonit[nopan_indeksi].configure(text="lukittu",
                                                            background="red")
        else:
            self.__nopat_käytössä[nopan_indeksi] = True
            self.__lukitusbuttonit[nopan_indeksi].configure(text="vapaa",
                                                            background="green")

    def heitä(self):
        random.seed()

        for noppa_label in range(0, NOPPIEN_LKM):
            if not self.__nopat_käytössä[noppa_label]:
                continue
            luku = random.randint(1, 6)
            self.__silmäluvut[noppa_label] = luku
            self.__noppakuvalabelit[noppa_label]\
                .configure(image=self.__noppakuvat[luku - 1])

        pisteet = 0
        for k in self.__silmäluvut:
            pisteet += k

        self.__pelaajien_pisteet[self.__pelivuoro] += pisteet
        self.päivitä_käyttöliittymän_tekstit()

    def kaynnista(self):
        self.__ikkuna.mainloop()


def main():
    käli = Noppapeli()
    käli.kaynnista()


main()
