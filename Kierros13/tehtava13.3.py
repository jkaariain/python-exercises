from tkinter import *


class Käyttöliittymä:
    def __init__(self):
        self.__pääikkuna = Tk()

        self.__tekstikenttä = Label(self.__pääikkuna, text="Hello World!")
        self.__tekstikenttä.pack()

        self.__lopetusnappi = Button(self.__pääikkuna, text="lopeta mut",
                                     command=self.lopeta)

        self.__lopetusnappi.pack()

        self.__pääikkuna.mainloop()

    def lopeta(self):
        self.__pääikkuna.destroy()


def main():
    käli = Käyttöliittymä()

main()
