from tkinter import *
import random
import time


NOPPAKUVAT = [ "1.gif", "2.gif", "3.gif", "4.gif", "5.gif", "6.gif" ]

PELAAJA_1 = 1
PELAAJA_2 = 2


class Noppapeli:
    def __init__(self):
        self.__ikkuna = Tk()
        self.__ikkuna.title("Noppapeli")

        self.__pelivuoro = None
        self.__heittokertoja = None

        self.__noppakuvat = []
        for kuvatiedosto in NOPPAKUVAT:
            kuva = PhotoImage(file=kuvatiedosto)
            self.__noppakuvat.append(kuva)

        Label(self.__ikkuna, text="Pelaajan 1 pistetilanne:")\
            .grid(row=0, column=0, columnspan=2, sticky=E)
        Label(self.__ikkuna, text="Pelaajan 2 pistetilanne:")\
            .grid(row=1, column=0, columnspan=2, sticky=E)

        self.__pel1pisteetLabel = Label(self.__ikkuna)
        self.__pel1pisteetLabel.grid(row=0, column=2, sticky=W)
        self.__pel2pisteetLabel = Label(self.__ikkuna)
        self.__pel2pisteetLabel.grid(row=1, column=2, sticky=W)

        self.__heitäButton = Button(self.__ikkuna, text="heitä",
                                    command=self.heitä)
        self.__heitäButton.grid(row=0, column=3, sticky=W+E)
        self.__lopetavuoroButton = Button(self.__ikkuna, text="lopeta vuoro")
        self.__lopetavuoroButton.grid(row=1, column=3, sticky=W+E)

        Button(self.__ikkuna, text="uusi peli", command=self.alusta_peli)\
            .grid(row=2, column=3, sticky=W+E+N)
        Button(self.__ikkuna, text="lopeta", command=self.__ikkuna.destroy)\
            .grid(row=4, column=3, sticky=W+E+S)

        self.__noppa1Label = Label(self.__ikkuna)
        self.__noppa1Label.grid(row=2, column=0)
        self.__noppa2Label = Label(self.__ikkuna)
        self.__noppa2Label.grid(row=2, column=1)
        self.__noppa3Label = Label(self.__ikkuna)
        self.__noppa3Label.grid(row=2, column=2)

        self.__lukitus1Button = Button(self.__ikkuna)
        self.__lukitus1Button.grid(row=3, column=0)
        self.__lukitus2Button = Button(self.__ikkuna)
        self.__lukitus2Button.grid(row=3, column=1)
        self.__lukitus3Button = Button(self.__ikkuna)
        self.__lukitus3Button.grid(row=3, column=2)

        self.__infoLabel = Label(self.__ikkuna)
        self.__infoLabel.grid(row=4, column=0, columnspan=3)

        self.alusta_peli()

    def alusta_peli(self):
        self.__pelivuoro = PELAAJA_1
        self.__heittokertoja = 2

        self.__noppa1Label.configure(image=self.__noppakuvat[0])
        self.__noppa2Label.configure(image=self.__noppakuvat[0])
        self.__noppa3Label.configure(image=self.__noppakuvat[0])

        self.raportoi_vuorotilanne()

        self.salli_heitä_ja_lopeta_vuoro_napit()

        self.vapauta_ja_estä_lukitusnapit()


    def estä_heitä_ja_lopeta_vuoro_napit(self):
        self.__heitäButton.configure(state=DISABLED)
        self.__lopetavuoroButton.configure(state=DISABLED)


    def salli_heitä_ja_lopeta_vuoro_napit(self):
        self.__heitäButton.configure(state=NORMAL)
        self.__lopetavuoroButton.configure(state=NORMAL)


    def raportoi_vuorotilanne(self):
        self.__infoLabel.configure(text=
              "Pelaajan {:d} vuoro, heittokertoja jäljellä {:d}" \
              .format(self.__pelivuoro, self.__heittokertoja))


    def vapauta_ja_estä_lukitusnapit(self):
        self.__lukitus1Button.configure(text="vapaa")
        self.__lukitus2Button.configure(text="vapaa")
        self.__lukitus3Button.configure(text="vapaa")

        self.__lukitus1Button.configure(background="green")
        self.__lukitus2Button.configure(background="green")
        self.__lukitus3Button.configure(background="green")

        self.__lukitus1Button.configure(state=DISABLED)
        self.__lukitus2Button.configure(state=DISABLED)
        self.__lukitus3Button.configure(state=DISABLED)

    def heitä(self):
        """ Heittää kaikkia noppia."""
        random.seed()
        noppa1 = random.randint(1, 6)
        noppa2 = random.randint(1, 6)
        noppa3 = random.randint(1, 6)

        self.__noppa1Label.configure(image=self.__noppakuvat[noppa1-1])
        self.__noppa2Label.configure(image=self.__noppakuvat[noppa2-1])
        self.__noppa3Label.configure(image=self.__noppakuvat[noppa3-1])

    def kaynnista(self):
        self.__ikkuna.mainloop()

def main():
    käli = Noppapeli()
    käli.kaynnista()


main()
