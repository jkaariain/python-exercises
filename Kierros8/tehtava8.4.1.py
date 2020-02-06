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
    nimi = input("Syötä tiedoston nimi: ")
    rivi_nro = 1

    try:
        tiedosto = open(nimi, "w", encoding="utf-8")
        syöte = lue_viesti()
        whitespace = (len(str(len(syöte)))) * " "

        for rivi in syöte:
            tiedosto.write(str(rivi_nro) + whitespace + rivi + "\n")
            rivi_nro += 1

        tiedosto.close()

        print("Tiedosto " + nimi + " kirjoitettu.")
    except OSError:
        print("Tiedoston " + nimi + " kirjoittaminen epäonnistui.")

main()
