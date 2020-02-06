from tkinter import *


class Käyttöliittymä:
    def __init__(self):
        self.__pääikkuna = Tk()

        self.__tekstikenttä = Label(self.__pääikkuna, text="Hello World!",
                                    background="#00ff00", foreground="#ff0000",
                                    padx=30, pady=10,
                                    relief=RIDGE, borderwidth=10)
        self.__tekstikenttä.pack(expand=True, fill=BOTH)

        self.__pääikkuna.mainloop()


def main():
    käli = Käyttöliittymä()

main()
