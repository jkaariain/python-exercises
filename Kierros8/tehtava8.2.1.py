def main():
    korkeus = -1
    leveys = -1
    leveys_ok = False
    korkeus_ok = False
    process_ok = False

    while not process_ok:
        try:
            if not leveys_ok:
                leveys = int(input("Syötä ruudun leveys: "))
                if leveys > 0:
                    leveys_ok = True

            if not korkeus_ok and leveys_ok:
                korkeus = int(input("Syötä ruudun korkeus: "))
                if korkeus > 0:
                    korkeus_ok = True

            if leveys_ok and korkeus_ok:
                process_ok = True
        except ValueError:
            continue

    merkki = input("Syötä tulostusmerkki: ")
    print()

    for i in range(0, korkeus):
        print(merkki * leveys)

main()
