# TIE-02100 Johdatus ohjelmointiin
# Tehtävä: ristinolla, ohjelmakoodipohja


def tarkista_lauta(pelilauta):
    if pelilauta[0][0] == "X":
        if pelilauta[0][1] == pelilauta[0][2] == "X":
            return "X"
        elif pelilauta[1][1] == pelilauta[2][2] == "X":
            return "X"
        elif pelilauta[1][0] == pelilauta[2][0] == "X":
            return "X"
        else:
            return ""
    elif pelilauta[1][1] == "X":
        if pelilauta[0][1] == pelilauta[2][1] == "X":
            return "X"
        elif pelilauta[1][0] == pelilauta[1][2] == "X":
            return "X"
        elif pelilauta[0][0] == pelilauta[2][2] == "X":
            return "X"
        elif pelilauta[2][0] == pelilauta[0][2] == "X":
            return "X"
        else:
            return ""
    elif pelilauta[2][2] == "X":
        if pelilauta[0][2] == pelilauta[1][2] == "X":
            return "X"
        elif pelilauta[2][0] == pelilauta[2][1] == "X":
            return "X"
        else:
            return ""
    elif pelilauta[0][0] == "O":
        if pelilauta[0][1] == pelilauta[0][2] == "O":
            return "O"
        elif pelilauta[1][1] == pelilauta[2][2] == "O":
            return "O"
        elif pelilauta[1][0] == pelilauta[2][0] == "O":
            return "O"
        else:
            return ""
    elif pelilauta[1][1] == "O":
        if pelilauta[0][1] == pelilauta[2][1] == "O":
            return "O"
        elif pelilauta[1][0] == pelilauta[1][2] == "O":
            return "O"
        elif pelilauta[0][0] == pelilauta[2][2] == "O":
            return "O"
        elif pelilauta[2][0] == pelilauta[0][2] == "O":
            return "O"
        else:
            return ""
    elif pelilauta[2][2] == "O":
        if pelilauta[0][2] == pelilauta[1][2] == "O":
            return "O"
        elif pelilauta[2][0] == pelilauta[2][1] == "O":
            return "O"
        else:
            return ""
    else:
        return ""


def main():
    pelilauta = []
    for i in range(0, 3):
        rivi = []
        for j in range(0, 3):
            rivi.append('.')
        pelilauta.append(rivi)

    vuorot = 0  # Pelattujen vuorojen määrä
    shit_happened = False
    merkki = ""
    voittaja = ""
    peli_jatkuu = True

    # Peli jatkuu kunnes ruudukko on täynnä.
    # 8 vuoron vaihdon jälkeen laudalle on laitettu 9 merkkiä.
    while vuorot < 9 and peli_jatkuu:
        if not shit_happened:
            for i in range(0, 3):
                for j in range(0, 3):
                    print(pelilauta[i][j], end="")
                print()

        # Päivitetään merkki vuoron mukaan
        if vuorot % 2 == 0:
            merkki = "X"
        else:
            merkki = "O"
        koordinaatit = input("Pelaaja " + merkki + " anna koordinaatit: ")

        try:
            y, x = koordinaatit.split(" ")
            x = int(x)
            y = int(y)

            while pelilauta[x][y] != '.':
                print("Virhe: ruutuun on jo pelattu.")
                koordinaatit = input(
                    "Pelaaja " + merkki + " anna koordinaatit: ")
                y, x = koordinaatit.split(" ")
                x = int(x)
                y = int(y)

            pelilauta[x][y] = merkki

            voittaja = tarkista_lauta(pelilauta)
            if voittaja != "":
                peli_jatkuu = False

            vuorot += 1

            shit_happened = False

        except ValueError:
            shit_happened = True
            print("Virhe: syötä kaksi kokonaislukua välilyönnillä erotettuna.")

        except IndexError:
            shit_happened = True
            print("Virhe: koordinaattien oltava välillä 0-2.")

    for i in range(0, 3):
        for j in range(0, 3):
            print(pelilauta[i][j], end="")
        print()

    if voittaja == "":
        print("Tasapeli!")
    else:
        print("Peli loppui, voittaja on " + merkki)

main()
