def main():
    nimi = input("Syötä tiedoston nimi: ")
    rivi_nro = 1
    num_of_rows = 0
    whitespace = ""

    try:
        tiedosto = open(nimi, "r", encoding="utf-8")

        for rivi in tiedosto:
            num_of_rows += 1
            whitespace = (len(str(num_of_rows)) - 1) * " "

        tiedosto.seek(0)

        for rivi in tiedosto:
            rivi = rivi.rstrip()
            print("{:s}{:s} {:s}".format(whitespace,
                                         str(rivi_nro), rivi))
            rivi_nro += 1

        tiedosto.close()
    except OSError:
        print("Virhe tiedoston lukemisessa.")


main()
