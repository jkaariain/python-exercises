# TIE-02100 Johdatus ohjelmointiin
# Tehtävä: ristinolla, ohjelmakoodipohja


def main():
    pelilauta = []
    for i in range(0, 3):
        rivi = []
        for j in range(0, 3):
            rivi.append('.')
        pelilauta.append(rivi)

    vuorot = 0  # Pelattujen vuorojen määrä
    shit_happened = False

    # Peli jatkuu kunnes ruudukko on täynnä.
    # 8 vuoron vaihdon jälkeen laudalle on laitettu 9 merkkiä.
    while vuorot < 9:
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


main()
