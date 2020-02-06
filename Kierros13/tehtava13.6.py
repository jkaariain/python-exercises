# TIE-02100 Johdatus ohjelmointiin S2016
# Painoindeksilaskurin pohjakoodi

from tkinter import *

NaN = float("NaN")


class Käyttöliittymä:

    def __init__(self):
        self.__pääikkuna = Tk()
        self.__pääikkuna.title("Painoindeksilaskuri")

        # TODO: Lisää haluamiasi elementtejä, kuten tekstikentät 
        # syötelaatikoiden yläpuolelle kertomaan, mitä laatikkoon tulee antaa.
        self.__pituus_teksti = Label(self.__pääikkuna, text="Pituus (cm):")
        self.__paino_teksti = Label(self.__pääikkuna, text="Paino (kg):")
        self.__BMI_teksti = Label(self.__pääikkuna, text="BMI:")

        # TODO: Syötelaatikko pituuden antamiseen
        self.__pituus_arvo = Entry()
        # TODO: Syötelaatikko painon antamiseen
        self.__paino_arvo = Entry()

        # TODO: Nappi, joka kutsuu laske_BMI-metodia
        # TODO: Värjää nappi muun väriseksi, kuin se oletuksena on
        self.__laskunappi = Button(self.__pääikkuna, text="Laske",
                                   background="#A0FF86",
                                   foreground="#F186FF",
                                   borderwidth=2,
                                   command=self.laske_BMI)
        # TODO: Label, johon laskettu bmi asetetaan
        self.__tulos_teksti = Label(self.__pääikkuna, text="")
        # TODO: Label, johon sanallinen selitys asetetaan
        self.__selite_teksti = Label(self.__pääikkuna,
                                     text="",
                                     justify=CENTER)
        # Todo: Nappi, joka kutsuu lopeta-metodia
        self.__lopetusnappi = Button(self.__pääikkuna, text="Lopeta",
                                     command=self.lopeta)

        # TODO: Sijoittele elementit ikkunassa haluamallasi tavalla
        self.__pituus_teksti.grid(row=1, column=0, stick=E)
        self.__pituus_arvo.grid(row=1, column=1, columnspan=2, stick=E+W)
        self.__paino_teksti.grid(row=2, column=0, stick=E)
        self.__paino_arvo.grid(row=2, column=1, columnspan=2, stick=E+W)
        self.__laskunappi.grid(row=3, column=1, stick=W)
        self.__lopetusnappi.grid(row=4, column=4)
        self.__BMI_teksti.grid(row=2, column=3, stick=E)
        self.__tulos_teksti.grid(row=2, column=4, stick=W)
        self.__selite_teksti.grid(row=0, column=0, columnspan=5, pady=10,
                                  padx=10)

    # TODO: Toteuta metodi
    def laske_BMI(self):
        """ Laskee käyttäjän painoindeksin ja näyttää sen käyttäjälle.
            Ottaa pituuden ja painon elementeistä self.__pituus_arvo ja
            self.__paino_arvo. Asettaa lasketun bmi:n elementtiin
            self.__tulos_teksti ja sanallisen palautteen elementtiin
            self.__selite_teksti.
        """
        try:
            pituus = float(self.__pituus_arvo.get()) * 0.01
            paino = float(self.__paino_arvo.get())

            if pituus <= 0 or paino <= 0:
                self.__selite_teksti.configure(text="Virhe: pituus ja paino "
                                                    "oltava positiivisia.",
                                               foreground="#FF0000")
                self.nollaa_kentät()
                return

            tulos = paino / (pituus ** 2)
            teksti = "{:.2f}".format(tulos)
            self.__tulos_teksti.configure(text=teksti)

            if 18.5 <= tulos <= 25:
                self.__selite_teksti.configure(text="Olet normaalipainoinen.",
                                               foreground="#000000")
            elif tulos > 25:
                self.__selite_teksti.configure(text="Olet ylipainoinen.",
                                               foreground="#000000")
            else:
                self.__selite_teksti.configure(text="Olet alipainoinen.",
                                               foreground="#000000")
        except ValueError:
            self.__selite_teksti.configure(text="Virhe: pituus ja "
                                           "paino oltava lukuja.",
                                           foreground="#FF0000")
            self.nollaa_kentät()
            return

    # TODO: Toteuta metodi
    def nollaa_kentät(self):
        """Nollaa virheen sattuessa elementit self.__tulos_teksti,
        self.__pituus_arvo jaself.__paino_arvo"""
        self.__tulos_teksti.configure(text="")
        self.__pituus_arvo.delete(0, END)
        self.__paino_arvo.delete(0, END)

    def lopeta(self):
        """ Lopettaa ohjelman. """
        self.__pääikkuna.destroy()

    def kaynnista(self):
        """ Käynnistää ohjelman. """
        self.__pääikkuna.mainloop()


def main():
    käli = Käyttöliittymä()
    käli.kaynnista()


main()
