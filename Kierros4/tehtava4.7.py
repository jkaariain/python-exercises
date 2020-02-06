# Johdatus ohjelmointiin
# Koodipohja geometrisia kuvioita varten
import math

def tulosta(ymparysmitta, pinta_ala):
    """
    Tulostaa ympärysmitan ja pinta-alan arvot
    :param ymparysmitta: ympärysmitan arvo
    :param pinta_ala: pinta-alan arvo
    :return:
    """
    print("Ympärysmitta on {:.2f}".format(ymparysmitta))
    print("Pinta-ala on {:.2f}".format(pinta_ala))


def neliö():
    """
    Tulostaa neliön ympärysmitan ja pinta-alan neliön sivun arvolla
    :return:
    """
    sivun_pituus = -1
    while sivun_pituus <= 0:
        sivun_pituus = float(input("Syötä neliön sivun pituus: "))
    tulosta(sivun_pituus*4, sivun_pituus ** 2)


def suorakaide():
    """
    Tulostaa suorakaiteen ympärysmitan ja pinta-alan annetuilla arvoilla
    :return:
    """
    s1, s2 = -1, -1
    while s1 <= 0:
        s1 = float(input("Syötä suorakaiteen sivun 1 pituus: "))
    while s2 <= 0:
        s2 = float(input("Syötä suorakaiteen sivun 2 pituus: "))
    tulosta(s1*2 + s2*2, s1*s2)


def ympyrä():
    """
    Tulostaa ympyrän ympärysmitan ja pinta-alan ympyrän säteen arvolla
    :return:
    """
    säde = -1
    while säde <= 0:
        säde = float(input("Syötä ympyrän säde: "))
    tulosta(2*math.pi*säde, math.pi* säde ** 2)


def valikko():
    """
    Tulostaa valikon, josta käyttäjä voi valita vaihtoehdon
    :return:
    """
    while True:
        vastaus = input("Syötä kuvion alkukirjain, q lopettaa (n/s/y/q): ")
        if vastaus == "n":
            neliö()
        elif vastaus == "s":
            suorakaide()
        elif vastaus == 'y':
            ympyrä()
        elif vastaus == "q":
            return
        else:
            print("Virheellinen syöte, yritä uudelleen!")
        print()  # Tyhjä rivi, että ohjelman tulostetta on helpompi lukea


def main():
    """
    Main-funktio
    :return:
    """
    valikko()
    print("Näkemiin!")


main()
