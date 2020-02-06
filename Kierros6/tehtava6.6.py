# TIE-02100 Johdatus ohjelmointiin
# Tehtävä: ROT-13, ohjelmakoodipohja


def salaa(merkki):
    SELKOMERKIT = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
                        "x", "y", "z"]

    SALAMERKIT = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
                            "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                            "j", "k", "l", "m"]

    # Täydennä merkin salaaminen tähän
    if merkki.isupper():
        return str(SALAMERKIT[SELKOMERKIT.index(str.lower(merkki))]).upper()
    elif not merkki.isalpha():
        return merkki
    elif str.lower(merkki) == "å" or str.lower(merkki) == "ä" or \
            str.lower(merkki) == "ö":
        return merkki
    else:
        return SALAMERKIT[SELKOMERKIT.index(merkki)]


def rivin_salaus(rivi):
    salattu_rivi = ""

    for i in rivi:
        salattu_rivi += salaa(i)

    return salattu_rivi


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
    viesti = lue_viesti()

    if viesti:
        print("ROT13:")
        for rivi in viesti:
            print(rivin_salaus(rivi))

main()
