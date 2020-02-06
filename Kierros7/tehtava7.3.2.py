# TIE-02100 Johdatus ohjelmointiin
# Tehtävä: sanakirja, ohjelmakoodipohja


def tulosta_sanakirja(sanakirja):
    idx = 0
    print("Sanakirjan sisältö:")
    for sana in sorted(sanakirja):
        print(sana, end="", sep="")
        idx += 1
        if idx < len(sanakirja):
            print(", ", end="")
    print()


def tulosta_käännökset(sanakirja1, sanakirja2):
    print()
    print("Suomi-espanja:")
    for sana in sorted(sanakirja1):
        print(sana, sanakirja1[sana])
    print()
    print("Espanja-suomi:")
    for sana in sorted(sanakirja2):
        print(sana, sanakirja2[sana])
    print()


def main():
    espanja_suomi = {}
    suomi_espanja = {"moi": "hola", "kiitos": "gracias", "ranta": "playa"}
    for sana in suomi_espanja:
        espanja_suomi[suomi_espanja[sana]] = sana

    tulosta_sanakirja(suomi_espanja)

    while True:
        komento = input("[S]ana/[L]isää/[P]oista/[T]ulosta/[K]äännä/[Q]uit: ")

        if komento == "S":
            sana = input("Syötä käännettävä sana: ")
            if sana in suomi_espanja:
                print(sana, "espanjaksi on", suomi_espanja[sana])
            else:
                print("Sanaa", sana, "ei löydy sanakirjasta.")

        elif komento == "L":
            suomeksi = input("Syötä lisättävä sana suomeksi: ")
            espanjaksi = input("Syötä lisättävä sana espanjaksi: ")
            suomi_espanja[suomeksi] = espanjaksi
            espanja_suomi[espanjaksi] = suomeksi
            tulosta_sanakirja(suomi_espanja)

        elif komento == "P":
            poistettava = input("Syötä poistettava sana suomeksi: ")
            if poistettava in suomi_espanja:
                del suomi_espanja[poistettava]
            else:
                print("Sanaa", poistettava, "ei löydy sanakirjasta.")

        elif komento == "T":
            tulosta_käännökset(suomi_espanja, espanja_suomi)

        elif komento == "K":
            syöte = input("Syötä käännettävä teksti suomeksi: ")
            sanat = syöte.split(" ")
            käännös = ""
            for sana in sanat:
                if sana in suomi_espanja:
                    käännös += suomi_espanja[sana] + " "
                else:
                    käännös += sana + " "
            print("Teksti sanakirjan varassa käännettynä:")
            print(käännös)

        elif komento == "Q":
            print("Adios!")
            return

        else:
            print("Virheellinen komento, syötä joko S, L, P, T, K tai Q!")


main()
