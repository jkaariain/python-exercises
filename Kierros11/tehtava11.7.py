class Matriisi:
    def __init__(self, matriisi):
        self.__matriisi = matriisi

    def lue_matriisi(self):
        return self.__matriisi

    def tulosta(self):
        print(self.__matriisi)

    def kirjoita_arvo(self, leveys, korkeus, arvo):
        self.__matriisi[leveys][korkeus] = arvo

    def lue_arvo(self, leveys, korkeus):
        return self.__matriisi[leveys][korkeus]

    def skalaarikertolasku(self, skalaari):
        ret = Matriisi(self.__matriisi)

        for i in range(0, len(ret.lue_matriisi())):
            for j in range(0, len(ret.lue_matriisi()[0])):
                ret.kirjoita_arvo(i, j, ret.lue_arvo(i, j) * skalaari)

        return ret

    def matriisikertolasku(self, toinen_matriisi):
        if len(self.__matriisi[0]) != len(toinen_matriisi.lue_matriisi()):
            print("Matriisien dimensiot eivät täsmää")
            return False

        rows_A = len(self.__matriisi)
        cols_A = len(self.__matriisi[0])
        rows_B = len(toinen_matriisi.lue_matriisi())
        cols_B = len(toinen_matriisi.lue_matriisi()[0])

        ret = [[0 for row in range(0, cols_B)]
               for col in range(0, rows_A)]

        for i in range(0, rows_A):
            for j in range(0, cols_B):
                for k in range(0, cols_A):
                    ret[i][j] += \
                        self.__matriisi[i][k] * \
                        toinen_matriisi.lue_matriisi()[k][j]

        return ret

    def __str__(self):
        return str(self.__matriisi)


def lue_tiedosto():
    tiedostonimi = input("Syötä matriisitiedoston nimi: ")
    matriisi = []

    try:
        tiedosto = open(tiedostonimi, "r", encoding="utf-8")

        for rivi in tiedosto:
            rivi = rivi.rstrip()
            matriisi_rivi = rivi.split(" ")
            matriisi_rivi = [int(x) for x in matriisi_rivi]
            matriisi.append(matriisi_rivi)

        tiedosto.close()

        avain = input("Syötä matriisin nimi: ")
        return avain, Matriisi(matriisi)
    except OSError:
        print("Virhe! Tiedostoa " + tiedostonimi + " ei voida lukea.")


def tulosta(sanakirja):
    avain = input("Syötä nimi: ")

    if avain in sanakirja:
        print(avain, "=", sanakirja[avain])
    else:
        print("Nimeä {:s} ei ole olemassa".format(avain))


def listaa(sanakirja):
    for x in sorted(sanakirja):
        print(x, "=", sanakirja[x])


def skalaarikertolasku(sanakirja):
    avain = input("Syötä matriisin nimi: ")

    if avain in sanakirja:
        luku = int(input("Syötä luku: "))

        print(str(luku) + " * " + str(sanakirja[avain]))
        tulo = sanakirja[avain].skalaarikertolasku(luku)
        print("= " + str(tulo))


def matriisikertolasku(sanakirja):
    a1 = input("Syötä 1. operandin nimi: ")
    if a1 not in sanakirja:
        print("Nimeä {:s} ei ole olemassa".format(a1))
    a2 = input("Syötä 2. operandin nimi: ")
    if a2 not in sanakirja:
        print("Nimeä {:s} ei ole olemassa".format(a2))

    tulos = sanakirja[a1].matriisikertolasku(sanakirja[a2])

    if not tulos:
        return
    else:
        print(str(sanakirja[a1]))
        print("* " + str(sanakirja[a2]))
        print("= " + str(tulos))


def main():
    matriisit = {}

    while 1:
        komento = input("> ")

        if komento == "lisää":
            avain, matriisi = lue_tiedosto()
            matriisit[avain] = matriisi
        elif komento == "tulosta":
            tulosta(matriisit)
        elif komento == "listaa":
            listaa(matriisit)
        elif komento == "skalaarikertolasku":
            skalaarikertolasku(matriisit)
        elif komento == "matriisikertolasku":
            matriisikertolasku(matriisit)
        elif komento == "lopeta":
            break
        else:
            print("Tuntematon komento!")

    print("Hei hei!")

main()
