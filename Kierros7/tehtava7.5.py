def lue_viesti():
    rivit = []
    print("Syötä viestin tekstirivejä. Lopeta syöttämällä tyhjä rivi.")
    while 1:  # Ääretön silmukka
        rivi = input()
        if rivi == "":
            return rivit
        else:
            rivit.append(rivi)


def main():
    sanatiheys = {}
    teksti = lue_viesti()

    for rivi in teksti:
        sanat = rivi.split(" ")

        for sana in sanat:
            if str.lower(sana) in sanatiheys:
                sanatiheys[str.lower(sana)] += 1
            else:
                sanatiheys[str.lower(sana)] = 1

    for sana in sorted(sanatiheys):
        print(sana, ":", sanatiheys[sana], "kpl")

main()