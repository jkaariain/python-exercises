jatka = True


def siirto(x, y, z):
    try:
        siirto_x = float(input("x-koordinaatin siirto: "))
        siirto_y = float(input("y-koordinaatin siirto: "))
        siirto_z = float(input("z-koordinaatin siirto: "))

        for i in range(0, len(x)):
            x[i] += siirto_x
            y[i] += siirto_y
            z[i] += siirto_z
    except ValueError:
        global jatka
        jatka = False
        print("Virheellinen syöte.")


def venytys(x, y, z):
    try:
        venytys_x = float(input("x-koordinaatin venytys: "))
        venytys_y = float(input("y-koordinaatin venytys: "))
        venytys_z = float(input("z-koordinaatin venytys: "))

        for i in range(0, len(x)):
            x[i] *= venytys_x
            y[i] *= venytys_y
            z[i] *= venytys_z
    except ValueError:
        global jatka
        jatka = False
        print("Virheellinen syöte.")


def main():
    nimi = input("Anna luettavan tiedoston nimi: ")
    x = []
    y = []
    z = []

    try:
        tiedosto = open(nimi, "r", encoding="utf-8")

        for rivi in tiedosto:
            osat = rivi.rstrip().split(";")
            x.append(float(osat[0]))
            y.append(float(osat[1]))
            z.append(float(osat[2]))

        tiedosto.close()
    except ValueError:
        print("Virhe tiedoston lukemisessa.")
    except OSError:
        print("Virhe tiedoston lukemisessa.")

    valinta = input("Haluatko siirtää vai venyttää kuviota (S/V): ")

    if valinta == 'S':
        siirto(x, y, z)
    elif valinta == 'V':
        venytys(x, y, z)
    else:
        print("Virheellinen syöte.")
        return

    if jatka:
        nimi = input("Anna kirjoitettavan tiedoston nimi: ")

        try:
            tiedosto = open(nimi, "w", encoding="utf-8")
            for i in range(0, len(x)):
                tiedosto.write(str(x[i]) + ';' + str(y[i]) + ';' + str(z[i])
                               + '\n')
            tiedosto.close()

            print("Kuvion tallennus onnistui!")
        except OSError:
            pass

main()
