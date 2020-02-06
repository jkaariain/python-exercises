def luo_koordinaatisto(w, h):
    taulukko = []
    for i in range(0, h):
        taulukko.append("." * w)

    return taulukko


def tulosta_koordinaatisto(w, h, koordinaatisto):
    print("  ", end="")
    for i in range(0, w):
        print((i+1) % 10, end="")
    print()
    print(" ", "+", "-"*w, sep="")
    for i in range(0, h):
        print((i+1) % 10, "|", koordinaatisto[i], sep="")
    pass


def lisaa_piste(leveys, korkeus, koordinaatisto):
    x = int(input("Anna vaaka-koordinaatti: "))
    x -= 1

    if x < 0 or x > leveys-1:
        print("Piste on koordinaatiston ulkopuolella.")
        return

    y = int(input("Anna pysty-koordinaatti: "))
    y -= 1

    if y < 0 or y > korkeus-1:
        print("Piste on koordinaatiston ulkopuolella.")
        return

    rivi = list(koordinaatisto[y])
    rivi[x] = "X"
    koordinaatisto[y] = ''.join(rivi)
    tulosta_koordinaatisto(leveys, korkeus, koordinaatisto)

    pass


def main():
    leveys = int(input("Anna koordinaatiston leveys: "))
    while leveys < 1 or leveys > 20:
        print("Virheellinen syöte!")
        leveys = int(input("Anna koordinaatiston leveys: "))

    korkeus = int(input("Anna koordinaatiston korkeus: "))
    while korkeus < 1 or korkeus > 10:
        print("Virheellinen syöte!")
        korkeus = int(input("Anna koordinaatiston korkeus: "))

    koordinaatisto = luo_koordinaatisto(leveys, korkeus)
    tulosta_koordinaatisto(leveys, korkeus, koordinaatisto)

    lisataanko_piste = input("Lisätäänkö koordinaatistoon piste (K/E)? ")

    while lisataanko_piste.lower() != "k" and lisataanko_piste.lower() != "e":
        print("Virheellinen syöte!")
        lisataanko_piste = input("Lisätäänkö koordinaatistoon piste (K/E)? ")

    while lisataanko_piste.lower() == "k":
        lisaa_piste(leveys, korkeus, koordinaatisto)
        lisataanko_piste = input("Lisätäänkö koordinaatistoon piste (K/E)? ")
        while lisataanko_piste.lower() != "k" \
                and lisataanko_piste.lower() != "e":
            print("Virheellinen syöte!")
            lisataanko_piste = \
                input("Lisätäänkö koordinaatistoon piste (K/E)? ")

    pass

main()
