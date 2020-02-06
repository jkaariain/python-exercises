import math

def main():
    nimi = input("Syötä luettavan tiedoston nimi: ")
    header = ""
    is_header = True
    sekuntilista = []
    sekuntimuutos = []
    lt1 = []
    lt1muutos = []
    lt2 = []
    lt2muutos = []
    lt3 = []
    lt3muutos = []
    jatka = True
    idx = 0

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
                lt1.append(tiedot[1])
                lt2.append(tiedot[2])
                lt3.append(tiedot[3])
                tunnit, minuutit, sekunnit = aika.split(":")

                kok_sekunnit = 3600 * \
                               int(tunnit) + 60 * int(minuutit) + int(sekunnit)

                sekuntilista.append(int(kok_sekunnit))

                if idx == 0:
                    idx += 1
                    continue
                else:
                    sekuntimuutos.append(float
                                         (sekuntilista[idx] - sekuntilista[
                                             idx - 1]))

                    lt_a1 = float(str(lt1[idx]).replace(',', '.'))
                    lt_b1 = float(str(lt1[idx - 1]).replace(',', '.'))
                    lt1muutos.append(round((lt_a1 - lt_b1) /
                                           sekuntimuutos[idx-1], 1))

                    lt_a1 = float(str(lt2[idx]).replace(',', '.'))
                    lt_b1 = float(str(lt2[idx - 1]).replace(',', '.'))
                    lt2muutos.append(round((lt_a1 - lt_b1) /
                                           sekuntimuutos[idx-1], 1))

                    lt_a1 = float(str(lt3[idx]).replace(',', '.'))
                    lt_b1 = float(str(lt3[idx - 1]).replace(',', '.'))
                    lt3muutos.append(round((lt_a1 - lt_b1) /
                                           sekuntimuutos[idx-1], 1))
                    idx += 1

        tiedosto.close()
    except OSError:
        jatka = False
        print("Virhe tiedoston lukemisessa!")

    if jatka:
        kirjoitettavan_nimi = input("Syötä kirjoitettavan tiedoston nimi: ")

        try:
            tiedosto = open(kirjoitettavan_nimi, "w", encoding="utf-8")

            for x in range(0, len(sekuntimuutos)):
                tiedosto.write(str(sekuntimuutos[x]) + ";" + str(lt1muutos[x])
                               + ";" + str(lt2muutos[x]) + ";"
                               + str(lt3muutos[x]) + '\n')

            tiedosto.close()
        except OSError:
            pass

        print("Tietojen tallennus onnistui.")


main()
