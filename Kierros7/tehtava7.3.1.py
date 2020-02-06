# TIE-02100 Johdatus ohjelmointiin
# Tehtävä: sanakirja, ohjelmakoodipohja


def main():
    suomi_espanja = {"moi": "hola", "kiitos": "gracias", "ranta": "playa"}

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

        elif komento == "P":
            poistettava = input("Syötä poistettava sana suomeksi: ")
            if poistettava in suomi_espanja:
                del suomi_espanja[poistettava]
            else:
                print("Sanaa", poistettava, "ei löydy sanakirjasta.")

        elif komento == "T":
            for sana in sorted(suomi_espanja):
                print(sana, suomi_espanja[sana])

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
