from tkinter import *

NaN = float('NaN')


class Käyttöliittymä:
    def __init__(self):
        self.__float_tulos = NaN

        self.__pääikkuna = Tk()

        # GUI komponentit
        self.__entryA = Entry(self.__pääikkuna)
        self.__entryB = Entry(self.__pääikkuna)

        self.__labelA = Label(self.__pääikkuna, text="A:")
        self.__labelB = Label(self.__pääikkuna, text="B:")

        self.__tulosotsikko = Label(self.__pääikkuna, text="Tulos:")
        self.__tulosarvo = Label(self.__pääikkuna, text=NaN)

        self.__summanappi = Button(self.__pääikkuna, text="A + B",
                                   command=self.summa)
        self.__erotusnappi = Button(self.__pääikkuna, text="A - B",
                                    command=self.miinus)
        self.__kertonappi = Button(self.__pääikkuna, text="A * B",
                                   command=self.kerto)
        self.__jakonappi = Button(self.__pääikkuna, text="A / B",
                                  command=self.jako)
        self.__siirtonappi = Button(self.__pääikkuna, text="tulos→A",
                                    command=self.siirto)
        self.__vaihtonappi = Button(self.__pääikkuna, text="A↔B",
                                    command=self.vaihto)
        self.__lopetusnappi = Button(self.__pääikkuna, text="lopeta",
                                     command=self.lopeta)

        # Sijoittele komponentit
        self.__labelA.grid(row=0, column=0, sticky=E)
        self.__entryA.grid(row=0, column=1, columnspan=2)
        self.__labelB.grid(row=0, column=3, sticky=E)
        self.__entryB.grid(row=0, column=4)

        self.__tulosotsikko.grid(row=1, column=3, sticky=E)
        self.__tulosarvo.grid(row=1, column=4)

        self.__summanappi.grid(row=2, column=0, sticky=E+W)
        self.__erotusnappi.grid(row=2, column=1, sticky=E+W)
        self.__kertonappi.grid(row=3, column=0, sticky=E+W)
        self.__jakonappi.grid(row=3, column=1, sticky=E+W)
        self.__siirtonappi.grid(row=2, column=2, sticky=E+W)
        self.__vaihtonappi.grid(row=3, column=2, sticky=E+W)

        self.__lopetusnappi.grid(row=4, column=4, sticky=E)

        self.__pääikkuna.mainloop()

    def summa(self):
        (a, b) = self.hae_lähtöarvot()
        self.__float_tulos = a + b
        self.aseta_tulosarvo()

    def miinus(self):
        (a, b) = self.hae_lähtöarvot()
        self.__float_tulos = a - b
        self.aseta_tulosarvo()

    def kerto(self):
        (a, b) = self.hae_lähtöarvot()
        self.__float_tulos = a * b
        self.aseta_tulosarvo()

    def jako(self):
        (a, b) = self.hae_lähtöarvot()
        self.__float_tulos = a / b
        self.aseta_tulosarvo()

    def vaihto(self):
        (a, b) = self.hae_lähtöarvot()
        self.__entryA.delete(0, END)
        self.__entryA.insert(0, b)
        self.__entryB.delete(0, END)
        self.__entryB.insert(0, a)

    def siirto(self):
        self.__entryA.delete(0, END)
        self.__entryA.insert(0, self.__float_tulos)

    def lopeta(self):
        self.__pääikkuna.destroy()

    def hae_lähtöarvot(self):
        try:
            a_arvo = float(self.__entryA.get())
        except ValueError:
            a_arvo = NaN

        try:
            b_arvo = float(self.__entryB.get())
        except ValueError:
            b_arvo = NaN

        return a_arvo, b_arvo

    def aseta_tulosarvo(self):
        self.__tulosarvo.configure(text=self.__float_tulos)


def main():
    käli = Käyttöliittymä()


main()
