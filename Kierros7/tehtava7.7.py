def lue_pisteet():
    rivit = []
    print("Syötä kilpailijan nimi ja pistemäärä. Lopeta syöttämällä "
          "tyhjä rivi.")
    while 1:  # Ääretön silmukka
        rivi = input()
        if rivi == "":
            return rivit
        else:
            rivit.append(rivi)


def main():
    syöte = lue_pisteet()
    piste_sanakirja = {}
    summa = 0

    for rivi in syöte:
        nimi, piste = rivi.split(" ")

        if nimi in piste_sanakirja:
            piste_sanakirja[nimi].append(piste)
        else:
            piste_sanakirja[nimi] = [piste]

    print("Kilpailijoiden pistetilanne:")
    for nimi in sorted(piste_sanakirja):
        print(nimi, end=" ")
        for i in piste_sanakirja[nimi]:
            print(i, end=" ")
            summa += int(i)
        print("=", str(summa))
        summa = 0


main()
