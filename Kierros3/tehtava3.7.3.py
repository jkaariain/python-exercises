def tulosta_ruutu(l, k, m):
    for i in range(0, k):
        for j in range(0, l):
            print(m, end="")
        print()


def main():
    leveys = int(input("Syötä ruudun leveys: "))
    korkeus = int(input("Syötä ruudun korkeus: "))
    tulostusmerkki = input("Syötä tulostusmerkki: ")
    print()
    tulosta_ruutu(leveys, korkeus, tulostusmerkki)

main()
