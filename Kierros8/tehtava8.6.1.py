def main():
    nimi = input("Syötä luettavan tiedoston nimi: ")
    header = ""
    is_header = True
    sekuntilista = []
    lt1 = []
    lt2 = []
    lt3 = []
    jatka = True

    try:
        tiedosto = open(nimi, "r", encoding="utf-8")

        for rivi in tiedosto:
            tiedot = rivi.split(";")

            if is_header:
                try:
                    header += tiedot[0] + ";"
                    header += tiedot[1] + ";"
                    header += tiedot[2] + ";"
                    header += tiedot[3]
                except ValueError:
                    jatka = False
                    print("Virhe tiedoston lukemisessa!")
                is_header = False
                continue

            if jatka:
                aika = tiedot[0]
                lt1.append(tiedot[1] + ";")
                lt2.append(tiedot[2] + ";")
                lt3.append(tiedot[3])
                tunnit, minuutit, sekunnit = aika.split(":")

                kok_sekunnit = 3600 * int(tunnit) + 60 * int(minuutit) + \
                                int(sekunnit)
                sekuntilista.append(int(kok_sekunnit))

        tiedosto.close()
    except OSError:
        print("Virhe tiedoston lukemisessa!")

    kirjoitettavan_nimi = input("Syötä kirjoitettavan tiedoston nimi: ")

    try:
        tiedosto = open(kirjoitettavan_nimi, "w", encoding="utf-8")

        tiedosto.write(header)
        for x in range(0, len(sekuntilista)):
            tiedosto.write(str(sekuntilista[x]) + ";" + str(lt1[x])
                           + str(lt2[x]) + str(lt3[x]))

        tiedosto.close()
    except OSError:
        pass

    print("Tietojen tallennus onnistui.")

main()
