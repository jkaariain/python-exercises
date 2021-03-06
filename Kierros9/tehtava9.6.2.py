jatka = True


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

    half_x = (max(x) - min(x)) / 2
    half_y = (max(y) - min(y)) / 2
    half_z = (max(z) - min(z)) / 2

    half_x_loc = max(x) - half_x
    half_y_loc = max(y) - half_y
    half_z_loc = max(z) - half_z

    for i in range(0, len(x)):
        x[i] -= half_x_loc
        y[i] -= half_y_loc
        z[i] -= half_z_loc

    if jatka:
        nimi = input("Anna kirjoitettavan tiedoston nimi: ")

        try:
            tiedosto = open(nimi, "w", encoding="utf-8")
            for i in range(0, len(x)):
                tiedosto.write("{:.4f};{:.4f};{:.4f}\n".format(x[i],
                                                               y[i], z[i]))
            tiedosto.close()

            print("Kappale siirretty origoon.")
        except OSError:
            print("Virhe tiedoston kirjoittamisessa.")
            pass

main()
